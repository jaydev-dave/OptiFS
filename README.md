# OptiFS: Optimization Framework with Simulation Software


## Overview
**OptiFS** is a Python-based framework for automating multi-objective design optimization, integrating a complete **CAD → Meshing → CFD → Post-processing** pipeline. It combines:

- **ANSYS SpaceClaim** for parametric CAD generation
- **ANSYS Fluent Meshing** for automated mesh creation
- **OpenFOAM** (via WSL/Linux) for CFD simulations
- **pymoo (NSGA-II)** for multi-objective optimization

OptiFS is designed to be extensible. If your preferred CAD or simulation software provides a Python interface, you can easily adapt the framework to use alternatives such as StarCCM+, ANSYS Fluent, or other tools. The workflow is applicable to a wide range of simulation domains, including structural mechanics, acoustics, and electromagnetics, making OptiFS suitable for diverse engineering optimization tasks.

### Example Application: *Cylinder-in-Pipe*  
This setup optimizes a **3D cylinder placed inside a pipe** by varying its **length** and **diameter**, with the objectives of:  
- Minimizing **pressure drop across the cylinder**  
- Minimizing **drag force on the cylinder**  

(No constraints are applied in this study, but they can be added if required.)  

## Features
- **Parametric Design Optimization**: Vary cylinder length and diameter.
- **Automated CAD Generation**: Uses SpaceClaim via Python scripting.
- **Automated Meshing**: Uses ANSYS Fluent Meshing workflow.
- **CFD Simulation**: Runs OpenFOAM cases in WSL.
- **Post-Processing**: Extracts results and generates Pareto front plots.
- **Logging**: Detailed logs for each design and overall process.

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

## Workflow
1. **Setup**: Configure all paths and parameters in `src/utils/config.py`.
2. **Run Optimization**: Execute `src/main.py` to start the optimization loop.
   - For each design:
     - Generate CAD (SpaceClaim)
     - Mesh geometry (Fluent)
     - Run CFD simulation (OpenFOAM)
     - Extract objectives (pressure drop, drag)
     - Log results
3. **Results**: Pareto-optimal designs and plots are saved in `result_of_optimization_study/`.

## Requirements
- Python 3.8+
- [pymoo](https://pymoo.org/)
- [ANSYS SpaceClaim](https://www.ansys.com/products/modeling/spaceclaim)
- [ANSYS Fluent](https://www.ansys.com/products/fluids/ansys-fluent)
- [OpenFOAM](https://openfoam.org/) (WSL recommended for Windows)
- [Paraview](https://www.paraview.org/) (for post-processing)
- Other Python packages: numpy, pandas, matplotlib, autograd
- Python modules: `ansys.geometry.core`, `ansys.fluent.core`

## Installation
1. Clone the repository and set up the directory structure as above.
2. Install Python dependencies:
  ```bash
  pip install numpy pandas matplotlib autograd pymoo
  ```
3. Ensure SpaceClaim, Fluent, OpenFOAM, and Paraview are installed and accessible.
4. Install required Python modules for ANSYS integration:
  ```bash
  pip install ansys-geometry-core ansys-fluent-core
  ```
5. Update all relevant paths in `src/utils/config.py` and in `reference/wsl_openfoam_case/01_cylinder_in_pipe_optimization/paraview_trace_script.py` to match your system.


## WSL Display Setup for OpenFOAM (Windows 10 & XLaunch)
If you are running OpenFOAM in WSL on Windows 10 and using XLaunch (or another X server) for graphical display, you may need to modify the display environment variables in your shell scripts. For example, in `reference/wsl_openfoam_case/01_cylinder_in_pipe_optimization/shell_script.sh`:

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

## Usage
Run the main optimization script:
```bash
python src/main.py
```

## Input & Output
- **Input**: Design parameters (length, diameter) defined in `config.py`.
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
- Pareto front and all solutions plots are saved as PNGs in `result_of_optimization_study/`.
- Final Pareto-optimal designs exported as CSV.

## Troubleshooting
- Ensure all external software (SpaceClaim, Fluent, OpenFOAM) are properly installed and licensed.
- Check and update all paths in `config.py` and relevant scripts.
- Review logs in `logs/` for errors.


## Authors
- Preetham Suresh
- Jaydev Dave

---
For more details, see comments in each script and the configuration file.

