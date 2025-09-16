# OptiFS: Optimization Framework with Simulation Software


## Overview
**OptiFS** is a Python-based framework for automating **multi-objective design optimization**, integrating a complete **CAD → Meshing → CFD → Post-processing** pipeline coupled with a genetic algorithm–based optimizer. 

The framework can be configured with different tools at each stage:  
- **CAD generation** – parametric geometry creation (e.g., ANSYS SpaceClaim, SolidWorks, Inventor)  
- **Mesh generation** – automated meshing (e.g., ANSYS Fluent Meshing, Gmsh, SALOME)  
- **Physics simulation** – flow or multiphysics solvers (e.g., OpenFOAM, ANSYS Fluent, STAR-CCM+)  
- **Optimization algorithms** – multi-objective optimization (e.g., NSGA-II, NSGA-III, BRKGA) 


The optimization is performed using the **Non-dominated Sorting Genetic Algorithm II (NSGA-II)** from the [pymoo](https://pymoo.org) library. However, the modular structure allows the substitution of any other optimization algorithm as required.  

OptiFS enables users to select the most suitable software for each stage, balancing simulation cost and unique capabilities. The workflow is extensible to other simulation domains and software with Python interfaces.  


## Project Structure

```
generations/
  cad/                # CAD files for each design
  mesh/               # Mesh files for each design
  residuals_probes/   # Residuals and probe data
  results_visuals/    # Plots and visualizations
logs/                 # Log files
reference/
  wsl_openfoam_case/  # Reference OpenFOAM case and scripts
result_of_optimization_study/ # Final results and plots
src/
  main.py             # Main optimization script
  kill_background_apps.py
  template/
    spaceclaim_cylinder_in_pipe.py
  utils/
    config.py         # Configuration and paths
    spaceclaim.py     # SpaceClaim automation
    pyfluent_meshing.py # Fluent meshing automation
    openfoam.py       # OpenFOAM automation
    plotter.py        # Plotting utilities
```

During execution, the OpenFOAM case folder is copied to the WSL `$FOAM_RUN` directory. CAD files are saved in `generations/cad`, then moved to `generations/mesh` for meshing, and subsequently transferred to the OpenFOAM case directory in WSL for simulation and post-processing.

OptiFS is designed to be extensible. If your preferred CAD or simulation software provides a Python interface, you can adapt the framework to alternatives such as StarCCM+, SALOME, ANSYS Fluent, or other tools. The workflow is applicable to various simulation domains, including structural mechanics, acoustics, and electromagnetics.

The example application is described in detail in the section [Example Application: *Cylinder-in-Pipe*](#example-application-cylinder-in-pipe).  



## Requirements

- Windows Subsystem for Linux (WSL) Version: 2.6.1.0
- [Python 3.10+](https://www.python.org/downloads/)
- [pymoo 0.6.0](https://pymoo.org/)
- [ANSYS SpaceClaim 2025R2](https://www.ansys.com/products/modeling/spaceclaim)
- [ANSYS Fluent 2025R2](https://www.ansys.com/products/fluids/ansys-fluent)
- [OpenFOAM 12](https://openfoam.org/) (recommended via WSL for Windows)
- [Paraview](https://www.paraview.org/) (for post-processing)
- Additional Python packages listed in [requirements.txt](./requirements.txt)

## WSL Display Setup (Windows 10 & XLaunch)

If running OpenFOAM in WSL on Windows 10 with XLaunch (or another X server), set the display environment variable in your shell scripts. For example, in `reference/wsl_openfoam_case/01_cylinder_in_pipe_optimization/shell_script.sh`:

```bash
# #!/bin/bash
. /opt/openfoam12/etc/bashrc
export DISPLAY=$(grep -oP "(?<=nameserver )[0-9\.]+" /etc/resolv.conf):0.0
export LIBGL_ALWAYS_SOFTWARE=1
```

**Note:**
- The `DISPLAY` variable is set using the nameserver IP from `/etc/resolv.conf`, which works for most WSL2 setups with XLaunch.
- If you use a different X server or have a custom network configuration, adjust the `DISPLAY` variable accordingly (e.g., `export DISPLAY=localhost:0.0`).
- Ensure XLaunch is running before starting OpenFOAM simulations that require graphical output (e.g., Paraview, foamToVTK, etc.).

For more details, see the comments in your shell script and the [WSL documentation](https://docs.microsoft.com/en-us/windows/wsl/tutorials/gui).


## Getting Started

1. **Clone the repository** and set up the directory structure as shown above.
2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Install and configure required software** (SpaceClaim, Fluent, OpenFOAM, Paraview).
4. **Update all relevant paths and parameters** in `src/utils/config.py` and `reference/wsl_openfoam_case/01_cylinder_in_pipe_optimization/paraview_trace_script.py`.
5. Activate XLaunch with display number 0 and disable access control (Windows).
6. **Run the optimization**:
   ```bash
   python src/main.py
   ```

## Input & Output

- **Input**: Design parameter limits (e.g., length, diameter) and corresponding step sizes, specified in `config.py`.
- **Output**: CSV files with design data, Pareto front plots, logs, and simulation results.

## Key Scripts

- `src/main.py`: Orchestrates the optimization workflow.
- `src/utils/config.py`: Central configuration.
- `src/utils/spaceclaim.py`: CAD automation.
- `src/utils/pyfluent_meshing.py`: Meshing automation.
- `src/utils/openfoam.py`: CFD simulation and post-processing.
- `reference/wsl_openfoam_case/01_cylinder_in_pipe_optimization/`: Reference case, shell scripts, Paraview scripts.

## Logging

- Logs for each design are saved in `logs/`.
- Main log file: `logs/log.log`.

## Results & Visualization

- Pareto front and solution plots are saved as PNGs in `result_of_optimization_study/`.
- Final Pareto-optimal designs exported as CSV.

## Example Application: *Cylinder-in-Pipe*

This example optimizes a **3D cylinder placed inside a pipe** by varying its **length** and **diameter**, with the objectives of:
- Minimizing **pressure drop across the cylinder**
- Minimizing **drag force on the cylinder**

(No constraints are applied in this study, but they can be added if required.)  


In the current implementation, OptiFS integrates:  
- **ANSYS SpaceClaim 2025R2** for parametric CAD generation  
- **ANSYS Fluent Meshing 2025R2** for automated mesh creation  
- **OpenFOAM 12** (via WSL/Linux) for CFD simulations  
- **pymoo 0.6.0 (NSGA-II)** for multi-objective optimization 

## Troubleshooting

- Ensure all external software is properly installed and licensed.
- Confirm file formats are compatible between connected software.
- Verify design variable limits are appropriate and non-conflicting.
- Update all paths in `config.py` and relevant scripts.
- Review logs in `logs/` for errors.

## Authors

- Preetham Suresh
- Jaydev Dave

---

For further details, refer to comments in each script and the configuration file.
