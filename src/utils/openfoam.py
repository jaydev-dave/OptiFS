#######################################################################################
# Import required libraries/modules
# =====================================================================================
import os
import shutil
import time
import subprocess
import pandas as pd
import numpy as np

from utils.config import Config
from utils.plotter import Plotter 

config = Config()

class OpenFOAM:
    def __init__(self, design_number):
        self.design_number = design_number

        

    def execute(self):
        print(f"Running Openfoam Simulation with the design: {self.design_number}")
        

        if os.path.exists(rf"{config.foam_case_run}/mesh.msh"):
            os.remove(rf"{config.foam_case_run}/mesh.msh") 

        #copy and rename mesh file to case directory
        self.mesh_path = rf"{config.mesh_folder}\mesh-"+str(self.design_number)+".msh"
        original_msh = rf"{config.foam_case_run}\\mesh-"+str(self.design_number)+".msh"
        renamed_msh = rf"{config.foam_case_run}\\mesh.msh"

        shutil.copy(self.mesh_path,config.foam_case_run)
        os.rename(original_msh,renamed_msh)

        if os.path.exists(self.mesh_path):
            os.remove(self.mesh_path) 
        



        #Start timing
        start_time = time.time()
        design_log_path = os.path.join(config.log_folder, f"log_design-{self.design_number}.txt")
        wsl_command = f'wsl bash -c "cd {config.wsl_foam_path} && chmod +x shell_script.sh && ./shell_script.sh"'

        with open(design_log_path, "a") as log_file:
            process = subprocess.Popen(wsl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
            for line in process.stdout:
                print(line, end='')       # Print to terminal
            process.wait()


        # Generate and save plots 
        plotter = Plotter(self.design_number)
        plotter.generate_plots()

        image_paths = [rf"{config.foam_case_run}\U.png",
                       rf"{config.foam_case_run}\LIC.png",
                       rf"{config.residual_probes}\residuals_design-{self.design_number}.png",
                       rf"{config.residual_probes}\probe_U_design-{self.design_number}.png",
                       rf"{config.residual_probes}\probe_press_design-{self.design_number}.png",]
        
        collage_output_path  = rf"{config.results_visuals}\results_visuals_design-{self.design_number}"

        plotter.create_collage(image_paths,collage_output_path)


        # Read CFD output
        cf = pd.read_csv(config.simulation_data_csv)

        # Extract swirl number data from mid-IntVar
        mid_row = cf[cf['Block Name'] == 'cyc-IntVar'].iloc[0]
        drag = mid_row['drag']
        lift = mid_row['lift']


        # Extract pressure data
        p1 = cf[cf['Block Name'] == 'down-IntVar']['p'].values[0]
        p2 = cf[cf['Block Name'] == 'up-IntVar']['p'].values[0]
        pressure_drop = abs(p1 - p2)*1.184

        # Read and update the design table
        table_df = pd.read_csv(config.design_table_csv)
        row_index = table_df.index[table_df["Design Number"] == self.design_number].tolist()

        if row_index:
            idx = row_index[0]
            table_df.at[idx, "Drag [N]"] = round(drag, 2)
            table_df.at[idx, "Pressure Drop [Pa]"] = round(pressure_drop, 2)


            # Save back the updated table
            table_df.to_csv(config.design_table_csv, index=False)
        else:
            print(f"Design Number {self.design_number} not found in the table.")


        # End timing
        end_time = time.time()
        modeling_time = round(end_time - start_time, 2)  # in seconds

        print(f"OpenFOAM Simulation & Post-Processing of design {self.design_number} completed in {modeling_time} seconds.\n")

        
        df = pd.read_csv(config.design_table_csv)

        # Update the last row (newest design)
        if not df.empty:
            df.loc[df["Design Number"] == self.design_number, "OpenFOAM Time [s]"] = modeling_time
            df.to_csv(config.design_table_csv, index=False)
        else:
            print("Design table is empty. Cannot update modeling time.")


        # Clean __pycache__ from utils
        for item in os.listdir(config.utils):
            full_path = os.path.join(config.utils, item)
            if item.startswith("__pycache__"):
                try:
                    if os.path.isfile(full_path):
                        os.remove(full_path)
                    elif os.path.isdir(full_path):
                        shutil.rmtree(full_path)
                except Exception as e:
                    print(f"Could not remove {full_path}: {e}")

        # Clean template folder
        for item in os.listdir(config.template):
            full_path = os.path.join(config.template, item)
            if item.endswith(".trn") or item.endswith(".bat") or item.startswith("FM"):
                try:
                    if os.path.isfile(full_path):
                        os.remove(full_path)
                    elif os.path.isdir(full_path):
                        shutil.rmtree(full_path)
                except Exception as e:
                    print(f"Could not remove {full_path}: {e}")

        # Clean mesh folder
        for item in os.listdir(config.mesh_folder):
            full_path = os.path.join(config.mesh_folder, item)
            if item.endswith("workflow_files") or item.startswith("fluent"):
                try:
                    if os.path.isfile(full_path):
                        os.remove(full_path)
                    elif os.path.isdir(full_path):
                        shutil.rmtree(full_path)
                except Exception as e:
                    print(f"Could not remove {full_path}: {e}")
        

        
if __name__ == "__main__":
        # Generate and save plots using the PlotResiduals class
        simulation = OpenFOAM(1)

        simulation.execute()
