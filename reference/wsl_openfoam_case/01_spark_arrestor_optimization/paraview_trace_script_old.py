# trace generated using paraview version 5.11.2
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
a01_spark_arrestor_optimization_800vtk = LegacyVTKReader(registrationName='01_spark_arrestor_optimization_1000.vtk', FileNames=['/home/cfduser/OpenFOAM/cfduser-12/run/01_spark_arrestor_optimization/VTK/01_spark_arrestor_optimization_1000.vtk'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
a01_spark_arrestor_optimization_800vtkDisplay = Show(a01_spark_arrestor_optimization_800vtk, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
a01_spark_arrestor_optimization_800vtkDisplay.Representation = 'Surface'
a01_spark_arrestor_optimization_800vtkDisplay.ColorArrayName = [None, '']
a01_spark_arrestor_optimization_800vtkDisplay.SelectTCoordArray = 'None'
a01_spark_arrestor_optimization_800vtkDisplay.SelectNormalArray = 'None'
a01_spark_arrestor_optimization_800vtkDisplay.SelectTangentArray = 'None'
a01_spark_arrestor_optimization_800vtkDisplay.OSPRayScaleArray = 'U'
a01_spark_arrestor_optimization_800vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
a01_spark_arrestor_optimization_800vtkDisplay.SelectOrientationVectors = 'None'
a01_spark_arrestor_optimization_800vtkDisplay.ScaleFactor = 0.3967499971389771
a01_spark_arrestor_optimization_800vtkDisplay.SelectScaleArray = 'None'
a01_spark_arrestor_optimization_800vtkDisplay.GlyphType = 'Arrow'
a01_spark_arrestor_optimization_800vtkDisplay.GlyphTableIndexArray = 'None'
a01_spark_arrestor_optimization_800vtkDisplay.GaussianRadius = 0.019837499856948854
a01_spark_arrestor_optimization_800vtkDisplay.SetScaleArray = ['POINTS', 'U']
a01_spark_arrestor_optimization_800vtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
a01_spark_arrestor_optimization_800vtkDisplay.OpacityArray = ['POINTS', 'U']
a01_spark_arrestor_optimization_800vtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
a01_spark_arrestor_optimization_800vtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
a01_spark_arrestor_optimization_800vtkDisplay.PolarAxes = 'PolarAxesRepresentation'
a01_spark_arrestor_optimization_800vtkDisplay.ScalarOpacityUnitDistance = 0.014089459783280177
a01_spark_arrestor_optimization_800vtkDisplay.OpacityArrayName = ['POINTS', 'U']
a01_spark_arrestor_optimization_800vtkDisplay.SelectInputVectors = ['POINTS', 'U']
a01_spark_arrestor_optimization_800vtkDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
a01_spark_arrestor_optimization_800vtkDisplay.ScaleTransferFunction.Points = [-28.488000869750977, 0.0, 0.5, 0.0, 57.575199127197266, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
a01_spark_arrestor_optimization_800vtkDisplay.OpacityTransferFunction.Points = [-28.488000869750977, 0.0, 0.5, 0.0, 57.575199127197266, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=a01_spark_arrestor_optimization_800vtk)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.9187499284744263, 0.0, 2.2351741790771484e-08]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [0.9187499284744263, 0.0, 2.2351741790771484e-08]

RenameProxy(slice1, 'sources', 'mid')

# rename source object
RenameSource('mid', slice1)

# create a new 'Hierarchical Fractal'
hierarchicalFractal1 = HierarchicalFractal(registrationName='HierarchicalFractal1')

# destroy hierarchicalFractal1
Delete(hierarchicalFractal1)
del hierarchicalFractal1

# set active source
SetActiveSource(slice1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=slice1.SliceType)

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
slice1Display.ScaleFactor = 0.024989800900220873
slice1Display.SelectScaleArray = 'None'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'None'
slice1Display.GaussianRadius = 0.0012494900450110435
slice1Display.SetScaleArray = ['POINTS', 'U']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'U']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'
slice1Display.SelectInputVectors = ['POINTS', 'U']
slice1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [-1.0746620893478394, 0.0, 0.5, 0.0, 33.84053039550781, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [-1.0746620893478394, 0.0, 0.5, 0.0, 33.84053039550781, 1.0, 0.5, 0.0]

# hide data in view
Hide(a01_spark_arrestor_optimization_800vtk, renderView1)

# update the view to ensure updated data information
renderView1.Update()

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
calculator1Display.ScaleFactor = 0.024989800900220873
calculator1Display.SelectScaleArray = 'r'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'r'
calculator1Display.GaussianRadius = 0.0012494900450110435
calculator1Display.SetScaleArray = ['POINTS', 'r']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'r']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.SelectInputVectors = ['POINTS', 'U']
calculator1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [0.0006978997165777533, 0.0, 0.5, 0.0, 0.12496797193378187, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [0.0006978997165777533, 0.0, 0.5, 0.0, 0.12496797193378187, 1.0, 0.5, 0.0]

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
calculator1_1Display.ScaleFactor = 0.024989800900220873
calculator1_1Display.SelectScaleArray = 'U_t'
calculator1_1Display.GlyphType = 'Arrow'
calculator1_1Display.GlyphTableIndexArray = 'U_t'
calculator1_1Display.GaussianRadius = 0.0012494900450110435
calculator1_1Display.SetScaleArray = ['POINTS', 'U_t']
calculator1_1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1_1Display.OpacityArray = ['POINTS', 'U_t']
calculator1_1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1_1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1_1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1_1Display.SelectInputVectors = ['POINTS', 'U']
calculator1_1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1_1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 44.80210633975694, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1_1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 44.80210633975694, 1.0, 0.5, 0.0]

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

# rename source object
RenameSource('U_t', calculator1_1)

# create a new 'Calculator'
calculator1_2 = Calculator(registrationName='Calculator1', Input=calculator1_1)
calculator1_2.Function = ''

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
calculator1_2Display.ScaleFactor = 0.024989800900220873
calculator1_2Display.SelectScaleArray = 'num'
calculator1_2Display.GlyphType = 'Arrow'
calculator1_2Display.GlyphTableIndexArray = 'num'
calculator1_2Display.GaussianRadius = 0.0012494900450110435
calculator1_2Display.SetScaleArray = ['POINTS', 'num']
calculator1_2Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1_2Display.OpacityArray = ['POINTS', 'num']
calculator1_2Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1_2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1_2Display.PolarAxes = 'PolarAxesRepresentation'
calculator1_2Display.SelectInputVectors = ['POINTS', 'U']
calculator1_2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1_2Display.ScaleTransferFunction.Points = [-0.019081525546062433, 0.0, 0.5, 0.0, 66.26840348091179, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1_2Display.OpacityTransferFunction.Points = [-0.019081525546062433, 0.0, 0.5, 0.0, 66.26840348091179, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1_1, renderView1)

# show color bar/color legend
calculator1_2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'num'
numPWF = GetOpacityTransferFunction('num')

# get 2D transfer function for 'num'
numTF2D = GetTransferFunction2D('num')

# rename source object
RenameSource('num', calculator1_2)

# create a new 'Calculator'
calculator1_3 = Calculator(registrationName='Calculator1', Input=calculator1_2)
calculator1_3.Function = ''

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
calculator1_3Display.ScaleFactor = 0.024989800900220873
calculator1_3Display.SelectScaleArray = 'den'
calculator1_3Display.GlyphType = 'Arrow'
calculator1_3Display.GlyphTableIndexArray = 'den'
calculator1_3Display.GaussianRadius = 0.0012494900450110435
calculator1_3Display.SetScaleArray = ['POINTS', 'den']
calculator1_3Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1_3Display.OpacityArray = ['POINTS', 'den']
calculator1_3Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1_3Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1_3Display.PolarAxes = 'PolarAxesRepresentation'
calculator1_3Display.SelectInputVectors = ['POINTS', 'U']
calculator1_3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1_3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1145.1814974492881, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1_3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1145.1814974492881, 1.0, 0.5, 0.0]

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

# rename source object
RenameSource('den', calculator1_3)

# set active source
SetActiveSource(calculator1_2)

# set active source
SetActiveSource(calculator1_3)

# create a new 'Calculator'
calculator1_4 = Calculator(registrationName='Calculator1', Input=calculator1_3)
calculator1_4.Function = ''

# Properties modified on calculator1_4
calculator1_4.ResultArrayName = 'a_c'
calculator1_4.Function = 'U_t^2/r'

# show data in view
calculator1_4Display = Show(calculator1_4, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'a_c'
a_cLUT = GetColorTransferFunction('a_c')

# trace defaults for the display properties.
calculator1_4Display.Representation = 'Surface'
calculator1_4Display.ColorArrayName = ['POINTS', 'a_c']
calculator1_4Display.LookupTable = a_cLUT
calculator1_4Display.SelectTCoordArray = 'None'
calculator1_4Display.SelectNormalArray = 'None'
calculator1_4Display.SelectTangentArray = 'None'
calculator1_4Display.OSPRayScaleArray = 'a_c'
calculator1_4Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1_4Display.SelectOrientationVectors = 'None'
calculator1_4Display.ScaleFactor = 0.024989800900220873
calculator1_4Display.SelectScaleArray = 'a_c'
calculator1_4Display.GlyphType = 'Arrow'
calculator1_4Display.GlyphTableIndexArray = 'a_c'
calculator1_4Display.GaussianRadius = 0.0012494900450110435
calculator1_4Display.SetScaleArray = ['POINTS', 'a_c']
calculator1_4Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1_4Display.OpacityArray = ['POINTS', 'a_c']
calculator1_4Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1_4Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1_4Display.PolarAxes = 'PolarAxesRepresentation'
calculator1_4Display.SelectInputVectors = ['POINTS', 'U']
calculator1_4Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1_4Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 39698.24292319704, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1_4Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 39698.24292319704, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1_3, renderView1)

# show color bar/color legend
calculator1_4Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'a_c'
a_cPWF = GetOpacityTransferFunction('a_c')

# get 2D transfer function for 'a_c'
a_cTF2D = GetTransferFunction2D('a_c')

# rename source object
RenameSource('a_c', calculator1_4)

# create a new 'Point Data to Cell Data'
pointDatatoCellData1 = PointDatatoCellData(registrationName='PointDatatoCellData1', Input=calculator1_4)
pointDatatoCellData1.PointDataArraytoprocess = ['U', 'U_t', 'a_c', 'den', 'k', 'num', 'nut', 'omega', 'p', 'r']

# show data in view
pointDatatoCellData1Display = Show(pointDatatoCellData1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
pointDatatoCellData1Display.Representation = 'Surface'
pointDatatoCellData1Display.ColorArrayName = ['CELLS', 'a_c']
pointDatatoCellData1Display.LookupTable = a_cLUT
pointDatatoCellData1Display.SelectTCoordArray = 'None'
pointDatatoCellData1Display.SelectNormalArray = 'None'
pointDatatoCellData1Display.SelectTangentArray = 'None'
pointDatatoCellData1Display.OSPRayScaleFunction = 'PiecewiseFunction'
pointDatatoCellData1Display.SelectOrientationVectors = 'None'
pointDatatoCellData1Display.ScaleFactor = 0.024989800900220873
pointDatatoCellData1Display.SelectScaleArray = 'a_c'
pointDatatoCellData1Display.GlyphType = 'Arrow'
pointDatatoCellData1Display.GlyphTableIndexArray = 'a_c'
pointDatatoCellData1Display.GaussianRadius = 0.0012494900450110435
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

# create a new 'Integrate Variables'
integrateVariables1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=pointDatatoCellData1)

# rename source object
RenameSource('mid-IntVar', integrateVariables1)

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

# Properties modified on spreadSheetView1
spreadSheetView1.FieldAssociation = 'Cell Data'

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(a01_spark_arrestor_optimization_800vtk)

# create a new 'Slice'
slice1_1 = Slice(registrationName='Slice1', Input=a01_spark_arrestor_optimization_800vtk)
slice1_1.SliceType = 'Plane'
slice1_1.HyperTreeGridSlicer = 'Plane'
slice1_1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1_1.SliceType.Origin = [0.9187499284744263, 0.0, 2.2351741790771484e-08]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1_1.HyperTreeGridSlicer.Origin = [0.9187499284744263, 0.0, 2.2351741790771484e-08]

# rename source object
RenameSource('nach', slice1_1)

# Properties modified on slice1_1.SliceType
slice1_1.SliceType.Origin = [2.3, 0.0, 2.2351741790771484e-08]

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
slice1_1Display.ScaleFactor = 0.024894142895936968
slice1_1Display.SelectScaleArray = 'None'
slice1_1Display.GlyphType = 'Arrow'
slice1_1Display.GlyphTableIndexArray = 'None'
slice1_1Display.GaussianRadius = 0.0012447071447968484
slice1_1Display.SetScaleArray = ['POINTS', 'U']
slice1_1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1_1Display.OpacityArray = ['POINTS', 'U']
slice1_1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1_1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1_1Display.PolarAxes = 'PolarAxesRepresentation'
slice1_1Display.SelectInputVectors = ['POINTS', 'U']
slice1_1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1_1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 18.795164108276367, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1_1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 18.795164108276367, 1.0, 0.5, 0.0]

# hide data in view
Hide(a01_spark_arrestor_optimization_800vtk, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Integrate Variables'
integrateVariables1_1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=slice1_1)

# rename source object
RenameSource('nach-IntVar', integrateVariables1_1)

# Properties modified on integrateVariables1_1
integrateVariables1_1.DivideCellDataByVolume = 1

# Create a new 'SpreadSheet View'
spreadSheetView2 = CreateView('SpreadSheetView')
spreadSheetView2.ColumnToSort = ''
spreadSheetView2.BlockSize = 1024

# show data in view
integrateVariables1_1Display = Show(integrateVariables1_1, spreadSheetView2, 'SpreadSheetRepresentation')

# add view to a layout so it's visible in UI
AssignViewToLayout(view=spreadSheetView2, layout=layout1, hint=1)

# Properties modified on integrateVariables1_1Display
integrateVariables1_1Display.Assembly = ''

# update the view to ensure updated data information
spreadSheetView2.Update()

# set active source
SetActiveSource(a01_spark_arrestor_optimization_800vtk)

# create a new 'Slice'
slice1_2 = Slice(registrationName='Slice1', Input=a01_spark_arrestor_optimization_800vtk)
slice1_2.SliceType = 'Plane'
slice1_2.HyperTreeGridSlicer = 'Plane'
slice1_2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1_2.SliceType.Origin = [0.9187499284744263, 0.0, 2.2351741790771484e-08]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1_2.HyperTreeGridSlicer.Origin = [0.9187499284744263, 0.0, 2.2351741790771484e-08]

# rename source object
RenameSource('vor', slice1_2)

# Properties modified on slice1_2.SliceType
slice1_2.SliceType.Origin = [-0.5, 0.0, 2.2351741790771484e-08]

# show data in view
slice1_2Display = Show(slice1_2, spreadSheetView2, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView2.Update()

# Properties modified on slice1_2Display
slice1_2Display.Assembly = ''

# create a new 'Integrate Variables'
integrateVariables1_2 = IntegrateVariables(registrationName='IntegrateVariables1', Input=slice1_2)

# rename source object
RenameSource('vor-IntVar', integrateVariables1_2)

# Properties modified on integrateVariables1_2
integrateVariables1_2.DivideCellDataByVolume = 1

# show data in view
integrateVariables1_2Display = Show(integrateVariables1_2, spreadSheetView2, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView2.Update()

# Properties modified on integrateVariables1_2Display
integrateVariables1_2Display.Assembly = ''

# set active source
SetActiveSource(integrateVariables1_1)

# set active source
SetActiveSource(integrateVariables1)

# set active source
SetActiveSource(integrateVariables1_2)

# create a new 'Group Datasets'
groupDatasets1 = GroupDatasets(registrationName='GroupDatasets1', Input=[integrateVariables1_1, integrateVariables1, integrateVariables1_2])
groupDatasets1.BlockNames = ['nach-IntVar', 'mid-IntVar', 'vor-IntVar']

# show data in view
groupDatasets1Display = Show(groupDatasets1, spreadSheetView2, 'SpreadSheetRepresentation')

# hide data in view
Hide(integrateVariables1_1, spreadSheetView2)

# hide data in view
Hide(integrateVariables1_2, spreadSheetView2)

# update the view to ensure updated data information
spreadSheetView2.Update()

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Point ID']

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Point ID', 'k']

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Point ID', 'k', 'nut']

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Point ID', 'k', 'nut', 'omega']

# Properties modified on spreadSheetView2
spreadSheetView2.FieldAssociation = 'Cell Data'

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Point ID', 'k', 'nut', 'omega', 'Cell ID']

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Point ID', 'k', 'nut', 'omega', 'Cell ID', 'Cell Type']

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Point ID', 'k', 'nut', 'omega', 'Cell ID', 'Cell Type', 'cellID']

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Point ID', 'k', 'nut', 'omega', 'Cell ID', 'Cell Type', 'cellID', 'r']

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Point ID', 'k', 'nut', 'omega', 'Cell ID', 'Cell Type', 'cellID', 'r', 'U']

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Point ID', 'k', 'nut', 'omega', 'Cell ID', 'Cell Type', 'cellID', 'r', 'U', 'U_Magnitude']

# Properties modified on spreadSheetView2
spreadSheetView2.ColumnToSort = 'vtkBlockNameIndices'
spreadSheetView2.InvertOrder = 1

# Properties modified on spreadSheetView2
spreadSheetView2.InvertOrder = 0

# Properties modified on spreadSheetView2
spreadSheetView2.InvertOrder = 1

# Properties modified on spreadSheetView2
spreadSheetView2.InvertOrder = 0

# export view
ExportView('/home/cfduser/OpenFOAM/cfduser-12/run/01_spark_arrestor_optimization/data.csv', view=spreadSheetView2)

# set active source
SetActiveSource(groupDatasets1)

# set active view
SetActiveView(spreadSheetView1)

# destroy spreadSheetView1
Delete(spreadSheetView1)
del spreadSheetView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(a01_spark_arrestor_optimization_800vtk)

# Properties modified on a01_spark_arrestor_optimization_800vtkDisplay
a01_spark_arrestor_optimization_800vtkDisplay.Opacity = 0.6

# set active source
SetActiveSource(a01_spark_arrestor_optimization_800vtk)

# show data in view
a01_spark_arrestor_optimization_800vtkDisplay = Show(a01_spark_arrestor_optimization_800vtk, renderView1, 'UnstructuredGridRepresentation')

# hide data in view
Hide(pointDatatoCellData1, renderView1)

# hide data in view
Hide(slice1_1, renderView1)

# reset view to fit data
renderView1.ResetCamera(True)

# reset view to fit data
renderView1.ResetCamera(True)

# find settings proxy
generalSettings = GetSettingsProxy('GeneralSettings')

# find settings proxy
renderViewInteractionSettings = GetSettingsProxy('RenderViewInteractionSettings')

# find settings proxy
renderViewSettings = GetSettingsProxy('RenderViewSettings')

# find settings proxy
representedArrayListSettings = GetSettingsProxy('RepresentedArrayListSettings')

# find settings proxy
colorPalette = GetSettingsProxy('ColorPalette')

# layout/tab size in pixels
layout1.SetSize(1453, 790)

# current camera placement for renderView1
renderView1.CameraPosition = [0.7624999284744263, 2.2351741790771484e-08, 7.093874919022586]
renderView1.CameraFocalPoint = [0.7624999284744263, 2.2351741790771484e-08, -1.4901161193847656e-08]
renderView1.CameraViewAngle = 8.442303280568938
renderView1.CameraParallelScale = 1.8360299364748516

# save screenshot
SaveScreenshot('/home/cfduser/OpenFOAM/cfduser-12/run/01_spark_arrestor_optimization/CAD.png', renderView1, ImageResolution=[1600, 900])

# create a new 'Slice'
slice1_3 = Slice(registrationName='Slice1', Input=a01_spark_arrestor_optimization_800vtk)
slice1_3.SliceType = 'Plane'
slice1_3.HyperTreeGridSlicer = 'Plane'
slice1_3.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1_3.SliceType.Origin = [0.9187499284744263, 0.0, 2.2351741790771484e-08]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1_3.HyperTreeGridSlicer.Origin = [0.9187499284744263, 0.0, 2.2351741790771484e-08]

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
slice1_3Display.ScaleFactor = 0.3654999971389771
slice1_3Display.SelectScaleArray = 'None'
slice1_3Display.GlyphType = 'Arrow'
slice1_3Display.GlyphTableIndexArray = 'None'
slice1_3Display.GaussianRadius = 0.018274999856948852
slice1_3Display.SetScaleArray = ['POINTS', 'U']
slice1_3Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1_3Display.OpacityArray = ['POINTS', 'U']
slice1_3Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1_3Display.DataAxesGrid = 'GridAxesRepresentation'
slice1_3Display.PolarAxes = 'PolarAxesRepresentation'
slice1_3Display.SelectInputVectors = ['POINTS', 'U']
slice1_3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1_3Display.ScaleTransferFunction.Points = [-19.352184295654297, 0.0, 0.5, 0.0, 51.01696014404297, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1_3Display.OpacityTransferFunction.Points = [-19.352184295654297, 0.0, 0.5, 0.0, 51.01696014404297, 1.0, 0.5, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
spreadSheetView2.Update()

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=slice1_3.SliceType)

# hide data in view
Hide(a01_spark_arrestor_optimization_800vtk, renderView1)

# set active view
SetActiveView(spreadSheetView2)

# destroy spreadSheetView2
Delete(spreadSheetView2)
del spreadSheetView2

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# reset view to fit data
renderView1.ResetCamera(True)

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

# Rescale transfer function
uLUT.RescaleTransferFunction(0.0, 71.96952655205459)

# Rescale transfer function
uPWF.RescaleTransferFunction(0.0, 71.96952655205459)

# layout/tab size in pixels
layout1.SetSize(1453, 790)

# current camera placement for renderView1
renderView1.CameraPosition = [0.7624999284744263, 2.2351741790771484e-08, 7.0774155514511365]
renderView1.CameraFocalPoint = [0.7624999284744263, 2.2351741790771484e-08, 2.2351741790771484e-08]
renderView1.CameraViewAngle = 17.458132599220004
renderView1.CameraParallelScale = 1.831769929035257

# save screenshot
SaveScreenshot('/home/cfduser/OpenFOAM/cfduser-12/run/01_spark_arrestor_optimization/U.png', renderView1, ImageResolution=[1453, 790])

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
renderView1.CameraPosition = [0.7624999284744263, 2.2351741790771484e-08, 7.0774155514511365]
renderView1.CameraFocalPoint = [0.7624999284744263, 2.2351741790771484e-08, 2.2351741790771484e-08]
renderView1.CameraViewAngle = 17.458132599220004
renderView1.CameraParallelScale = 1.831769929035257

# save screenshot
SaveScreenshot('/home/cfduser/OpenFOAM/cfduser-12/run/01_spark_arrestor_optimization/p.png', renderView1, ImageResolution=[1453, 790])

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=slice1_3,
    SeedType='Line')
streamTracer1.Vectors = ['POINTS', 'U']
streamTracer1.MaximumStreamlineLength = 3.6549999713897705

# init the 'Line' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-1.065000057220459, -0.12499947845935822, 2.2351741790771484e-08]
streamTracer1.SeedType.Point2 = [2.5899999141693115, 0.1249995231628418, 2.2351741790771484e-08]

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=streamTracer1.SeedType)

# Properties modified on streamTracer1
streamTracer1.MaximumStreamlineLength = 0.015
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
SetActiveSource(a01_spark_arrestor_optimization_800vtk)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=streamTracer1.SeedType)

# create a new 'Stream Tracer'
streamTracer2 = StreamTracer(registrationName='StreamTracer2', Input=a01_spark_arrestor_optimization_800vtk,
    SeedType='Line')
streamTracer2.Vectors = ['POINTS', 'U']
streamTracer2.MaximumStreamlineLength = 3.9674999713897705

# init the 'Line' selected for 'SeedType'
streamTracer2.SeedType.Point1 = [-1.065000057220459, -0.25, -0.24999995529651642]
streamTracer2.SeedType.Point2 = [2.9024999141693115, 0.25, 0.25]

# set active source
SetActiveSource(a01_spark_arrestor_optimization_800vtk)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=streamTracer2.SeedType)

# show data in view
a01_spark_arrestor_optimization_800vtkDisplay = Show(a01_spark_arrestor_optimization_800vtk, renderView1, 'UnstructuredGridRepresentation')

# Properties modified on a01_spark_arrestor_optimization_800vtkDisplay
a01_spark_arrestor_optimization_800vtkDisplay.Opacity = 0.4

# set active source
SetActiveSource(streamTracer2)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=streamTracer2.SeedType)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=streamTracer2.SeedType)

# Properties modified on streamTracer2
streamTracer2.SeedType = 'Point Cloud'

# show data in view
streamTracer2Display = Show(streamTracer2, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
streamTracer2Display.Representation = 'Surface'
streamTracer2Display.ColorArrayName = [None, '']
streamTracer2Display.SelectTCoordArray = 'None'
streamTracer2Display.SelectNormalArray = 'None'
streamTracer2Display.SelectTangentArray = 'None'
streamTracer2Display.OSPRayScaleArray = 'AngularVelocity'
streamTracer2Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer2Display.SelectOrientationVectors = 'Normals'
streamTracer2Display.ScaleFactor = 0.3654508590698242
streamTracer2Display.SelectScaleArray = 'AngularVelocity'
streamTracer2Display.GlyphType = 'Arrow'
streamTracer2Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer2Display.GaussianRadius = 0.018272542953491212
streamTracer2Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer2Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer2Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer2Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer2Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer2Display.PolarAxes = 'PolarAxesRepresentation'
streamTracer2Display.SelectInputVectors = ['POINTS', 'Normals']
streamTracer2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer2Display.ScaleTransferFunction.Points = [-51705.12648379898, 0.0, 0.5, 0.0, 89294.95345345864, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer2Display.OpacityTransferFunction.Points = [-51705.12648379898, 0.0, 0.5, 0.0, 89294.95345345864, 1.0, 0.5, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Tube'
tube1 = Tube(registrationName='Tube1', Input=streamTracer2)
tube1.Scalars = ['POINTS', 'AngularVelocity']
tube1.Vectors = ['POINTS', 'Normals']
tube1.Radius = 0.036545085906982425

# Properties modified on tube1
tube1.Radius = 0.003

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
tube1Display.ScaleFactor = 0.3656250238418579
tube1Display.SelectScaleArray = 'AngularVelocity'
tube1Display.GlyphType = 'Arrow'
tube1Display.GlyphTableIndexArray = 'AngularVelocity'
tube1Display.GaussianRadius = 0.018281251192092896
tube1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display.OpacityArray = ['POINTS', 'AngularVelocity']
tube1Display.OpacityTransferFunction = 'PiecewiseFunction'
tube1Display.DataAxesGrid = 'GridAxesRepresentation'
tube1Display.PolarAxes = 'PolarAxesRepresentation'
tube1Display.SelectInputVectors = ['POINTS', 'Normals']
tube1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube1Display.ScaleTransferFunction.Points = [-51705.12648379898, 0.0, 0.5, 0.0, 89294.95345345864, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube1Display.OpacityTransferFunction.Points = [-51705.12648379898, 0.0, 0.5, 0.0, 89294.95345345864, 1.0, 0.5, 0.0]

# hide data in view
Hide(streamTracer2, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(tube1Display, ('POINTS', 'U', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
tube1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tube1Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera(True)

# layout/tab size in pixels
layout1.SetSize(1453, 790)

# current camera placement for renderView1
renderView1.CameraPosition = [0.7632975578308105, 4.9620866775512695e-05, 7.0979818518070905]
renderView1.CameraFocalPoint = [0.7632975578308105, 4.9620866775512695e-05, -0.00020263344049453735]
renderView1.CameraViewAngle = 17.733425097499428
renderView1.CameraParallelScale = 1.8371453304333076

# save screenshot
SaveScreenshot('/home/cfduser/OpenFOAM/cfduser-12/run/01_spark_arrestor_optimization/Streamlines.png', renderView1, ImageResolution=[1600, 900])

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
renderView1.CameraPosition = [0.7632975578308105, 4.9620866775512695e-05, 7.0979818518070905]
renderView1.CameraFocalPoint = [0.7632975578308105, 4.9620866775512695e-05, -0.00020263344049453735]
renderView1.CameraViewAngle = 17.733425097499428
renderView1.CameraParallelScale = 1.8371453304333076

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).