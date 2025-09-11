#######################################################################################
# Import required libraries/modules
# =====================================================================================
import time
import os
import shutil
import pandas as pd
from ansys.geometry.core import launch_modeler
from ansys.geometry.core.modeler import Modeler
import subprocess

from utils.config import Config

config = Config()

class Spaceclaim:
    def __init__(self, parameter_0, parameter_1, design_number):

        self.parameter_0 = int(parameter_0)
        self.parameter_1 = float(parameter_1)
        self.design_number = int(design_number)

    def execute(self):
        print(f"Running SpaceClaim with the design: {self.design_number}")

        # Start timing
        start_time = time.time()

        modeler = launch_modeler(mode='spaceclaim', hidden=False)
        
        _,design = modeler.run_discovery_script_file(file_path=config.cad_script, script_args={
            "parameter_0": f"{self.parameter_0}",
            "parameter_1": f"{self.parameter_1}",
            "design_number": f"{self.design_number}"}, import_design=True)

        design.export_to_pmdb(config.save_cad+str(self.design_number))
        modeler.close()

        # End timing
        end_time = time.time()
        modeling_time = round(end_time - start_time, 2)  # in seconds

        print(f"SpaceClaim execution of design {self.design_number} completed in {modeling_time} seconds.\n")

        
        df = pd.read_csv(config.design_table_csv)

        # Update the last row (newest design)
        if not df.empty:
            df.loc[df["Design Number"] == self.design_number, "SpaceClaim Modeling Time [s]"] = modeling_time
            df.to_csv(config.design_table_csv, index=False)
        else:
            print("Design table is empty. Cannot update modeling time.")

        time.sleep(5)  # Pause for 10 seconds

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

        
        # Kill any running SpaceClaim processes
        subprocess.call('taskkill /F /IM SpaceClaim.exe /T', shell=True)
        

if __name__ == "__main__":
    cad = Spaceclaim( 60,60,1)
    cad.execute()