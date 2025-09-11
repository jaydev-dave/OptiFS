# trace generated using paraview version 5.11.2
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
a01_spark_arrestor_optimization_1000vtk = LegacyVTKReader(registrationName='01_spark_arrestor_optimization_1000.vtk', FileNames=['/home/cfduser/OpenFOAM/cfduser-12/run/01_spark_arrestor_optimization/VTK/01_spark_arrestor_optimization_1000.vtk'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
a01_spark_arrestor_optimization_1000vtkDisplay = Show(a01_spark_arrestor_optimization_1000vtk, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
a01_spark_arrestor_optimization_1000vtkDisplay.Representation = 'Surface'
a01_spark_arrestor_optimization_1000vtkDisplay.ColorArrayName = [None, '']
a01_spark_arrestor_optimization_1000vtkDisplay.SelectTCoordArray = 'None'
a01_spark_arrestor_optimization_1000vtkDisplay.SelectNormalArray = 'None'
a01_spark_arrestor_optimization_1000vtkDisplay.SelectTangentArray = 'None'
a01_spark_arrestor_optimization_1000vtkDisplay.OSPRayScaleArray = 'U'
a01_spark_arrestor_optimization_1000vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
a01_spark_arrestor_optimization_1000vtkDisplay.SelectOrientationVectors = 'None'
a01_spark_arrestor_optimization_1000vtkDisplay.ScaleFactor = 0.40549999475479126
a01_spark_arrestor_optimization_1000vtkDisplay.SelectScaleArray = 'None'
a01_spark_arrestor_optimization_1000vtkDisplay.GlyphType = 'Arrow'
a01_spark_arrestor_optimization_1000vtkDisplay.GlyphTableIndexArray = 'None'
a01_spark_arrestor_optimization_1000vtkDisplay.GaussianRadius = 0.020274999737739562
a01_spark_arrestor_optimization_1000vtkDisplay.SetScaleArray = ['POINTS', 'U']
a01_spark_arrestor_optimization_1000vtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
a01_spark_arrestor_optimization_1000vtkDisplay.OpacityArray = ['POINTS', 'U']
a01_spark_arrestor_optimization_1000vtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
a01_spark_arrestor_optimization_1000vtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
a01_spark_arrestor_optimization_1000vtkDisplay.PolarAxes = 'PolarAxesRepresentation'
a01_spark_arrestor_optimization_1000vtkDisplay.ScalarOpacityUnitDistance = 0.016083816853224464
a01_spark_arrestor_optimization_1000vtkDisplay.OpacityArrayName = ['POINTS', 'U']
a01_spark_arrestor_optimization_1000vtkDisplay.SelectInputVectors = ['POINTS', 'U']
a01_spark_arrestor_optimization_1000vtkDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
a01_spark_arrestor_optimization_1000vtkDisplay.ScaleTransferFunction.Points = [-55.034698486328125, 0.0, 0.5, 0.0, 76.87190246582031, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
a01_spark_arrestor_optimization_1000vtkDisplay.OpacityTransferFunction.Points = [-55.034698486328125, 0.0, 0.5, 0.0, 76.87190246582031, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=a01_spark_arrestor_optimization_1000vtk)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.9725000262260437, 0.0, 5.960464477539063e-08]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [0.9725000262260437, 0.0, 5.960464477539063e-08]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [x, 0.0, 0.0]

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = [None, '']
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.OSPRayScaleArray = 'U'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 0.024990692734718323
slice1Display.SelectScaleArray = 'None'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'None'
slice1Display.GaussianRadius = 0.0012495346367359162
slice1Display.SetScaleArray = ['POINTS', 'U']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'U']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'
slice1Display.SelectInputVectors = ['POINTS', 'U']
slice1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [-7.526168346405029, 0.0, 0.5, 0.0, 35.857398986816406, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [-7.526168346405029, 0.0, 0.5, 0.0, 35.857398986816406, 1.0, 0.5, 0.0]

# hide data in view
Hide(a01_spark_arrestor_optimization_1000vtk, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# rename source object
RenameSource('mid', slice1)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=slice1.SliceType)

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=slice1)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'r'
calculator1.Function = 'sqrt(coordsY^2 + coordsZ^2)'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'r'
rLUT = GetColorTransferFunction('r')

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['POINTS', 'r']
calculator1Display.LookupTable = rLUT
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.OSPRayScaleArray = 'r'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'None'
calculator1Display.ScaleFactor = 0.024990692734718323
calculator1Display.SelectScaleArray = 'r'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'r'
calculator1Display.GaussianRadius = 0.0012495346367359162
calculator1Display.SetScaleArray = ['POINTS', 'r']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'r']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.SelectInputVectors = ['POINTS', 'U']
calculator1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [0.0011078068796695636, 0.0, 0.5, 0.0, 0.12496932657533791, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [0.0011078068796695636, 0.0, 0.5, 0.0, 0.12496932657533791, 1.0, 0.5, 0.0]

# hide data in view
Hide(slice1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'r'
rPWF = GetOpacityTransferFunction('r')

# get 2D transfer function for 'r'
rTF2D = GetTransferFunction2D('r')

# rename source object
RenameSource('r', calculator1)

# create a new 'Calculator'
calculator1_1 = Calculator(registrationName='Calculator1', Input=calculator1)
calculator1_1.Function = ''

# rename source object
RenameSource('U_t', calculator1_1)

# Properties modified on calculator1_1
calculator1_1.ResultArrayName = 'U_t'
calculator1_1.Function = '(coordsY*U_Z - coordsZ*U_Y)/r'

# show data in view
calculator1_1Display = Show(calculator1_1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'U_t'
u_tLUT = GetColorTransferFunction('U_t')

# trace defaults for the display properties.
calculator1_1Display.Representation = 'Surface'
calculator1_1Display.ColorArrayName = ['POINTS', 'U_t']
calculator1_1Display.LookupTable = u_tLUT
calculator1_1Display.SelectTCoordArray = 'None'
calculator1_1Display.SelectNormalArray = 'None'
calculator1_1Display.SelectTangentArray = 'None'
calculator1_1Display.OSPRayScaleArray = 'U_t'
calculator1_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1_1Display.SelectOrientationVectors = 'None'
calculator1_1Display.ScaleFactor = 0.024990692734718323
calculator1_1Display.SelectScaleArray = 'U_t'
calculator1_1Display.GlyphType = 'Arrow'
calculator1_1Display.GlyphTableIndexArray = 'U_t'
calculator1_1Display.GaussianRadius = 0.0012495346367359162
calculator1_1Display.SetScaleArray = ['POINTS', 'U_t']
calculator1_1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1_1Display.OpacityArray = ['POINTS', 'U_t']
calculator1_1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1_1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1_1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1_1Display.SelectInputVectors = ['POINTS', 'U']
calculator1_1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1_1Display.ScaleTransferFunction.Points = [-6.713673651881516, 0.0, 0.5, 0.0, 25.664457417888222, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1_1Display.OpacityTransferFunction.Points = [-6.713673651881516, 0.0, 0.5, 0.0, 25.664457417888222, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
calculator1_1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'U_t'
u_tPWF = GetOpacityTransferFunction('U_t')

# get 2D transfer function for 'U_t'
u_tTF2D = GetTransferFunction2D('U_t')

# create a new 'Calculator'
calculator1_2 = Calculator(registrationName='Calculator1', Input=calculator1_1)
calculator1_2.Function = ''

# rename source object
RenameSource('num', calculator1_2)

# Properties modified on calculator1_2
calculator1_2.ResultArrayName = 'num'
calculator1_2.Function = 'r * U_X * U_t'

# show data in view
calculator1_2Display = Show(calculator1_2, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'num'
numLUT = GetColorTransferFunction('num')

# trace defaults for the display properties.
calculator1_2Display.Representation = 'Surface'
calculator1_2Display.ColorArrayName = ['POINTS', 'num']
calculator1_2Display.LookupTable = numLUT
calculator1_2Display.SelectTCoordArray = 'None'
calculator1_2Display.SelectNormalArray = 'None'
calculator1_2Display.SelectTangentArray = 'None'
calculator1_2Display.OSPRayScaleArray = 'num'
calculator1_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1_2Display.SelectOrientationVectors = 'None'
calculator1_2Display.ScaleFactor = 0.024990692734718323
calculator1_2Display.SelectScaleArray = 'num'
calculator1_2Display.GlyphType = 'Arrow'
calculator1_2Display.GlyphTableIndexArray = 'num'
calculator1_2Display.GaussianRadius = 0.0012495346367359162
calculator1_2Display.SetScaleArray = ['POINTS', 'num']
calculator1_2Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1_2Display.OpacityArray = ['POINTS', 'num']
calculator1_2Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1_2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1_2Display.PolarAxes = 'PolarAxesRepresentation'
calculator1_2Display.SelectInputVectors = ['POINTS', 'U']
calculator1_2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1_2Display.ScaleTransferFunction.Points = [-12.785727484934394, 0.0, 0.5, 0.0, 34.993410650398246, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1_2Display.OpacityTransferFunction.Points = [-12.785727484934394, 0.0, 0.5, 0.0, 34.993410650398246, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1_1, renderView1)

# show color bar/color legend
calculator1_2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
numLUT.RescaleTransferFunction(-12.785727484934394, 34.99341065039825)

# get opacity transfer function/opacity map for 'num'
numPWF = GetOpacityTransferFunction('num')

# Rescale transfer function
numPWF.RescaleTransferFunction(-12.785727484934394, 34.99341065039825)

# get 2D transfer function for 'num'
numTF2D = GetTransferFunction2D('num')

# create a new 'Calculator'
calculator1_3 = Calculator(registrationName='Calculator1', Input=calculator1_2)
calculator1_3.Function = ''

# rename source object
RenameSource('den', calculator1_3)

# Properties modified on calculator1_3
calculator1_3.ResultArrayName = 'den'
calculator1_3.Function = 'U_X^2'

# show data in view
calculator1_3Display = Show(calculator1_3, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'den'
denLUT = GetColorTransferFunction('den')

# trace defaults for the display properties.
calculator1_3Display.Representation = 'Surface'
calculator1_3Display.ColorArrayName = ['POINTS', 'den']
calculator1_3Display.LookupTable = denLUT
calculator1_3Display.SelectTCoordArray = 'None'
calculator1_3Display.SelectNormalArray = 'None'
calculator1_3Display.SelectTangentArray = 'None'
calculator1_3Display.OSPRayScaleArray = 'den'
calculator1_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1_3Display.SelectOrientationVectors = 'None'
calculator1_3Display.ScaleFactor = 0.024990692734718323
calculator1_3Display.SelectScaleArray = 'den'
calculator1_3Display.GlyphType = 'Arrow'
calculator1_3Display.GlyphTableIndexArray = 'den'
calculator1_3Display.GaussianRadius = 0.0012495346367359162
calculator1_3Display.SetScaleArray = ['POINTS', 'den']
calculator1_3Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1_3Display.OpacityArray = ['POINTS', 'den']
calculator1_3Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1_3Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1_3Display.PolarAxes = 'PolarAxesRepresentation'
calculator1_3Display.SelectInputVectors = ['POINTS', 'U']
calculator1_3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1_3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1285.7530620997422, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1_3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1285.7530620997422, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1_2, renderView1)

# show color bar/color legend
calculator1_3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'den'
denPWF = GetOpacityTransferFunction('den')

# get 2D transfer function for 'den'
denTF2D = GetTransferFunction2D('den')

# create a new 'Calculator'
calculator1_4 = Calculator(registrationName='Calculator1', Input=calculator1_3)
calculator1_4.Function = ''

# rename source object
RenameSource('a_c', calculator1_4)

# Properties modified on calculator1_4
calculator1_4.ResultArrayName = 'a_c'


# show data in view
calculator1_4Display = Show(calculator1_4, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
calculator1_4Display.Representation = 'Surface'
calculator1_4Display.ColorArrayName = ['POINTS', 'den']
calculator1_4Display.LookupTable = denLUT
calculator1_4Display.SelectTCoordArray = 'None'
calculator1_4Display.SelectNormalArray = 'None'
calculator1_4Display.SelectTangentArray = 'None'
calculator1_4Display.OSPRayScaleArray = 'den'
calculator1_4Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1_4Display.SelectOrientationVectors = 'None'
calculator1_4Display.ScaleFactor = 0.024990692734718323
calculator1_4Display.SelectScaleArray = 'den'
calculator1_4Display.GlyphType = 'Arrow'
calculator1_4Display.GlyphTableIndexArray = 'den'
calculator1_4Display.GaussianRadius = 0.0012495346367359162
calculator1_4Display.SetScaleArray = ['POINTS', 'den']
calculator1_4Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1_4Display.OpacityArray = ['POINTS', 'den']
calculator1_4Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1_4Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1_4Display.PolarAxes = 'PolarAxesRepresentation'
calculator1_4Display.SelectInputVectors = ['POINTS', 'U']
calculator1_4Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1_4Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1285.7530620997422, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1_4Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1285.7530620997422, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1_3, renderView1)

# show color bar/color legend
calculator1_4Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on calculator1_4
calculator1_4.Function = 'U_t^2/r'

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Point Data to Cell Data'
pointDatatoCellData1 = PointDatatoCellData(registrationName='PointDatatoCellData1', Input=calculator1_4)
pointDatatoCellData1.PointDataArraytoprocess = ['U', 'U_t', 'a_c', 'den', 'k', 'num', 'nut', 'omega', 'p', 'r']

# show data in view
pointDatatoCellData1Display = Show(pointDatatoCellData1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'a_c'
a_cLUT = GetColorTransferFunction('a_c')

# trace defaults for the display properties.
pointDatatoCellData1Display.Representation = 'Surface'
pointDatatoCellData1Display.ColorArrayName = ['CELLS', 'a_c']
pointDatatoCellData1Display.LookupTable = a_cLUT
pointDatatoCellData1Display.SelectTCoordArray = 'None'
pointDatatoCellData1Display.SelectNormalArray = 'None'
pointDatatoCellData1Display.SelectTangentArray = 'None'
pointDatatoCellData1Display.OSPRayScaleFunction = 'PiecewiseFunction'
pointDatatoCellData1Display.SelectOrientationVectors = 'None'
pointDatatoCellData1Display.ScaleFactor = 0.024990692734718323
pointDatatoCellData1Display.SelectScaleArray = 'a_c'
pointDatatoCellData1Display.GlyphType = 'Arrow'
pointDatatoCellData1Display.GlyphTableIndexArray = 'a_c'
pointDatatoCellData1Display.GaussianRadius = 0.0012495346367359162
pointDatatoCellData1Display.SetScaleArray = [None, '']
pointDatatoCellData1Display.ScaleTransferFunction = 'PiecewiseFunction'
pointDatatoCellData1Display.OpacityArray = [None, '']
pointDatatoCellData1Display.OpacityTransferFunction = 'PiecewiseFunction'
pointDatatoCellData1Display.DataAxesGrid = 'GridAxesRepresentation'
pointDatatoCellData1Display.PolarAxes = 'PolarAxesRepresentation'
pointDatatoCellData1Display.SelectInputVectors = [None, '']
pointDatatoCellData1Display.WriteLog = ''

# hide data in view
Hide(calculator1_4, renderView1)

# show color bar/color legend
pointDatatoCellData1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'a_c'
a_cPWF = GetOpacityTransferFunction('a_c')

# get 2D transfer function for 'a_c'
a_cTF2D = GetTransferFunction2D('a_c')

# create a new 'Integrate Variables'
integrateVariables1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=pointDatatoCellData1)

# Properties modified on integrateVariables1
integrateVariables1.DivideCellDataByVolume = 1

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024

# show data in view
integrateVariables1Display = Show(integrateVariables1, spreadSheetView1, 'SpreadSheetRepresentation')

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=0)

# Properties modified on integrateVariables1Display
integrateVariables1Display.Assembly = ''

# update the view to ensure updated data information
spreadSheetView1.Update()

# rename source object
RenameSource('mid-IntVar', integrateVariables1)

# set active source
SetActiveSource(a01_spark_arrestor_optimization_1000vtk)

# create a new 'Slice'
slice1_1 = Slice(registrationName='Slice1', Input=a01_spark_arrestor_optimization_1000vtk)
slice1_1.SliceType = 'Plane'
slice1_1.HyperTreeGridSlicer = 'Plane'
slice1_1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1_1.SliceType.Origin = [0.9725000262260437, 0.0, 5.960464477539063e-08]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1_1.HyperTreeGridSlicer.Origin = [0.9725000262260437, 0.0, 5.960464477539063e-08]

# rename source object
RenameSource('nach', slice1_1)

# Properties modified on slice1_1.SliceType
slice1_1.SliceType.Origin = [2.3, 0.0, 0.0]

# show data in view
slice1_1Display = Show(slice1_1, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# Properties modified on slice1_1Display
slice1_1Display.Assembly = ''

# create a new 'Integrate Variables'
integrateVariables1_1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=slice1_1)

# rename source object
RenameSource('nach-IntVar', integrateVariables1_1)

# Properties modified on integrateVariables1_1
integrateVariables1_1.DivideCellDataByVolume = 1

# show data in view
integrateVariables1_1Display = Show(integrateVariables1_1, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# Properties modified on integrateVariables1_1Display
integrateVariables1_1Display.Assembly = ''

# set active source
SetActiveSource(a01_spark_arrestor_optimization_1000vtk)

# create a new 'Slice'
slice1_2 = Slice(registrationName='Slice1', Input=a01_spark_arrestor_optimization_1000vtk)
slice1_2.SliceType = 'Plane'
slice1_2.HyperTreeGridSlicer = 'Plane'
slice1_2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1_2.SliceType.Origin = [0.9725000262260437, 0.0, 5.960464477539063e-08]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1_2.HyperTreeGridSlicer.Origin = [0.9725000262260437, 0.0, 5.960464477539063e-08]

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=slice1_2.SliceType)

# Properties modified on slice1_2.SliceType
slice1_2.SliceType.Origin = [-0.5, 0.0, 0.0]

# show data in view
slice1_2Display = Show(slice1_2, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# Properties modified on slice1_2Display
slice1_2Display.Assembly = ''

# rename source object
RenameSource('vor', slice1_2)

# create a new 'Integrate Variables'
integrateVariables1_2 = IntegrateVariables(registrationName='IntegrateVariables1', Input=slice1_2)

# rename source object
RenameSource('vor-IntVar', integrateVariables1_2)

# set active source
SetActiveSource(integrateVariables1_1)

# set active source
SetActiveSource(integrateVariables1)

# set active source
SetActiveSource(integrateVariables1_2)

# Properties modified on integrateVariables1_2
integrateVariables1_2.DivideCellDataByVolume = 1

# show data in view
integrateVariables1_2Display = Show(integrateVariables1_2, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# Properties modified on integrateVariables1_2Display
integrateVariables1_2Display.Assembly = ''

# set active source
SetActiveSource(integrateVariables1_1)

# set active source
SetActiveSource(integrateVariables1)

# create a new 'Group Datasets'
groupDatasets1 = GroupDatasets(registrationName='GroupDatasets1', Input=[integrateVariables1_2, integrateVariables1_1, integrateVariables1])
groupDatasets1.BlockNames = ['vor-IntVar', 'nach-IntVar', 'mid-IntVar']

# show data in view
groupDatasets1Display = Show(groupDatasets1, spreadSheetView1, 'SpreadSheetRepresentation')

# hide data in view
Hide(integrateVariables1, spreadSheetView1)

# hide data in view
Hide(integrateVariables1_1, spreadSheetView1)

# hide data in view
Hide(integrateVariables1_2, spreadSheetView1)

# update the view to ensure updated data information
spreadSheetView1.Update()

# resize frame
layout1.SetSplitFraction(0, 0.3728581220013708)

# Properties modified on spreadSheetView1
spreadSheetView1.FieldAssociation = 'Cell Data'

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Cell ID']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Area']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Cell ID']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Cell Type']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Cell Type', 'cellID']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Cell Type', 'cellID', 'k']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Cell Type', 'cellID', 'k', 'nut']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Cell Type', 'cellID', 'k', 'nut', 'omega']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Cell Type', 'cellID', 'k', 'nut', 'omega', 'r']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Cell Type', 'cellID', 'k', 'nut', 'omega', 'r', 'U']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Cell Type', 'cellID', 'k', 'nut', 'omega', 'r', 'U', 'U_Magnitude']

# set active source
SetActiveSource(groupDatasets1)

# set active source
SetActiveSource(slice1_2)

# set active source
SetActiveSource(groupDatasets1)

# export view
ExportView('/home/cfduser/OpenFOAM/cfduser-12/run/01_spark_arrestor_optimization/data.csv', view=spreadSheetView1)

# destroy spreadSheetView1
Delete(spreadSheetView1)
del spreadSheetView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(a01_spark_arrestor_optimization_1000vtk)

# set active source
SetActiveSource(a01_spark_arrestor_optimization_1000vtk)

# show data in view
a01_spark_arrestor_optimization_1000vtkDisplay = Show(a01_spark_arrestor_optimization_1000vtk, renderView1, 'UnstructuredGridRepresentation')

# hide data in view
Hide(pointDatatoCellData1, renderView1)

renderView1.ResetActiveCameraToNegativeZ()

# reset view to fit data
renderView1.ResetCamera(False)

# Properties modified on a01_spark_arrestor_optimization_1000vtkDisplay
a01_spark_arrestor_optimization_1000vtkDisplay.Opacity = 0.6

# Properties modified on slice1_2.SliceType
slice1_2.SliceType.Origin = [-0.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera(True)

# layout/tab size in pixels
layout1.SetSize(1453, 790)

# current camera placement for renderView1
renderView1.CameraPosition = [0.7724999785423279, -1.6577541828155518e-06, 7.093876580938723]
renderView1.CameraFocalPoint = [0.7724999785423279, -1.6577541828155518e-06, 2.0153820514678955e-06]
renderView1.CameraViewAngle = 17.733425097499428
renderView1.CameraParallelScale = 1.836029841134437

# save screenshot
SaveScreenshot('/home/cfduser/OpenFOAM/cfduser-12/run/01_spark_arrestor_optimization/CAD.png', renderView1, ImageResolution=[1920, 1080],
    OverrideColorPalette='WhiteBackground')

# create a new 'Slice'
slice1_3 = Slice(registrationName='Slice1', Input=a01_spark_arrestor_optimization_1000vtk)
slice1_3.SliceType = 'Plane'
slice1_3.HyperTreeGridSlicer = 'Plane'
slice1_3.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1_3.SliceType.Origin = [0.9725000262260437, 0.0, 5.960464477539063e-08]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1_3.HyperTreeGridSlicer.Origin = [0.9725000262260437, 0.0, 5.960464477539063e-08]

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=slice1_3.SliceType)

# Properties modified on slice1_3.SliceType
slice1_3.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice1_3Display = Show(slice1_3, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1_3Display.Representation = 'Surface'
slice1_3Display.ColorArrayName = [None, '']
slice1_3Display.SelectTCoordArray = 'None'
slice1_3Display.SelectNormalArray = 'None'
slice1_3Display.SelectTangentArray = 'None'
slice1_3Display.OSPRayScaleArray = 'U'
slice1_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1_3Display.SelectOrientationVectors = 'None'
slice1_3Display.ScaleFactor = 0.3654999852180481
slice1_3Display.SelectScaleArray = 'None'
slice1_3Display.GlyphType = 'Arrow'
slice1_3Display.GlyphTableIndexArray = 'None'
slice1_3Display.GaussianRadius = 0.018274999260902404
slice1_3Display.SetScaleArray = ['POINTS', 'U']
slice1_3Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1_3Display.OpacityArray = ['POINTS', 'U']
slice1_3Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1_3Display.DataAxesGrid = 'GridAxesRepresentation'
slice1_3Display.PolarAxes = 'PolarAxesRepresentation'
slice1_3Display.SelectInputVectors = ['POINTS', 'U']
slice1_3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1_3Display.ScaleTransferFunction.Points = [-34.578956604003906, 0.0, 0.5, 0.0, 54.84508514404297, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1_3Display.OpacityTransferFunction.Points = [-34.578956604003906, 0.0, 0.5, 0.0, 54.84508514404297, 1.0, 0.5, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(a01_spark_arrestor_optimization_1000vtk, renderView1)

# set scalar coloring
ColorBy(slice1_3Display, ('POINTS', 'U', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
slice1_3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1_3Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')

# get 2D transfer function for 'U'
uTF2D = GetTransferFunction2D('U')

# layout/tab size in pixels
layout1.SetSize(1453, 790)

# current camera placement for renderView1
renderView1.CameraPosition = [0.7724999785423279, -1.6577541828155518e-06, 7.093876580938723]
renderView1.CameraFocalPoint = [0.7724999785423279, -1.6577541828155518e-06, 2.0153820514678955e-06]
renderView1.CameraViewAngle = 17.733425097499428
renderView1.CameraParallelScale = 1.836029841134437

# save screenshot
SaveScreenshot('/home/cfduser/OpenFOAM/cfduser-12/run/01_spark_arrestor_optimization/U.png', renderView1, ImageResolution=[1453, 790],
    OverrideColorPalette='WhiteBackground')

# set scalar coloring
ColorBy(slice1_3Display, ('POINTS', 'p'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(uLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice1_3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1_3Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# get 2D transfer function for 'p'
pTF2D = GetTransferFunction2D('p')

# layout/tab size in pixels
layout1.SetSize(1453, 790)

# current camera placement for renderView1
renderView1.CameraPosition = [0.7724999785423279, -1.6577541828155518e-06, 7.093876580938723]
renderView1.CameraFocalPoint = [0.7724999785423279, -1.6577541828155518e-06, 2.0153820514678955e-06]
renderView1.CameraViewAngle = 17.733425097499428
renderView1.CameraParallelScale = 1.836029841134437

# save screenshot
SaveScreenshot('/home/cfduser/OpenFOAM/cfduser-12/run/01_spark_arrestor_optimization/p.png', renderView1, ImageResolution=[1453, 790], OverrideColorPalette='WhiteBackground')

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=slice1_3,
    SeedType='Line')
streamTracer1.Vectors = ['POINTS', 'U']
streamTracer1.MaximumStreamlineLength = 3.654999852180481

# init the 'Line' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-1.0549999475479126, -0.12499972432851791, 5.960464477539063e-08]
streamTracer1.SeedType.Point2 = [2.5999999046325684, 0.12499912083148956, 5.960464477539063e-08]

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=streamTracer1.SeedType)

renderView1.ResetActiveCameraToNegativeZ()

# reset view to fit data
renderView1.ResetCamera(False)

# reset view to fit data
renderView1.ResetCamera(True)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=streamTracer1.SeedType)

# Properties modified on streamTracer1
streamTracer1.SeedType = 'Point Cloud'

# show data in view
streamTracer1Display = Show(streamTracer1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
streamTracer1Display.Representation = 'Surface'
streamTracer1Display.ColorArrayName = [None, '']
streamTracer1Display.SelectTCoordArray = 'None'
streamTracer1Display.SelectNormalArray = 'None'
streamTracer1Display.SelectTangentArray = 'None'
streamTracer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer1Display.SelectOrientationVectors = 'None'
streamTracer1Display.ScaleFactor = -2.0000000000000002e+298
streamTracer1Display.SelectScaleArray = 'None'
streamTracer1Display.GlyphType = 'Arrow'
streamTracer1Display.GlyphTableIndexArray = 'None'
streamTracer1Display.GaussianRadius = -1e+297
streamTracer1Display.SetScaleArray = [None, '']
streamTracer1Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer1Display.OpacityArray = [None, '']
streamTracer1Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer1Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer1Display.PolarAxes = 'PolarAxesRepresentation'
streamTracer1Display.SelectInputVectors = [None, '']
streamTracer1Display.WriteLog = ''

# hide data in view
Hide(slice1_3, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(slice1_3)

# hide data in view
Hide(streamTracer1, renderView1)

# show data in view
slice1_3Display = Show(slice1_3, renderView1, 'GeometryRepresentation')

# show color bar/color legend
slice1_3Display.SetScalarBarVisibility(renderView1, True)

# destroy streamTracer1
Delete(streamTracer1)
del streamTracer1

# set active source
SetActiveSource(a01_spark_arrestor_optimization_1000vtk)

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=a01_spark_arrestor_optimization_1000vtk,
    SeedType='Line')
streamTracer1.Vectors = ['POINTS', 'U']
streamTracer1.MaximumStreamlineLength = 4.054999947547913

# init the 'Line' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-1.0549999475479126, -0.25, -0.24999986588954926]
streamTracer1.SeedType.Point2 = [3.0, 0.25, 0.2499999850988388]

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=streamTracer1.SeedType)

# Properties modified on streamTracer1
streamTracer1.SeedType = 'Point Cloud'

# show data in view
streamTracer1Display = Show(streamTracer1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
streamTracer1Display.Representation = 'Surface'
streamTracer1Display.ColorArrayName = [None, '']
streamTracer1Display.SelectTCoordArray = 'None'
streamTracer1Display.SelectNormalArray = 'None'
streamTracer1Display.SelectTangentArray = 'None'
streamTracer1Display.OSPRayScaleArray = 'AngularVelocity'
streamTracer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer1Display.SelectOrientationVectors = 'Normals'
streamTracer1Display.ScaleFactor = 0.36545786857604984
streamTracer1Display.SelectScaleArray = 'AngularVelocity'
streamTracer1Display.GlyphType = 'Arrow'
streamTracer1Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer1Display.GaussianRadius = 0.018272893428802492
streamTracer1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer1Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer1Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer1Display.PolarAxes = 'PolarAxesRepresentation'
streamTracer1Display.SelectInputVectors = ['POINTS', 'Normals']
streamTracer1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer1Display.ScaleTransferFunction.Points = [-18937.987715561238, 0.0, 0.5, 0.0, 35566.73108924, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer1Display.OpacityTransferFunction.Points = [-18937.987715561238, 0.0, 0.5, 0.0, 35566.73108924, 1.0, 0.5, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Tube'
tube1 = Tube(registrationName='Tube1', Input=streamTracer1)
tube1.Scalars = ['POINTS', 'AngularVelocity']
tube1.Vectors = ['POINTS', 'Normals']
tube1.Radius = 0.036545786857604984

# Properties modified on tube1
tube1.Radius = 0.0025

# show data in view
tube1Display = Show(tube1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = [None, '']
tube1Display.SelectTCoordArray = 'None'
tube1Display.SelectNormalArray = 'TubeNormals'
tube1Display.SelectTangentArray = 'None'
tube1Display.OSPRayScaleArray = 'AngularVelocity'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'Normals'
tube1Display.ScaleFactor = 0.3655066847801209
tube1Display.SelectScaleArray = 'AngularVelocity'
tube1Display.GlyphType = 'Arrow'
tube1Display.GlyphTableIndexArray = 'AngularVelocity'
tube1Display.GaussianRadius = 0.01827533423900604
tube1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display.OpacityArray = ['POINTS', 'AngularVelocity']
tube1Display.OpacityTransferFunction = 'PiecewiseFunction'
tube1Display.DataAxesGrid = 'GridAxesRepresentation'
tube1Display.PolarAxes = 'PolarAxesRepresentation'
tube1Display.SelectInputVectors = ['POINTS', 'Normals']
tube1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube1Display.ScaleTransferFunction.Points = [-18937.987715561238, 0.0, 0.5, 0.0, 35566.73108924, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube1Display.OpacityTransferFunction.Points = [-18937.987715561238, 0.0, 0.5, 0.0, 35566.73108924, 1.0, 0.5, 0.0]

# hide data in view
Hide(streamTracer1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(slice1_3, renderView1)

# set active source
SetActiveSource(slice1_2)

# show data in view
slice1_2Display = Show(slice1_2, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1_2Display.Representation = 'Surface'
slice1_2Display.ColorArrayName = [None, '']
slice1_2Display.SelectTCoordArray = 'None'
slice1_2Display.SelectNormalArray = 'None'
slice1_2Display.SelectTangentArray = 'None'
slice1_2Display.OSPRayScaleArray = 'U'
slice1_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1_2Display.SelectOrientationVectors = 'None'
slice1_2Display.ScaleFactor = 0.024587538838386536
slice1_2Display.SelectScaleArray = 'None'
slice1_2Display.GlyphType = 'Arrow'
slice1_2Display.GlyphTableIndexArray = 'None'
slice1_2Display.GaussianRadius = 0.0012293769419193267
slice1_2Display.SetScaleArray = ['POINTS', 'U']
slice1_2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1_2Display.OpacityArray = ['POINTS', 'U']
slice1_2Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1_2Display.DataAxesGrid = 'GridAxesRepresentation'
slice1_2Display.PolarAxes = 'PolarAxesRepresentation'
slice1_2Display.SelectInputVectors = ['POINTS', 'U']
slice1_2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1_2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 17.995460510253906, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1_2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 17.995460510253906, 1.0, 0.5, 0.0]

# set active source
SetActiveSource(slice1_1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=slice1_1.SliceType)

# show data in view
slice1_1Display = Show(slice1_1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1_1Display.Representation = 'Surface'
slice1_1Display.ColorArrayName = [None, '']
slice1_1Display.SelectTCoordArray = 'None'
slice1_1Display.SelectNormalArray = 'None'
slice1_1Display.SelectTangentArray = 'None'
slice1_1Display.OSPRayScaleArray = 'U'
slice1_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1_1Display.SelectOrientationVectors = 'None'
slice1_1Display.ScaleFactor = 0.024887690693140032
slice1_1Display.SelectScaleArray = 'None'
slice1_1Display.GlyphType = 'Arrow'
slice1_1Display.GlyphTableIndexArray = 'None'
slice1_1Display.GaussianRadius = 0.0012443845346570015
slice1_1Display.SetScaleArray = ['POINTS', 'U']
slice1_1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1_1Display.OpacityArray = ['POINTS', 'U']
slice1_1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1_1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1_1Display.PolarAxes = 'PolarAxesRepresentation'
slice1_1Display.SelectInputVectors = ['POINTS', 'U']
slice1_1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1_1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 20.668962478637695, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1_1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 20.668962478637695, 1.0, 0.5, 0.0]

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=slice1_1.SliceType)

# set active source
SetActiveSource(slice1)

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# set active source
SetActiveSource(a01_spark_arrestor_optimization_1000vtk)

# show data in view
a01_spark_arrestor_optimization_1000vtkDisplay = Show(a01_spark_arrestor_optimization_1000vtk, renderView1, 'UnstructuredGridRepresentation')

# Properties modified on a01_spark_arrestor_optimization_1000vtkDisplay
a01_spark_arrestor_optimization_1000vtkDisplay.Opacity = 0.4

# set active source
SetActiveSource(tube1)

# set scalar coloring
ColorBy(tube1Display, ('POINTS', 'U', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
tube1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tube1Display.SetScalarBarVisibility(renderView1, True)

# Rescale transfer function
uLUT.RescaleTransferFunction(0.0, 58.43639609265706)

# Rescale transfer function
uPWF.RescaleTransferFunction(0.0, 58.43639609265706)

# set active source
SetActiveSource(slice1_2)

# set active source
SetActiveSource(slice1_1)

# set active source
SetActiveSource(slice1)

# set active source
SetActiveSource(tube1)

# set scalar coloring
ColorBy(tube1Display, ('POINTS', 'p'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(uLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
tube1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tube1Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(tube1Display, ('POINTS', 'U', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
tube1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tube1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(streamTracer1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=streamTracer1.SeedType)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(tube1)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=streamTracer1.SeedType)

# set active source
SetActiveSource(streamTracer1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=streamTracer1.SeedType)

# hide data in view
Hide(tube1, renderView1)

# show data in view
streamTracer1Display = Show(streamTracer1, renderView1, 'GeometryRepresentation')

# destroy tube1
Delete(tube1)
del tube1

# set active source
SetActiveSource(a01_spark_arrestor_optimization_1000vtk)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=streamTracer1.SeedType)

# hide data in view
Hide(streamTracer1, renderView1)

# show data in view
a01_spark_arrestor_optimization_1000vtkDisplay = Show(a01_spark_arrestor_optimization_1000vtk, renderView1, 'UnstructuredGridRepresentation')

# destroy streamTracer1
Delete(streamTracer1)
del streamTracer1

# set active source
SetActiveSource(slice1_3)

# set active source
SetActiveSource(groupDatasets1)

# set active source
SetActiveSource(slice1_3)

# destroy groupDatasets1
Delete(groupDatasets1)
del groupDatasets1

# set active source
SetActiveSource(a01_spark_arrestor_optimization_1000vtk)

# destroy slice1_3
Delete(slice1_3)
del slice1_3

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=a01_spark_arrestor_optimization_1000vtk,
    SeedType='Line')
streamTracer1.Vectors = ['POINTS', 'U']
streamTracer1.MaximumStreamlineLength = 4.054999947547913

# init the 'Line' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-1.0549999475479126, -0.25, -0.24999986588954926]
streamTracer1.SeedType.Point2 = [3.0, 0.25, 0.2499999850988388]

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=streamTracer1.SeedType)

# Properties modified on streamTracer1
streamTracer1.SeedType = 'Point Cloud'

# show data in view
streamTracer1Display = Show(streamTracer1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
streamTracer1Display.Representation = 'Surface'
streamTracer1Display.ColorArrayName = [None, '']
streamTracer1Display.SelectTCoordArray = 'None'
streamTracer1Display.SelectNormalArray = 'None'
streamTracer1Display.SelectTangentArray = 'None'
streamTracer1Display.OSPRayScaleArray = 'AngularVelocity'
streamTracer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer1Display.SelectOrientationVectors = 'Normals'
streamTracer1Display.ScaleFactor = 0.36545327901840213
streamTracer1Display.SelectScaleArray = 'AngularVelocity'
streamTracer1Display.GlyphType = 'Arrow'
streamTracer1Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer1Display.GaussianRadius = 0.018272663950920105
streamTracer1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer1Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer1Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer1Display.PolarAxes = 'PolarAxesRepresentation'
streamTracer1Display.SelectInputVectors = ['POINTS', 'Normals']
streamTracer1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer1Display.ScaleTransferFunction.Points = [-37999.79272602985, 0.0, 0.5, 0.0, 45881.91552655851, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer1Display.OpacityTransferFunction.Points = [-37999.79272602985, 0.0, 0.5, 0.0, 45881.91552655851, 1.0, 0.5, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Tube'
tube1 = Tube(registrationName='Tube1', Input=streamTracer1)
tube1.Scalars = ['POINTS', 'AngularVelocity']
tube1.Vectors = ['POINTS', 'Normals']
tube1.Radius = 0.03654532790184021

# Properties modified on tube1
tube1.Radius = 0.0025

# show data in view
tube1Display = Show(tube1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = [None, '']
tube1Display.SelectTCoordArray = 'None'
tube1Display.SelectNormalArray = 'TubeNormals'
tube1Display.SelectTangentArray = 'None'
tube1Display.OSPRayScaleArray = 'AngularVelocity'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'Normals'
tube1Display.ScaleFactor = 0.3655160069465637
tube1Display.SelectScaleArray = 'AngularVelocity'
tube1Display.GlyphType = 'Arrow'
tube1Display.GlyphTableIndexArray = 'AngularVelocity'
tube1Display.GaussianRadius = 0.018275800347328185
tube1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display.OpacityArray = ['POINTS', 'AngularVelocity']
tube1Display.OpacityTransferFunction = 'PiecewiseFunction'
tube1Display.DataAxesGrid = 'GridAxesRepresentation'
tube1Display.PolarAxes = 'PolarAxesRepresentation'
tube1Display.SelectInputVectors = ['POINTS', 'Normals']
tube1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube1Display.ScaleTransferFunction.Points = [-37999.79272602985, 0.0, 0.5, 0.0, 45881.91552655851, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube1Display.OpacityTransferFunction.Points = [-37999.79272602985, 0.0, 0.5, 0.0, 45881.91552655851, 1.0, 0.5, 0.0]

# hide data in view
Hide(streamTracer1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(tube1Display, ('POINTS', 'U', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
tube1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tube1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(slice1_2, renderView1)

# set active source
SetActiveSource(slice1_2)

# show data in view
slice1_2Display = Show(slice1_2, renderView1, 'GeometryRepresentation')

# hide data in view
Hide(slice1_1, renderView1)

# set active source
SetActiveSource(slice1_1)

# show data in view
slice1_1Display = Show(slice1_1, renderView1, 'GeometryRepresentation')

# hide data in view
Hide(slice1, renderView1)

# set active source
SetActiveSource(slice1)

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# reset view to fit data
renderView1.ResetCamera(True)

# layout/tab size in pixels
layout1.SetSize(1453, 790)

# current camera placement for renderView1
renderView1.CameraPosition = [0.7727397084236145, 0.0004878789186477661, 7.095518693412788]
renderView1.CameraFocalPoint = [0.7727397084236145, 0.0004878789186477661, -4.319101572036743e-05]
renderView1.CameraViewAngle = 17.733425097499428
renderView1.CameraParallelScale = 1.8364665513936291

# save screenshot
SaveScreenshot('/home/cfduser/OpenFOAM/cfduser-12/run/01_spark_arrestor_optimization/Streamlines.png', renderView1, ImageResolution=[1453, 790], OverrideColorPalette='WhiteBackground')

# set active source
SetActiveSource(integrateVariables1_2)

# set active source
SetActiveSource(streamTracer1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=streamTracer1.SeedType)

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
uLUT.RescaleTransferFunction(0.0, 59.761912020899466)

# Rescale transfer function
uPWF.RescaleTransferFunction(0.0, 59.761912020899466)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1453, 790)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.7727397084236145, 0.0004878789186477661, 7.095518693412788]
renderView1.CameraFocalPoint = [0.7727397084236145, 0.0004878789186477661, -4.319101572036743e-05]
renderView1.CameraViewAngle = 17.733425097499428
renderView1.CameraParallelScale = 1.8364665513936291

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).