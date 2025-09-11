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
        self.base_path = r"<local_project_directory>"   # Example : r"F:\Preetham\Optimization"

        # OpenFOAM case location in WSL (Windows path mapping)
        self.foam_directory = r"\\wsl$\<DistroName>\home\<username>\OpenFOAM\<username>-<version>\run"  # Example : r"\\wsl$\Ubuntu-Preetham\home\cfduser\OpenFOAM\cfduser-12\run" 

        # OpenFOAM case path inside WSL (Linux path)
        self.wsl_foam_path = r"~/OpenFOAM/<username>-<version>/run/<case_name>"     # Example : r"~/OpenFOAM/cfduser-12/run/01_optimization"


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

        # Path to design table and final output CSV
        self.design_table_csv = os.path.join(self.base_path, "optimization_designs_data_table.csv")
        # self.final_csv = os.path.join(self.base_path, "data.csv")

        # CAD-related paths
        self.cad_script = os.path.join(self.base_path, "src","template", "spaceclaim_cylinder_in_pipe.py")
        self.cad_folder = os.path.join(self.base_path, "generations","cad")
        self.save_cad = os.path.join(self.base_path, "generations","cad", "CIP_Design-")

        # Mesh-related paths
        self.mesh_folder = os.path.join(self.base_path, "generations","mesh")
        self.save_mesh = os.path.join(self.base_path, "generations","mesh", "CIP_mesh-")

        # Foam Simulation-related paths
        self.foam_case = os.path.join(self.foam_directory, "01_cylinder_in_pipe_optimization")
        self.simulation_data_csv = os.path.join(self.foam_case, "data.csv")
        self.residual_probes = os.path.join(self.base_path, "generations", "residuals_probes")


        # Log file
        self.log_file = os.path.join(self.base_path, "logs","log.log")
        self.log_folder = os.path.join(self.base_path, "logs")
        
        # Results visuals
        self.results_visuals = os.path.join(self.base_path, "generations", "results_visuals")
        self.optimization_result = os.path.join(self.base_path, "result_of_optimization_study")
        self.pareto_front_solution = os.path.join(self.base_path, "result_of_optimization_study", "pareto_front_solutions.csv")