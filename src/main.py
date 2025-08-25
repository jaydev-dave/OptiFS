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
matplotlib.use("Agg")  # Set headless backend before importing pyplot
import matplotlib.pyplot as plt
import signal
import subprocess

from utils.config import Config
from utils.spaceclaim import Spaceclaim
from utils.pyfluent_meshing import FluentMeshing
from utils.openfoam import OpenFOAM

def kill_background_processes():
    print("\nCleaning up background processes...")
    apps_to_kill = ["SpaceClaim.exe", "fluent.exe", "fluentlauncher.exe", "mpiexec.exe", "hydra_pmi_proxy.exe"]
    for app in apps_to_kill:
        subprocess.call(f"taskkill /F /IM {app} /T", shell=True)

#---------------------------------------------------------------------#

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

# Redirect both stdout and stderr
config = Config()
sys.stdout = Logger(config.log_file)  
sys.stderr = Logger(config.log_file)  # Add this line


#---------------------------------------------------------------------#



class MainOptimizationProblem(Problem):
    def __init__(self):
        super().__init__(
            n_var=7,
            n_obj=2,
            n_constr=2,
            xl=np.array([
                config.core_diameter[0],
                config.blade_count[0],
                config.blade_angle[0],
                config.blade_height[0],
                config.eff_sep_cham_length[0],
                config.imm_pipe_diameter[0],
                config.imm_pipe_length[0]
            ]),
            xu=np.array([
                config.core_diameter[1],
                config.blade_count[1],
                config.blade_angle[1],
                config.blade_height[1],
                config.eff_sep_cham_length[1],
                config.imm_pipe_diameter[1],
                config.imm_pipe_length[1]
            ])
        )
        
    def _evaluate(self, X, out, *args, **kwargs):
        # Check if the foam_case directory does not exist
        if not os.path.exists(config.foam_case):
            shutil.copytree(
                src=os.path.join(config.reference, "wsl_openfoam_case", "01_spark_arrestor_optimization"),
                dst=config.foam_case
            )

        f1_list = []  # Pressure Drop
        f2_list = []  # Centrifugal Acceleration (negated)
        g1_list = []   # Constraint: 0.6 - swirl_number
        g2_list = []    # Constraint: pressure_drop - 2500

        print("\n\n X:")
        for row in X:
            print([round(val, 2) for val in row])
        print("\n")
        
        
        for input in X:
            # Round/clip inputs to valid discrete steps
            diff = (config.core_diameter[1] - config.core_diameter[0]) / 3
            if config.core_diameter[0] <= input[0] < config.core_diameter[0] + diff:
                core_diameter = 116
            elif config.core_diameter[0] + diff <= input[0] < config.core_diameter[0] + 2 * diff:
                core_diameter = 132
            else:
                core_diameter = 146
            blade_count = int(round((input[1] - config.blade_count[0]) / config.blade_count[2]) * config.blade_count[2] + config.blade_count[0] )  # 1 step
            blade_angle = int(round((input[2] - config.blade_angle[0]) / config.blade_angle[2]) * config.blade_angle[2] + config.blade_angle[0])
            blade_height = int(round((input[3] - config.blade_height[0]) / config.blade_height[2]) * config.blade_height[2] + config.blade_height[0])
            eff_sep_cham_length = int(round((input[4] - config.eff_sep_cham_length[0]) / config.eff_sep_cham_length[2]) * config.eff_sep_cham_length[2] + config.eff_sep_cham_length[0])
            imm_pipe_diameter = int(round((input[5] - config.imm_pipe_diameter[0]) / config.imm_pipe_diameter[2]) * config.imm_pipe_diameter[2] + config.imm_pipe_diameter[0])
            imm_pipe_length = int(round((input[6] - config.imm_pipe_length[0]) / config.imm_pipe_length[2]) * config.imm_pipe_length[2] + config.imm_pipe_length[0])



            current_design = {
                                "Core Diameter [mm]": core_diameter,
                                "Blade Count": blade_count,
                                "Blade Angle [deg]": blade_angle,
                                "Blade Height [mm]": blade_height,
                                "Eff Sep Cham Length [mm]": eff_sep_cham_length,
                                "Imm Pipe Diameter [mm]": imm_pipe_diameter,
                                "Imm Pipe Length [mm]": imm_pipe_length
                            }
            
            
            if os.path.exists(config.design_table_csv):
                table_df = pd.read_csv(config.design_table_csv)

                # Remove rows where any key parameter is NaN
                parameter_columns = ["SpaceClaim Modeling Time [s]", "Fluent Meshing Time [s]", "OpenFOAM Time [s]", "Swirl Number", 
                                     "Pressure Drop [Pa]", "Centrifugal Acceleration [m/s²]"]
                table_df.dropna(subset=parameter_columns, how='any', inplace=True)
                table_df.to_csv(config.design_table_csv, index=False)

            else:
                columns = ["Design Number", "Core Diameter [mm]", "Blade Count", "Blade Angle [deg]", "Blade Height [mm]",  "Eff Sep Cham Length [mm]" , "Imm Pipe Diameter [mm]", 
                        "Imm Pipe Length [mm]", "SpaceClaim Modeling Time [s]", "Fluent Meshing Time [s]", "OpenFOAM Time [s]", "Swirl Number", 
                        "Pressure Drop [Pa]", "Centrifugal Acceleration [m/s²]"]
                table_df = pd.DataFrame(columns=columns)
                table_df.to_csv(config.design_table_csv, index=False)

         

            # Check if this design is already present in the table
            is_duplicate = (
                (table_df["Core Diameter [mm]"] == core_diameter) &
                (table_df["Blade Count"] == blade_count) &
                (table_df["Blade Angle [deg]"] == blade_angle) &
                (table_df["Blade Height [mm]"] == blade_height) &
                (table_df["Eff Sep Cham Length [mm]"] == eff_sep_cham_length) &
                (table_df["Imm Pipe Diameter [mm]"] == imm_pipe_diameter) &
                (table_df["Imm Pipe Length [mm]"] == imm_pipe_length)
            ).any()

            # Skip if design already exists
            if is_duplicate:
                print(f"Repetitive design reused: {current_design}")
                match = table_df[(table_df["Core Diameter [mm]"] == core_diameter) &
                                 (table_df["Blade Count"] == blade_count) &
                                 (table_df["Blade Angle [deg]"] == blade_angle) &
                                 (table_df["Blade Height [mm]"] == blade_height) &
                                 (table_df["Eff Sep Cham Length [mm]"] == eff_sep_cham_length) &
                                 (table_df["Imm Pipe Diameter [mm]"] == imm_pipe_diameter) &
                                 (table_df["Imm Pipe Length [mm]"] == imm_pipe_length)]

                pressure_drop = float(match["Pressure Drop [Pa]"].values[0])
                centrifugal_acc = float(match["Centrifugal Acceleration [m/s²]"].values[0])
                swirl_number = float(match["Swirl Number"].values[0])

                f1_list.append(pressure_drop)
                f2_list.append(-centrifugal_acc)
                g1_list.append(0.6 - swirl_number)
                g2_list.append(pressure_drop - 2000)

                continue
            

            design_number = len(table_df) + 1
            # Append current design to table with placeholders
            current_design_row = {
                "Design Number": design_number,
                "Core Diameter [mm]": core_diameter,
                "Blade Count": blade_count,
                "Blade Angle [deg]": blade_angle,
                "Blade Height [mm]": blade_height,
                "Eff Sep Cham Length [mm]": eff_sep_cham_length,
                "Imm Pipe Diameter [mm]": imm_pipe_diameter,
                "Imm Pipe Length [mm]": imm_pipe_length
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

            try:
                simulation = MainSimulation(core_diameter, blade_count, blade_angle, blade_height, eff_sep_cham_length, imm_pipe_diameter, imm_pipe_length, design_number)
                simulation.execute()
            finally:
                # Restore the original stdout/stderr
                sys.stdout = original_stdout
                sys.stderr = original_stderr 

            table_df = pd.read_csv(config.design_table_csv)  # Re-read to update
            current_row = table_df[table_df["Design Number"] == design_number]

            # Extract values
            try:
                pressure_drop = float(current_row["Pressure Drop [Pa]"].values[0])
                centrifugal_acc = float(current_row["Centrifugal Acceleration [m/s²]"].values[0])
                swirl_number = float(current_row["Swirl Number"].values[0])

                f1_list.append(pressure_drop)
                f2_list.append(-centrifugal_acc)
                g1_list.append(0.6 - swirl_number)
                g2_list.append(pressure_drop - 2000)
                
            except Exception as e:
                print(f"Missing or invalid result for design {design_number}: {e}")
                continue

            # Objective 1: Minimize pressure drop
            # Objective 2: Maximize centrifugal acceleration → equivalent to minimizing -acceleration
        out["F"] = np.column_stack([f1_list, f2_list])
        out["G"] = np.column_stack([g1_list, g2_list ])
        print("\n")

        print("="*90)
        print(f"{'n_gen':^6} | {'n_eval':^8} | {'n_nds':^6} | {'cv_min':^13} | {'cv_avg':^13} | {'eps':^13} | {'indicator':^12}")
        print("="*90)

        #print("Objective Values (F):")
        #print(out["F"])
        #print("Constraint (G):")
        #print(out["G"])



class MainSimulation():
    def __init__(self, core_diameter, blade_count, blade_angle, blade_height, eff_sep_cham_length, imm_pipe_diameter, imm_pipe_length, design_number):
        self.core_diameter = float(core_diameter)
        self.blade_count = int(blade_count)
        self.blade_angle = float(blade_angle)
        self.blade_height = float(blade_height)
        self.eff_sep_cham_length = float(eff_sep_cham_length)
        self.imm_pipe_diameter = float(imm_pipe_diameter)
        self.imm_pipe_length = float(imm_pipe_length)
        self.design_number = int(design_number)
        


    def execute(self):
        print(f"\n------------- Design {self.design_number} -------------\n")
        print(f"Design Inputs: {self.core_diameter}  {self.blade_count}  {self.blade_angle}  {self.blade_height}  {self.eff_sep_cham_length}  {self.imm_pipe_diameter}  {self.imm_pipe_length}")
        self.cad = Spaceclaim(self.core_diameter, self.blade_count, self.blade_angle, self.blade_height, self.eff_sep_cham_length, self.imm_pipe_diameter, 
                              self.imm_pipe_length, self.design_number)
        self.cad.execute()

        self.mesh = FluentMeshing(self.design_number)
        self.mesh.execute()

        self.simulation = OpenFOAM(self.design_number, self.blade_height)
        self.simulation.execute()



    
# Define the Optimization Algorithm (NSGA-II)
algorithm = NSGA2(
    pop_size=70,  # Population size
    n_offsprings=70,
    sampling=IntegerRandomSampling(),
    crossover=SBX(prob=0.9, eta=20),
    mutation=PM(eta=20),
    eliminate_duplicates=True
)

try:
    problem = MainOptimizationProblem()
    res = minimize(
        problem,
        algorithm,
        termination=["n_gen",40],  
        seed=10,
        save_history=True,
        verbose=True
    )
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

# Check if optimization results are available
if res.F is not None and res.X is not None:
    # Optional: Plot Pareto front
    F_all = np.vstack([gen.pop.get("F") for gen in res.history])  # All evaluated individuals (incl. non-optimal)
    F_pareto = res.F                    # Pareto fron


    # Plot 1: Pareto Front Only
    plt.figure(figsize=(8, 6))
    plt.scatter(F_pareto[:, 0], -F_pareto[:, 1], c='blue', label="Pareto Front", s=50)
    plt.xlabel("Pressure Drop [Pa]")
    plt.ylabel("Centrifugal Acceleration [m/s²]")
    plt.title("Pareto Front")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("pareto_front.png")
    plt.show()

    # Plot 2: All Populations + Highlight Pareto Front
    plt.figure(figsize=(8, 6))
    plt.scatter(F_all[:, 0], -F_all[:, 1], c='lightgray', label="All Solutions", s=30)
    plt.scatter(F_pareto[:, 0], -F_pareto[:, 1], c='blue', label="Pareto Front", s=60)
    plt.xlabel("Pressure Drop [Pa]")
    plt.ylabel("Centrifugal Acceleration [m/s²]")
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
        # Quantize design variables using config step sizes
        core_diameter = int(round((result_X[i, 0] - config.core_diameter[0]) / config.core_diameter[2]) * config.core_diameter[2] + config.core_diameter[0])
        blade_count = int(round((result_X[i, 1] - config.blade_count[0]) / config.blade_count[2]) * config.blade_count[2] + config.blade_count[0])
        blade_angle = int(round((result_X[i, 2] - config.blade_angle[0]) / config.blade_angle[2]) * config.blade_angle[2] + config.blade_angle[0])
        blade_height = int(round((result_X[i, 3] - config.blade_height[0]) / config.blade_height[2]) * config.blade_height[2] + config.blade_height[0])
        eff_sep_cham_length = int(round((result_X[i, 4] - config.eff_sep_cham_length[0]) / config.eff_sep_cham_length[2]) * config.eff_sep_cham_length[2] + config.eff_sep_cham_length[0])
        imm_pipe_diameter = int(round((result_X[i, 5] - config.imm_pipe_diameter[0]) / config.imm_pipe_diameter[2]) * config.imm_pipe_diameter[2] + config.imm_pipe_diameter[0])
        imm_pipe_length = int(round((result_X[i, 6] - config.imm_pipe_length[0]) / config.imm_pipe_length[2]) * config.imm_pipe_length[2] + config.imm_pipe_length[0])

        # Check for duplicate design
        match = table_df[
            (table_df["Core Diameter [mm]"] == core_diameter) &
            (table_df["Blade Count"] == blade_count) &
            (table_df["Blade Angle [deg]"] == blade_angle) &
            (table_df["Blade Height [mm]"] == blade_height) &
            (table_df["Eff Sep Cham Length [mm]"] == eff_sep_cham_length) &
            (table_df["Imm Pipe Diameter [mm]"] == imm_pipe_diameter) &
            (table_df["Imm Pipe Length [mm]"] == imm_pipe_length)
        ]

        if not match.empty:
            design_number = int(match["Design Number"].values[0])
        else:
            design_number = int(table_df["Design Number"].max() + 1) if not table_df.empty else 1
            # Optional: append new design to table_df if you're updating the master table

        # Append design to list
        df_pareto_list.append({
            "Design Number": design_number,
            "Core Diameter [mm]": core_diameter,
            "Blade Count": blade_count,
            "Blade Angle [deg]": blade_angle,
            "Blade Height [mm]": blade_height,
            "Eff Sep Cham Length [mm]": eff_sep_cham_length,
            "Imm Pipe Diameter [mm]": imm_pipe_diameter,
            "Imm Pipe Length [mm]": imm_pipe_length,
            "Swirl Number": round(0.6 - res.G[i, 0], 2),
            "Pressure Drop [Pa]": round(res.F[i, 0], 2),
            "Centrifugal Acceleration [m/s²]": round(-res.F[i, 1], 2)
        })

    # Combine all rows into one DataFrame
    df_pareto = pd.DataFrame(df_pareto_list)

    # Round first 8 columns to 0 decimals
    df_pareto.iloc[:, 1:8] = df_pareto.iloc[:, 1:8].round(0)

    # Save to CSV
    df_pareto.to_csv(config.pareto_front_solution, index=False)
    print(f"\nPareto-optimal designs exported to '{config.pareto_front_solution}'")
else:
    print("ERROR: Optimization result is incomplete or failed (res.F or res.X is None). Skipping export and plot.")

