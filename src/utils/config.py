import os

class Config:
    def __init__(self):


        #######################################################################################
        # Parametric Variables defined as (Min, Max, Step size)
        # =====================================================================================
        self.parameter_0 = (50, 100, 5) # Cylinder Length            
        self.parameter_1 = (50, 150, 10)   # Cylinder Diameter


        #######################################################################################
        # Optimization Algorithm Setup
        # =====================================================================================        
        self.population_size = 30
        self.offsprings_size = 30
        self.num_generations = 20

        # Base directory for project files (Windows or local machine)
        self.base_path = r"<local_project_directory>"   # Example : r"F:\Preetham\OptiFS"

        # OpenFOAM case path inside WSL (Linux path)
        self.wsl_foam_path = r"/mnt/<drive_letter>/. . ./reference//wsl_openfoam_case/foam_case_run"     # Example : r"/mnt/f/Preetham/OptiFS/reference/wsl_openfoam_case/foam_case_run"


        #######################################################################################
        # Optimization Algorithm Configuration - Change it if needed or leave it default
        # =====================================================================================        
        self.seed = 10
        self.crossover_probability = 0.9
        self.crossover_eta = 20
        self.mutation_eta = 20

        #######################################################################################
        # Parametric design varaibles
        # =====================================================================================
        self.num_objectives = 2
        self.num_constraints = 0
        self.num_variables = 2 

                       

        

        #######################################################################################
        # Other Paths
        # =====================================================================================        

        self.utils = os.path.join(self.base_path, "src", "utils")
        self.template = os.path.join(self.base_path, "src", "template")
        self.reference = os.path.join(self.base_path, "reference")

        self.foam_directory =os.path.join(self.base_path, "reference", "wsl_openfoam_case")

        # Path to design table and final output CSV
        self.design_table_csv = os.path.join(self.base_path, "optimization_designs_data_table.csv")

        # CAD-related paths
        self.cad_script = os.path.join(self.base_path, "src","template", "spaceclaim_SA_script.py")
        self.cad_folder = os.path.join(self.base_path, "generations","cad")
        self.save_cad = os.path.join(self.base_path, "generations","cad", "SA_Design-")

        # Mesh-related paths
        self.mesh_folder = os.path.join(self.base_path, "generations","mesh")
        self.workflow_path = os.path.join(self.base_path, "src", "template", "fluent_meshing_workflow_new.wft")
        self.save_mesh = os.path.join(self.base_path, "generations","mesh", "SA_mesh-")

        # Foam Simulation-related paths
        self.foam_case_reference = os.path.join(self.foam_directory, "01_spark_arrestor_optimization-355mm")
        self.foam_case_run = os.path.join(self.foam_directory, "foam_case_run")
        self.simulation_data_csv = os.path.join(self.foam_case_run, "data.csv")
        self.residual_probes = os.path.join(self.base_path, "generations", "residuals_probes")


        # Log file
        self.log_file = os.path.join(self.base_path, "logs","log.log")
        self.log_folder = os.path.join(self.base_path, "logs")
        
        # Results visuals
        self.results_visuals = os.path.join(self.base_path, "generations", "results_visuals")
        self.optimization_result = os.path.join(self.base_path, "result_of_optimization_study")
        self.pareto_front_solution = os.path.join(self.base_path, "result_of_optimization_study", "pareto_front_solutions.csv")
