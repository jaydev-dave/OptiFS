#######################################################################################
# Import required libraries/modules
# =====================================================================================
import numpy as np
import autograd.numpy as anp
import pandas as pd
from pymoo.core.problem import Problem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize
from pymoo.operators.sampling.rnd import IntegerRandomSampling
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.operators.selection.tournament import TournamentSelection
from pymoo.core.termination import Termination
from pymoo.termination import get_termination
import os
import sys
import shutil
import matplotlib 
matplotlib.use("Agg")  
import matplotlib.pyplot as plt
import signal
import subprocess

from utils.config import Config
from utils.spaceclaim import Spaceclaim
from utils.pyfluent_meshing import FluentMeshing
from utils.openfoam import OpenFOAM



#######################################################################################
# Function to kill all relevant software used in this Optimization study
# =====================================================================================
def kill_background_processes():
    print("\nCleaning up background processes...")
    apps_to_kill = ["SpaceClaim.exe", "fluent.exe", "fluentlauncher.exe", "mpiexec.exe", "hydra_pmi_proxy.exe"]
    for app in apps_to_kill:
        subprocess.call(f"taskkill /F /IM {app} /T", shell=True)


#######################################################################################
# Class to create log file
# =====================================================================================
class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()

    def __del__(self):
        self.log.close()

config = Config()
sys.stdout = Logger(config.log_file)  
sys.stderr = Logger(config.log_file)  


#######################################################################################
# Main Optimization Class inheriting from pymoo Problem interface
# =====================================================================================
class MainOptimizationProblem(Problem):
    def __init__(self):
        super().__init__(
            n_var=config.num_variables,
            n_obj=config.num_objectives,
            n_constr=config.num_constraints,   # no constraints
            xl=np.array([
                config.parameter_0[0],   # Cylinder Length lower bound
                config.parameter_1[0]    # Cylinder Diameter lower bound
            ]),
            xu=np.array([
                config.parameter_0[1],   # Cylinder Length upper bound
                config.parameter_1[1]    # Cylinder Diameter upper bound
            ])
        )
    

    def _evaluate(self, X, out, *args, **kwargs):

        #######################################################################################
        # Check if foam_case directory exists
        # =====================================================================================
        if not os.path.exists(config.foam_case):
            shutil.copytree(
                src=os.path.join(config.reference, "wsl_openfoam_case", "01_cylinder_in_pipe_optimization"),
                dst=config.foam_case
            )

        f1_list = []  # Pressure Drop
        f2_list = []  # Drag Force of the cylinder 
        g1_list = []  # Placeholder for constraints (if any)

        #######################################################################################
        # Print every variable set for the current generation
        # =====================================================================================
        print("\n\n X:")
        for row in X:
            print([round(val, 2) for val in row])
        print("\n")
        
        
        #######################################################################################
        # Run the simulation for each variable set 
        # =====================================================================================
        for input in X:

            # index fix: input[0] = length, input[1] = diameter
            parameter_0 = int(round((input[0] - config.parameter_0[0]) / config.parameter_0[2]) * config.parameter_0[2] + config.parameter_0[0])  
            parameter_1 = int(round((input[1] - config.parameter_1[0]) / config.parameter_1[2]) * config.parameter_1[2] + config.parameter_1[0])

            current_design = {
                                "Cylinder Length": parameter_0,
                                "Cylinder Diameter": parameter_1
                            }
            
            #######################################################################################
            # Create main Design Table if not present; otherwise remove incomplete rows  
            # =====================================================================================
            if os.path.exists(config.design_table_csv):
                table_df = pd.read_csv(config.design_table_csv)

                # Remove rows where any key parameter is NaN
                parameter_columns = ["SpaceClaim Modeling Time [s]", "Fluent Meshing Time [s]", "OpenFOAM Time [s]", "Drag [N]", 
                                     "Pressure Drop [Pa]"]
                table_df.dropna(subset=parameter_columns, how='any', inplace=True)
                table_df.to_csv(config.design_table_csv, index=False)

            else:
                columns = ["Design Number", "Cylinder Length", "Cylinder Diameter", "SpaceClaim Modeling Time [s]", "Fluent Meshing Time [s]", "OpenFOAM Time [s]", "Drag [N]", 
                        "Pressure Drop [Pa]"]
                table_df = pd.DataFrame(columns=columns)
                table_df.to_csv(config.design_table_csv, index=False)

         
            #######################################################################################
            # If design already exists in table, retrieve results and skip simulation
            # =====================================================================================
            is_duplicate = (
                (table_df["Cylinder Length"] == parameter_0) &
                (table_df["Cylinder Diameter"] == parameter_1)
            ).any()

            if is_duplicate:
                print(f"Repetitive design reused: {current_design}")
                match = table_df[(table_df["Cylinder Length"] == parameter_0) &
                                 (table_df["Cylinder Diameter"] == parameter_1) ]

                pressure_drop = float(match["Pressure Drop [Pa]"].values[0])
                drag = float(match["Drag [N]"].values[0])

                f1_list.append(pressure_drop)
                f2_list.append(drag)

                continue
            
            #######################################################################################
            # Append new design to table and create corresponding log file
            # =====================================================================================
            design_number = len(table_df) + 1

            current_design_row = {
                "Design Number": design_number,
                "Cylinder Length": parameter_0,
                "Cylinder Diameter": parameter_1,
            }

            table_df = pd.concat([table_df, pd.DataFrame([current_design_row])], ignore_index=True)
            table_df.to_csv(config.design_table_csv, index=False)

            # Save current stdout/stderr
            original_stdout = sys.stdout
            original_stderr = sys.stderr

            # Create a new logger for the specific design
            design_log_path = os.path.join(config.log_folder, f"log_design-{design_number}.txt")
            sys.stdout = Logger(design_log_path)
            sys.stderr = Logger(design_log_path)


            #######################################################################################
            # Execute complete simulation using MainSimulation class
            # =====================================================================================
            try:
                simulation = MainSimulation(parameter_0, parameter_1, design_number)
                simulation.execute()
            finally:
                sys.stdout = original_stdout
                sys.stderr = original_stderr 

            table_df = pd.read_csv(config.design_table_csv)  # Re-read to update
            current_row = table_df[table_df["Design Number"] == design_number]

            #######################################################################################
            # Extract results (objectives)
            # =====================================================================================
            try:
                pressure_drop = float(current_row["Pressure Drop [Pa]"].values[0])
                drag = float(current_row["Drag [N]"].values[0])

                f1_list.append(pressure_drop)
                f2_list.append(drag)

            except Exception as e:
                print(f"Missing or invalid result for design {design_number}: {e}")
                continue

        # Objective 1: Minimize pressure drop
        # Objective 2: Minimize drag
        out["F"] = np.column_stack([f1_list, f2_list])
        print("\n")

        print("="*90)
        print(f"{'n_gen':^6} | {'n_eval':^8} | {'n_nds':^6} | {'cv_min':^13} | {'cv_avg':^13} | {'eps':^13} | {'indicator':^12}")
        print("="*90)


#######################################################################################
# MainSimulation class executes the full simulation workflow using input from pymoo
# =====================================================================================
class MainSimulation():
    def __init__(self, parameter_0, parameter_1, design_number):
        self.parameter_0 = int(parameter_0)    # Cylinder Length
        self.parameter_1 = float(parameter_1)  # Cylinder Diameter
        self.design_number = int(design_number)
        

    def execute(self):
        print(f"\n------------- Design {self.design_number} -------------\n")
        print(f"Design Inputs: {self.parameter_0}  {self.parameter_1} ")

        #######################################################################################
        # Instantiate SpaceClaim class to generate CAD
        # =====================================================================================
        self.cad = Spaceclaim( self.parameter_0, self.parameter_1,  self.design_number)
        self.cad.execute()

        #######################################################################################
        # Instantiate FluentMeshing class to perform meshing
        # =====================================================================================
        self.mesh = FluentMeshing(self.design_number)
        self.mesh.execute()

        #######################################################################################
        # Instantiate OpenFOAM class to run simulation and post-process results
        # =====================================================================================
        self.simulation = OpenFOAM(self.design_number)
        self.simulation.execute()



#######################################################################################
# Define the Optimization Algorithm (NSGA-II) 
# =====================================================================================
algorithm = NSGA2(
    pop_size=config.population_size,  
    n_offsprings=config.offsprings_size,
    sampling=IntegerRandomSampling(),
    crossover=SBX(prob=config.crossover_probability, eta=config.crossover_eta),
    mutation=PM(eta=config.mutation_eta),
    eliminate_duplicates=True
)

#######################################################################################
# Run the optimization framework
# =====================================================================================
try:
    problem = MainOptimizationProblem()
    res = minimize(
        problem,
        algorithm,
        termination=["n_gen",config.num_generations],  
        seed=config.seed,
        save_history=True,
        verbose=True
    )

#######################################################################################
# Kill relevant background processes on error or completion
# =====================================================================================
except KeyboardInterrupt:
    print("Interrupted by user.")
    kill_background_processes()
    sys.exit(1)
except Exception as e:
    print(f"Unhandled exception: {e}")
    kill_background_processes()
    sys.exit(1) 
finally:
    kill_background_processes()
    sys.exit(1)


#######################################################################################
# If optimization results exist, plot them 
# =====================================================================================

if res.F is not None and res.X is not None:
    # Optional: Plot Pareto front
    F_all = np.vstack([gen.pop.get("F") for gen in res.history])  # All evaluated individuals (incl. non-optimal)
    F_pareto = res.F                    # Pareto fron


    # Plot Pareto Front
    plt.figure(figsize=(8, 6))
    plt.scatter(F_pareto[:, 0], F_pareto[:, 1], c='blue', label="Pareto Front", s=50)
    plt.xlabel("Pressure Drop [Pa]")
    plt.ylabel("Drag Force [N]")
    plt.title("Pareto Front")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("pareto_front.png")
    plt.show()

    # All solutions with Pareto Front
    plt.figure(figsize=(8, 6))
    plt.scatter(F_all[:, 0], F_all[:, 1], c='lightgray', label="All Solutions", s=30)
    plt.scatter(F_pareto[:, 0], F_pareto[:, 1], c='blue', label="Pareto Front", s=60)
    plt.xlabel("Pressure Drop [Pa]")
    plt.ylabel("Drag Force [N]")
    plt.title("All Evaluated Solutions with Pareto Front")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("all_solutions_with_pareto_front.png")
    plt.show()

    result_X = res.X
    df_pareto_list = []

    # Read design table once before loop
    table_df = pd.read_csv(config.design_table_csv)

    for i in range(len(result_X)):
        # Correct indexing: result_X has only 2 variables (0 = Length, 1 = Diameter)
        parameter_0 = int(round((result_X[i, 0] - config.parameter_0[0]) / config.parameter_0[2]) * config.parameter_0[2] + config.parameter_0[0])
        parameter_1 = int(round((result_X[i, 1] - config.parameter_1[0]) / config.parameter_1[2]) * config.parameter_1[2] + config.parameter_1[0])

        # Check for duplicate design
        match = table_df[
            (table_df["Cylinder Length"] == parameter_0) &
            (table_df["Cylinder Diameter"] == parameter_1)
        ]

        if not match.empty:
            design_number = int(match["Design Number"].values[0])
        else:
            design_number = int(table_df["Design Number"].max() + 1) if not table_df.empty else 1

        # Append design to list
        df_pareto_list.append({
            "Design Number": design_number,
            "Cylinder Length": parameter_0,
            "Cylinder Diameter": parameter_1,
            "Pressure Drop [Pa]": round(res.F[i, 0], 2),   # first objective
            "Drag Force [N]": round(res.F[i, 1], 2)       # second objective
        })

    # Combine all rows into one DataFrame
    df_pareto = pd.DataFrame(df_pareto_list)

    # Round Length and Diameter only (not objectives!)
    df_pareto[["Cylinder Length", "Cylinder Diameter"]] = df_pareto[["Cylinder Length", "Cylinder Diameter"]].round(0)

    # Save to CSV
    df_pareto.to_csv(config.pareto_front_solution, index=False)
    print(f"\nPareto-optimal designs exported to '{config.pareto_front_solution}'")
else:
    print("ERROR: Optimization result is incomplete or failed (res.F or res.X is None). Skipping export and plot.")
