# #!/bin/bash
. /opt/openfoam12/etc/bashrc
# export DISPLAY=$(grep -oP "(?<=nameserver )[0-9\.]+" /etc/resolv.conf):0.0
# export LIBGL_ALWAYS_SOFTWARE=1

#!/bin/bash
#. /opt/openfoam12/etc/bashrc
#export DISPLAY=:0
#export LIBGL_ALWAYS_SOFTWARE=1
export DISPLAY=127.0.0.1:0.0
export LIBGL_ALWAYS_SOFTWARE=1
export OMPI_MCA_btl_vader_single_copy_mechanism=none


# Navigate to the OpenFOAM run directory
cd __ADD_FOAM_PATH__
# Example:
# cd /mnt/f/Projects/CFD_Optimization/reference/wsl_openfoam_case/foam_case_run

chmod +x Allclean
./Allclean
rm data.csv
rm LIC.png U.png 

# Convert Fluent mesh to OpenFOAM format
fluent3DMeshToFoam mesh.msh
checkMesh 

# Run OpenFOAM simulation
decomposePar
mpirun --oversubscribe -np 3 foamRun -solver incompressibleFluid -parallel

echo "Simulation completed successfully."

reconstructPar

touch optimization.foam

# Run the Python Trace script to extract the .csv file
echo "Paraview Script running . . ."
pvbatch paraview_trace_script.py
echo "Done"

rm mesh.msh

echo "Exiting Shell Script"




