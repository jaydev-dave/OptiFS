#######################################################################################
# Import required libraries/modules
# =====================================================================================
import os
import shutil
import time
import pandas as pd
import ansys.fluent.core as pyfluent
import subprocess


from utils.config import Config


config = Config()

class FluentMeshing:
    def __init__(self, design_number):
        self.design_number = int(design_number)
        self.cad_path = rf"{config.save_cad}"+str(self.design_number)+"\Konstruktion1.pmdb"
        
    def execute(self):
                
        print(f"Running Fluent meshing for the design: {self.design_number}")

        #######################################################################################
        # Copy CAD file to Mesh Folder & Record the starting time
        # =====================================================================================
        self.cad_in_mesh_folder = f"{config.mesh_folder}/Konstruktion1.pmdb"

        if os.path.exists(self.cad_in_mesh_folder):
            os.remove(self.cad_in_mesh_folder)      
        shutil.copy(self.cad_path,config.mesh_folder)

        start_time = time.time()


        #######################################################################################
        # Launch Fluent session with meshing mode
        # =====================================================================================
        meshing = pyfluent.launch_fluent(mode=pyfluent.FluentMode.PURE_MESHING, precision=pyfluent.Precision.DOUBLE, processor_count=4, cwd = config.template, ui_mode=pyfluent.UIMode.GUI) # , ui_mode=pyfluent.UIMode.GUI
        


        #######################################################################################
        # Initialize the Meshing Workflow, Import Geometry
        # =====================================================================================     
        workflow = meshing.workflow
        workflow.InitializeWorkflow(WorkflowType="Watertight Geometry")
        workflow.TaskObject["Import Geometry"].Arguments= dict(
        FileName=self.cad_in_mesh_folder,
            LengthUnit= "m"
        )
        workflow.TaskObject["Import Geometry"].Execute()

        
        #######################################################################################
        # Add Local (Body of Influence) Sizing
        # =====================================================================================
        workflow.TaskObject["Add Local Sizing"].Arguments = dict(
            {
                "AddChild": "yes",
                "BOIControlName": "boi",
                "BOIExecution": "Body Of Influence",
                "BOIFaceLabelList": ["boi-volumenk-rper"], 
                "BOIGrowthRate": 1.2,
                "BOISize": 0.007
            }
        )
        workflow.TaskObject["Add Local Sizing"].Execute()
        workflow.TaskObject["Add Local Sizing"].InsertCompoundChildTask()



        #######################################################################################
        # Add Surface Mesh Sizing
        # =====================================================================================
        workflow.TaskObject["Generate the Surface Mesh"].Arguments = dict(
            {
                "CFDSurfaceMeshControls": {
                    "MaxSize": 0.08,
                    "MinSize": 0.0001,
                    "CellsPerGap": 2,
                }
            }
        )
        workflow.TaskObject["Generate the Surface Mesh"].Execute()
        workflow.TaskObject["Generate the Surface Mesh"].InsertNextTask(CommandName="ImproveSurfaceMesh")
        improve_surface_mesh = workflow.TaskObject["Improve Surface Mesh"]
        improve_surface_mesh.Execute()
        
        #######################################################################################
        # Describe Geometry, Update Boundaries, Update Regions
        # =====================================================================================
        workflow.TaskObject["Describe Geometry"].Arguments = dict(
            #CappingRequired="Yes",
            SetupType="The geometry consists of both fluid and solid regions and/or voids",
        )
        workflow.TaskObject["Describe Geometry"].Execute()
        workflow.TaskObject["Update Boundaries"].Execute()
        workflow.TaskObject["Update Regions"].Execute()
        

        #######################################################################################
        # Add Boundary Layers
        # =====================================================================================       
        add_boundary_layers = workflow.TaskObject["Add Boundary Layers"]
        add_boundary_layers.AddChildToTask()
        add_boundary_layers.InsertCompoundChildTask()
        workflow.TaskObject["smooth-transition_1"].Rename(
            NewName="last-ratio_1"
        )
        workflow.TaskObject["last-ratio_1"].Arguments = dict(
            {
                "BLControlName": "outer",
                "OffsetMethodType": "last-ratio",
                "FirstHeight": 0.0001,
                "NumberOfLayers": 8,
                "FaceScope": {"GrowOn": "selected-labels"},
                "BlLabelList": ["wall_outer"]}
        )
        add_boundary_layers.Execute()
        
        add_boundary_layers.AddChildToTask()
        add_boundary_layers.InsertCompoundChildTask()
        workflow.TaskObject["smooth-transition_1"].Rename(
            NewName="last-ratio_2"
        )
        workflow.TaskObject["last-ratio_2"].Arguments = dict(
            {
                "BLControlName": "cylinder",
                "OffsetMethodType": "last-ratio",
                "FirstHeight": 5e-05,
                "NumberOfLayers": 8,
                "FaceScope": {"GrowOn": "selected-labels"},
                "BlLabelList": ["wall_inner"]}
        )
        add_boundary_layers.Execute()

        #######################################################################################
        # Generate the Volume Mesh
        # =====================================================================================        
        workflow.TaskObject["Generate the Volume Mesh"].Arguments.update_dict({
        "VolumeFill": "polyhedra",
        "VolumeFillControls": {
            "MaxSize": 0.05813,
        },
        })
        
        workflow.TaskObject["Generate the Volume Mesh"].Execute()
        
        
        #######################################################################################
        # Write the mesh file & Close the session
        # =====================================================================================  
        meshing.tui.file.file_format("No")
        meshing.tui.file.cff_files("No")
        meshing.tui.file.write_mesh(rf"{config.save_mesh}"+str(self.design_number)+".msh")
        meshing.exit()



        #######################################################################################
        # Delete CAD file from Mesh Folder & Calculte the total FLuent meshing time
        # =====================================================================================  
        if os.path.exists(self.cad_in_mesh_folder):
            os.remove(self.cad_in_mesh_folder) 

        end_time = time.time()
        modeling_time = round(end_time - start_time, 2)

        print(f"Fluent Meshing execution of design {self.design_number} completed in {modeling_time} seconds.\n")
        df = pd.read_csv(config.design_table_csv)


        #######################################################################################
        # Update the Fluent meshing time in the Main csv file
        # ===================================================================================== 
        if not df.empty:
            df.loc[df["Design Number"] == self.design_number, "Fluent Meshing Time [s]"] = modeling_time
            df.to_csv(config.design_table_csv, index=False)
        else:
            print("Design table is empty. Cannot update modeling time.")

        time.sleep(8)  # Pause some seconds



        #######################################################################################
        # Kill any running fluent processes
        # =====================================================================================  
        subprocess.call('taskkill /F /IM fluent.exe /T', shell=True)
        subprocess.call('taskkill /F /IM fluentlauncher.exe /T', shell=True)
        subprocess.call('taskkill /F /IM mpiexec.exe /T', shell=True)
        subprocess.call('taskkill /F /IM hydra_pmi_proxy.exe /T', shell=True)
        
if __name__ == "__main__":
    mesh = FluentMeshing(1)
    mesh.execute()