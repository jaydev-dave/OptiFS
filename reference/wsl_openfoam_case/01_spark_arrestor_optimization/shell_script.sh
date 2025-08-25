# #!/bin/bash
. /opt/openfoam12/etc/bashrc
# export DISPLAY=$(grep -oP "(?<=nameserver )[0-9\.]+" /etc/resolv.conf):0.0
# export LIBGL_ALWAYS_SOFTWARE=1
export DISPLAY=127.0.0.1:0.0
export LIBGL_ALWAYS_SOFTWARE=1
export OMPI_MCA_btl_vader_single_copy_mechanism=none



# Navigate to the OpenFOAM run directory
cd $FOAM_RUN/01_spark_arrestor_optimization

chmod +x Allclean
./Allclean
rm data.csv
rm CAD.png p.png U.png Streamlines.png

# Convert Fluent mesh to OpenFOAM format
fluent3DMeshToFoam SA_mesh.msh
checkMesh 

# Run OpenFOAM simulation
decomposePar

mpirun --oversubscribe -np 14 foamRun -solver incompressibleFluid -parallel


echo "Simulation completed successfully."

reconstructPar

# Convert the foam files into VTK format for post-processing
foamToVTK -time 1000

# Run the Python Trace script to extract the .csv file
echo "Paraview Script running . . ."
pvbatch paraview_trace_script.py
echo "Done"

rm SA_mesh.msh

echo "Exiting Shell Script"




