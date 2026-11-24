# OptiFS: Optimization Framework with Simulation Software

# Project is migrated to Gitlab at : (https://github.com/jaydev-dave/OptiFS)

## Overview
**OptiFS** is a Python-based framework for automating multi-objective design optimization, integrating a complete **CAD → Meshing → CFD → Post-processing** pipeline. It combines:

- **ANSYS SpaceClaim 2025R2** for parametric CAD generation
- **ANSYS Fluent Meshing 2025R2** for automated mesh creation
- **OpenFOAM 12** (via WSL/Linux) for CFD simulations
- **pymoo 0.6.0 (NSGA-II)** for multi-objective optimization