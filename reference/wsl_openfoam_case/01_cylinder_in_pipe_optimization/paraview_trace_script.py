# trace generated using paraview version 5.11.2
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()



#######################################################################################
# Project Path Setup
# =====================================================================================
# NOTE: The case path must be updated in four places throughout this Script.
#######################################################################################



# create a new 'OpenFOAMReader'
optimizationfoam = OpenFOAMReader(registrationName='optimization.foam', FileName='/home/cfduser/OpenFOAM/cfduser-12/run/01_cylinder_in_pipe_optimization/optimization.foam') # <-- Path #1

optimizationfoam.MeshRegions = ['internalMesh']
optimizationfoam.CellArrays = ['U', 'k', 'nut', 'omega', 'p', 'wallShearStress']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on optimizationfoam
optimizationfoam.MeshRegions = ['internalMesh', 'patch/wall_inner']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
optimizationfoamDisplay = Show(optimizationfoam, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# trace defaults for the display properties.
optimizationfoamDisplay.Representation = 'Surface'
optimizationfoamDisplay.ColorArrayName = ['POINTS', 'p']
optimizationfoamDisplay.LookupTable = pLUT
optimizationfoamDisplay.SelectTCoordArray = 'None'
optimizationfoamDisplay.SelectNormalArray = 'None'
optimizationfoamDisplay.SelectTangentArray = 'None'
optimizationfoamDisplay.OSPRayScaleArray = 'p'
optimizationfoamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
optimizationfoamDisplay.SelectOrientationVectors = 'U'
optimizationfoamDisplay.ScaleFactor = 0.17309999763965608
optimizationfoamDisplay.SelectScaleArray = 'p'
optimizationfoamDisplay.GlyphType = 'Arrow'
optimizationfoamDisplay.GlyphTableIndexArray = 'p'
optimizationfoamDisplay.GaussianRadius = 0.008654999881982803
optimizationfoamDisplay.SetScaleArray = ['POINTS', 'p']
optimizationfoamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
optimizationfoamDisplay.OpacityArray = ['POINTS', 'p']
optimizationfoamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
optimizationfoamDisplay.DataAxesGrid = 'GridAxesRepresentation'
optimizationfoamDisplay.PolarAxes = 'PolarAxesRepresentation'
optimizationfoamDisplay.SelectInputVectors = ['POINTS', 'U']
optimizationfoamDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
optimizationfoamDisplay.ScaleTransferFunction.Points = [-1074.0, 0.0, 0.5, 0.0, 21.433399200439453, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
optimizationfoamDisplay.OpacityTransferFunction.Points = [-1074.0, 0.0, 0.5, 0.0, 21.433399200439453, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

# show color bar/color legend
optimizationfoamDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# get 2D transfer function for 'p'
pTF2D = GetTransferFunction2D('p')

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=optimizationfoam)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.46549998223781586, -4.2691826820373535e-06, 2.102181315422058e-05]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [0.46549998223781586, -4.2691826820373535e-06, 2.102181315422058e-05]

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=slice1.SliceType)

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'p']
slice1Display.LookupTable = pLUT
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.OSPRayScaleArray = 'p'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'U'
slice1Display.ScaleFactor = 0.1699999958276749
slice1Display.SelectScaleArray = 'p'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'p'
slice1Display.GaussianRadius = 0.008499999791383743
slice1Display.SetScaleArray = ['POINTS', 'p']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'p']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'
slice1Display.SelectInputVectors = ['POINTS', 'U']
slice1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [-987.2078247070312, 0.0, 0.5, 0.0, 10.898215293884277, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [-987.2078247070312, 0.0, 0.5, 0.0, 10.898215293884277, 1.0, 0.5, 0.0]

# hide data in view
Hide(optimizationfoam, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# rename source object
RenameSource('xy', slice1)

# set active source
SetActiveSource(optimizationfoam)

# create a new 'Slice'
slice1_1 = Slice(registrationName='Slice1', Input=optimizationfoam)
slice1_1.SliceType = 'Plane'
slice1_1.HyperTreeGridSlicer = 'Plane'
slice1_1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1_1.SliceType.Origin = [0.46549998223781586, -4.2691826820373535e-06, 2.102181315422058e-05]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1_1.HyperTreeGridSlicer.Origin = [0.46549998223781586, -4.2691826820373535e-06, 2.102181315422058e-05]

# rename source object
RenameSource('up', slice1_1)

# Properties modified on slice1_1.SliceType
slice1_1.SliceType.Origin = [-0.1, 0.0, 0.0]

# show data in view
slice1_1Display = Show(slice1_1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1_1Display.Representation = 'Surface'
slice1_1Display.ColorArrayName = ['POINTS', 'p']
slice1_1Display.LookupTable = pLUT
slice1_1Display.SelectTCoordArray = 'None'
slice1_1Display.SelectNormalArray = 'None'
slice1_1Display.SelectTangentArray = 'None'
slice1_1Display.OSPRayScaleArray = 'p'
slice1_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1_1Display.SelectOrientationVectors = 'U'
slice1_1Display.ScaleFactor = 0.01975768804550171
slice1_1Display.SelectScaleArray = 'p'
slice1_1Display.GlyphType = 'Arrow'
slice1_1Display.GlyphTableIndexArray = 'p'
slice1_1Display.GaussianRadius = 0.0009878844022750855
slice1_1Display.SetScaleArray = ['POINTS', 'p']
slice1_1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1_1Display.OpacityArray = ['POINTS', 'p']
slice1_1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1_1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1_1Display.PolarAxes = 'PolarAxesRepresentation'
slice1_1Display.SelectInputVectors = ['POINTS', 'U']
slice1_1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1_1Display.ScaleTransferFunction.Points = [-421.9056701660156, 0.0, 0.5, 0.0, -405.2984619140625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1_1Display.OpacityTransferFunction.Points = [-421.9056701660156, 0.0, 0.5, 0.0, -405.2984619140625, 1.0, 0.5, 0.0]

# hide data in view
Hide(optimizationfoam, renderView1)

# show color bar/color legend
slice1_1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=slice1_1.SliceType)

# create a new 'Point Data to Cell Data'
pointDatatoCellData1 = PointDatatoCellData(registrationName='PointDatatoCellData1', Input=slice1_1)
pointDatatoCellData1.PointDataArraytoprocess = ['U', 'k', 'nut', 'omega', 'p', 'wallShearStress']

# show data in view
pointDatatoCellData1Display = Show(pointDatatoCellData1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
pointDatatoCellData1Display.Representation = 'Surface'
pointDatatoCellData1Display.ColorArrayName = ['CELLS', 'p']
pointDatatoCellData1Display.LookupTable = pLUT
pointDatatoCellData1Display.SelectTCoordArray = 'None'
pointDatatoCellData1Display.SelectNormalArray = 'None'
pointDatatoCellData1Display.SelectTangentArray = 'None'
pointDatatoCellData1Display.OSPRayScaleFunction = 'PiecewiseFunction'
pointDatatoCellData1Display.SelectOrientationVectors = 'U'
pointDatatoCellData1Display.ScaleFactor = 0.01975768804550171
pointDatatoCellData1Display.SelectScaleArray = 'p'
pointDatatoCellData1Display.GlyphType = 'Arrow'
pointDatatoCellData1Display.GlyphTableIndexArray = 'p'
pointDatatoCellData1Display.GaussianRadius = 0.0009878844022750855
pointDatatoCellData1Display.SetScaleArray = [None, '']
pointDatatoCellData1Display.ScaleTransferFunction = 'PiecewiseFunction'
pointDatatoCellData1Display.OpacityArray = [None, '']
pointDatatoCellData1Display.OpacityTransferFunction = 'PiecewiseFunction'
pointDatatoCellData1Display.DataAxesGrid = 'GridAxesRepresentation'
pointDatatoCellData1Display.PolarAxes = 'PolarAxesRepresentation'
pointDatatoCellData1Display.SelectInputVectors = [None, '']
pointDatatoCellData1Display.WriteLog = ''

# hide data in view
Hide(slice1_1, renderView1)

# show color bar/color legend
pointDatatoCellData1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(pointDatatoCellData1, renderView1)

# create a new 'Integrate Variables'
integrateVariables1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=pointDatatoCellData1)

# rename source object
RenameSource('up-IntVar', integrateVariables1)

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

# set active source
SetActiveSource(optimizationfoam)

# create a new 'Slice'
slice1_2 = Slice(registrationName='Slice1', Input=optimizationfoam)
slice1_2.SliceType = 'Plane'
slice1_2.HyperTreeGridSlicer = 'Plane'
slice1_2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1_2.SliceType.Origin = [0.46549998223781586, -4.2691826820373535e-06, 2.102181315422058e-05]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1_2.HyperTreeGridSlicer.Origin = [0.46549998223781586, -4.2691826820373535e-06, 2.102181315422058e-05]

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=slice1_2.SliceType)

# Properties modified on slice1_2.SliceType
slice1_2.SliceType.Origin = [0.6, 0.0, 0.0]

# show data in view
slice1_2Display = Show(slice1_2, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# rename source object
RenameSource('down', slice1_2)

# destroy spreadSheetView1
Delete(spreadSheetView1)
del spreadSheetView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# create a new 'Point Data to Cell Data'
pointDatatoCellData2 = PointDatatoCellData(registrationName='PointDatatoCellData2', Input=slice1_2)
pointDatatoCellData2.PointDataArraytoprocess = ['U', 'k', 'nut', 'omega', 'p', 'wallShearStress']

# show data in view
pointDatatoCellData2Display = Show(pointDatatoCellData2, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
pointDatatoCellData2Display.Representation = 'Surface'
pointDatatoCellData2Display.ColorArrayName = ['CELLS', 'p']
pointDatatoCellData2Display.LookupTable = pLUT
pointDatatoCellData2Display.SelectTCoordArray = 'None'
pointDatatoCellData2Display.SelectNormalArray = 'None'
pointDatatoCellData2Display.SelectTangentArray = 'None'
pointDatatoCellData2Display.OSPRayScaleFunction = 'PiecewiseFunction'
pointDatatoCellData2Display.SelectOrientationVectors = 'U'
pointDatatoCellData2Display.ScaleFactor = 0.019844886660575867
pointDatatoCellData2Display.SelectScaleArray = 'p'
pointDatatoCellData2Display.GlyphType = 'Arrow'
pointDatatoCellData2Display.GlyphTableIndexArray = 'p'
pointDatatoCellData2Display.GaussianRadius = 0.0009922443330287933
pointDatatoCellData2Display.SetScaleArray = [None, '']
pointDatatoCellData2Display.ScaleTransferFunction = 'PiecewiseFunction'
pointDatatoCellData2Display.OpacityArray = [None, '']
pointDatatoCellData2Display.OpacityTransferFunction = 'PiecewiseFunction'
pointDatatoCellData2Display.DataAxesGrid = 'GridAxesRepresentation'
pointDatatoCellData2Display.PolarAxes = 'PolarAxesRepresentation'
pointDatatoCellData2Display.SelectInputVectors = [None, '']
pointDatatoCellData2Display.WriteLog = ''

# show color bar/color legend
pointDatatoCellData2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Integrate Variables'
integrateVariables1_1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=pointDatatoCellData2)

# rename source object
RenameSource('down-IntVar', integrateVariables1_1)

# Properties modified on integrateVariables1_1
integrateVariables1_1.DivideCellDataByVolume = 1

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024

# show data in view
integrateVariables1_1Display = Show(integrateVariables1_1, spreadSheetView1, 'SpreadSheetRepresentation')

# add view to a layout so it's visible in UI
AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=0)

# Properties modified on integrateVariables1_1Display
integrateVariables1_1Display.Assembly = ''

# update the view to ensure updated data information
spreadSheetView1.Update()

# set active source
SetActiveSource(optimizationfoam)

# create a new 'Extract Block'
extractBlock1 = ExtractBlock(registrationName='ExtractBlock1', Input=optimizationfoam)

# Properties modified on extractBlock1
extractBlock1.Selectors = ['/Root/boundary']

# show data in view
extractBlock1Display = Show(extractBlock1, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# set active view
SetActiveView(renderView1)

# create a new 'Point Data to Cell Data'
pointDatatoCellData3 = PointDatatoCellData(registrationName='PointDatatoCellData3', Input=extractBlock1)
pointDatatoCellData3.PointDataArraytoprocess = ['U', 'k', 'nut', 'omega', 'p', 'wallShearStress']

# show data in view
pointDatatoCellData3Display = Show(pointDatatoCellData3, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
pointDatatoCellData3Display.Representation = 'Surface'
pointDatatoCellData3Display.ColorArrayName = ['CELLS', 'p']
pointDatatoCellData3Display.LookupTable = pLUT
pointDatatoCellData3Display.SelectTCoordArray = 'None'
pointDatatoCellData3Display.SelectNormalArray = 'None'
pointDatatoCellData3Display.SelectTangentArray = 'None'
pointDatatoCellData3Display.OSPRayScaleFunction = 'PiecewiseFunction'
pointDatatoCellData3Display.SelectOrientationVectors = 'U'
pointDatatoCellData3Display.ScaleFactor = 0.010000676006075083
pointDatatoCellData3Display.SelectScaleArray = 'p'
pointDatatoCellData3Display.GlyphType = 'Arrow'
pointDatatoCellData3Display.GlyphTableIndexArray = 'p'
pointDatatoCellData3Display.GaussianRadius = 0.0005000338003037541
pointDatatoCellData3Display.SetScaleArray = [None, '']
pointDatatoCellData3Display.ScaleTransferFunction = 'PiecewiseFunction'
pointDatatoCellData3Display.OpacityArray = [None, '']
pointDatatoCellData3Display.OpacityTransferFunction = 'PiecewiseFunction'
pointDatatoCellData3Display.DataAxesGrid = 'GridAxesRepresentation'
pointDatatoCellData3Display.PolarAxes = 'PolarAxesRepresentation'
pointDatatoCellData3Display.SelectInputVectors = [None, '']
pointDatatoCellData3Display.WriteLog = ''

# show color bar/color legend
pointDatatoCellData3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Generate Surface Normals'
generateSurfaceNormals1 = GenerateSurfaceNormals(registrationName='GenerateSurfaceNormals1', Input=pointDatatoCellData3)

# Properties modified on generateSurfaceNormals1
generateSurfaceNormals1.ComputeCellNormals = 1

# show data in view
generateSurfaceNormals1Display = Show(generateSurfaceNormals1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
generateSurfaceNormals1Display.Representation = 'Surface'
generateSurfaceNormals1Display.ColorArrayName = ['CELLS', 'p']
generateSurfaceNormals1Display.LookupTable = pLUT
generateSurfaceNormals1Display.SelectTCoordArray = 'None'
generateSurfaceNormals1Display.SelectNormalArray = 'Normals'
generateSurfaceNormals1Display.SelectTangentArray = 'None'
generateSurfaceNormals1Display.OSPRayScaleArray = 'Normals'
generateSurfaceNormals1Display.OSPRayScaleFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.SelectOrientationVectors = 'U'
generateSurfaceNormals1Display.ScaleFactor = 0.010000676006075083
generateSurfaceNormals1Display.SelectScaleArray = 'p'
generateSurfaceNormals1Display.GlyphType = 'Arrow'
generateSurfaceNormals1Display.GlyphTableIndexArray = 'p'
generateSurfaceNormals1Display.GaussianRadius = 0.0005000338003037541
generateSurfaceNormals1Display.SetScaleArray = ['POINTS', 'Normals']
generateSurfaceNormals1Display.ScaleTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.OpacityArray = ['POINTS', 'Normals']
generateSurfaceNormals1Display.OpacityTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.DataAxesGrid = 'GridAxesRepresentation'
generateSurfaceNormals1Display.PolarAxes = 'PolarAxesRepresentation'
generateSurfaceNormals1Display.SelectInputVectors = ['POINTS', 'Normals']
generateSurfaceNormals1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
generateSurfaceNormals1Display.ScaleTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
generateSurfaceNormals1Display.OpacityTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(pointDatatoCellData3, renderView1)

# show color bar/color legend
generateSurfaceNormals1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=generateSurfaceNormals1)
calculator1.Function = ''

# set active source
SetActiveSource(optimizationfoam)

# set active source
SetActiveSource(generateSurfaceNormals1)

# set active source
SetActiveSource(calculator1)

# rename source object
RenameSource('drag', calculator1)

# Properties modified on calculator1
calculator1.AttributeType = 'Cell Data'
calculator1.ResultArrayName = 'drag'
calculator1.Function = '(p*Normals_X+wallShearStress_X)*1.184'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'drag'
dragLUT = GetColorTransferFunction('drag')

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['CELLS', 'drag']
calculator1Display.LookupTable = dragLUT
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'Normals'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.OSPRayScaleArray = 'Normals'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'U'
calculator1Display.ScaleFactor = 0.010000676006075083
calculator1Display.SelectScaleArray = 'drag'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'drag'
calculator1Display.GaussianRadius = 0.0005000338003037541
calculator1Display.SetScaleArray = ['POINTS', 'Normals']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'Normals']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.SelectInputVectors = ['POINTS', 'Normals']
calculator1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(generateSurfaceNormals1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'drag'
dragPWF = GetOpacityTransferFunction('drag')

# get 2D transfer function for 'drag'
dragTF2D = GetTransferFunction2D('drag')

# set active source
SetActiveSource(generateSurfaceNormals1)

# set active source
SetActiveSource(calculator1)

# create a new 'Calculator'
calculator1_1 = Calculator(registrationName='Calculator1', Input=calculator1)
calculator1_1.Function = ''

# set active source
SetActiveSource(calculator1)

# Properties modified on calculator1_1
calculator1_1.AttributeType = 'Cell Data'
calculator1_1.ResultArrayName = 'lift'
calculator1_1.Function = '(p*Normals+wallShearStress)*1.184'

# show data in view
calculator1_1Display = Show(calculator1_1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
calculator1_1Display.Representation = 'Surface'
calculator1_1Display.ColorArrayName = ['CELLS', 'drag']
calculator1_1Display.LookupTable = dragLUT
calculator1_1Display.SelectTCoordArray = 'None'
calculator1_1Display.SelectNormalArray = 'Normals'
calculator1_1Display.SelectTangentArray = 'None'
calculator1_1Display.OSPRayScaleArray = 'Normals'
calculator1_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1_1Display.SelectOrientationVectors = 'lift'
calculator1_1Display.ScaleFactor = 0.010000676006075083
calculator1_1Display.SelectScaleArray = 'drag'
calculator1_1Display.GlyphType = 'Arrow'
calculator1_1Display.GlyphTableIndexArray = 'drag'
calculator1_1Display.GaussianRadius = 0.0005000338003037541
calculator1_1Display.SetScaleArray = ['POINTS', 'Normals']
calculator1_1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1_1Display.OpacityArray = ['POINTS', 'Normals']
calculator1_1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1_1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1_1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1_1Display.SelectInputVectors = ['POINTS', 'Normals']
calculator1_1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1_1Display.ScaleTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1_1Display.OpacityTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
calculator1_1Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on calculator1
calculator1.Function = '(-p*Normals_X+wallShearStress_X)*1.184'

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
dragLUT.RescaleTransferFunction(-652.5802748654007, 651.6352489597916)

# Rescale transfer function
dragPWF.RescaleTransferFunction(-652.5802748654007, 651.6352489597916)

# set active source
SetActiveSource(calculator1_1)

# rename source object
RenameSource('lift', calculator1_1)

# Properties modified on calculator1_1
calculator1_1.Function = '(-p*Normals_Y+wallShearStress_Y)*1.184'

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(calculator1)

# set active source
SetActiveSource(calculator1_1)

# create a new 'Integrate Variables'
integrateVariables1_2 = IntegrateVariables(registrationName='IntegrateVariables1', Input=calculator1_1)

# Properties modified on integrateVariables1_2
integrateVariables1_2.DivideCellDataByVolume = 1

# Create a new 'SpreadSheet View'
spreadSheetView2 = CreateView('SpreadSheetView')
spreadSheetView2.ColumnToSort = ''
spreadSheetView2.BlockSize = 1024

# show data in view
integrateVariables1_2Display = Show(integrateVariables1_2, spreadSheetView2, 'SpreadSheetRepresentation')

# add view to a layout so it's visible in UI
AssignViewToLayout(view=spreadSheetView2, layout=layout1, hint=1)

# Properties modified on integrateVariables1_2Display
integrateVariables1_2Display.Assembly = ''

# update the view to ensure updated data information
spreadSheetView2.Update()

# rename source object
RenameSource('cyc-IntVar', integrateVariables1_2)

# set active source
SetActiveSource(integrateVariables1_1)

# set active source
SetActiveSource(integrateVariables1)

# set active source
SetActiveSource(integrateVariables1_1)

# set active source
SetActiveSource(integrateVariables1_2)

# create a new 'Group Datasets'
groupDatasets1 = GroupDatasets(registrationName='GroupDatasets1', Input=[integrateVariables1, integrateVariables1_1, integrateVariables1_2])
groupDatasets1.BlockNames = ['up-IntVar', 'down-IntVar', 'cyc-IntVar']

# set active view
SetActiveView(spreadSheetView1)

# destroy spreadSheetView1
Delete(spreadSheetView1)
del spreadSheetView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(spreadSheetView2)

# show data in view
groupDatasets1Display = Show(groupDatasets1, spreadSheetView2, 'SpreadSheetRepresentation')

# hide data in view
Hide(integrateVariables1_2, spreadSheetView2)

# update the view to ensure updated data information
spreadSheetView2.Update()

# Properties modified on spreadSheetView2
spreadSheetView2.FieldAssociation = 'Cell Data'

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Cell ID']

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Area']

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Area', 'Cell Type']

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Area', 'Cell Type', 'k']

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Area', 'Cell Type', 'k', 'Normals_0']

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Area', 'Cell Type', 'k', 'Normals_0', 'wallShearStress_Magnitude']

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Area', 'Cell Type', 'k', 'Normals_0', 'wallShearStress_Magnitude', 'wallShearStress']

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Area', 'Cell Type', 'k', 'Normals_0', 'wallShearStress_Magnitude', 'wallShearStress', 'U_Magnitude']

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Area', 'Cell Type', 'k', 'Normals_0', 'wallShearStress_Magnitude', 'wallShearStress', 'U_Magnitude', 'U']

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Area', 'Cell Type', 'k', 'Normals_0', 'wallShearStress_Magnitude', 'wallShearStress', 'U_Magnitude', 'U', 'omega']

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Area', 'Cell Type', 'k', 'Normals_0', 'wallShearStress_Magnitude', 'wallShearStress', 'U_Magnitude', 'U', 'omega', 'nut']

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Area', 'Cell Type', 'k', 'Normals_0', 'wallShearStress_Magnitude', 'wallShearStress', 'U_Magnitude', 'U', 'omega', 'nut', 'Normals_Magnitude']

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Area', 'Cell Type', 'k', 'Normals_0', 'wallShearStress_Magnitude', 'wallShearStress', 'U_Magnitude', 'U', 'omega', 'nut', 'Normals_Magnitude', 'Normals_2']

# Properties modified on spreadSheetView2
spreadSheetView2.HiddenColumnLabels = ['Block Number', 'Cell ID', 'Area', 'Cell Type', 'k', 'Normals_0', 'wallShearStress_Magnitude', 'wallShearStress', 'U_Magnitude', 'U', 'omega', 'nut', 'Normals_Magnitude', 'Normals_2', 'Normals_1']

# export view
ExportView('/home/cfduser/OpenFOAM/cfduser-12/run/01_cylinder_in_pipe_optimization/data.csv', view=spreadSheetView2) # <-- Path #2

# set active view
SetActiveView(renderView1)

# hide data in view
Hide(calculator1_1, renderView1)

# hide data in view
Hide(pointDatatoCellData2, renderView1)

# set active view
SetActiveView(spreadSheetView2)

# destroy spreadSheetView2
Delete(spreadSheetView2)
del spreadSheetView2

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# get color legend/bar for pLUT in view renderView1
pLUTColorBar = GetScalarBar(pLUT, renderView1)

# change scalar bar placement
pLUTColorBar.WindowLocation = 'Any Location'
pLUTColorBar.Position = [0.9112181693048864, 0.04556962025316455]
pLUTColorBar.ScalarBarLength = 0.33000000000000007

# reset view to fit data
renderView1.ResetCamera(True)

# set active source
SetActiveSource(slice1)

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'U', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')

# get 2D transfer function for 'U'
uTF2D = GetTransferFunction2D('U')

# layout/tab size in pixels
layout1.SetSize(1453, 790)

# current camera placement for renderView1
renderView1.CameraPosition = [0.44999997317790985, 2.2999942302703857e-05, 3.306599936336643]
renderView1.CameraFocalPoint = [0.44999997317790985, 2.2999942302703857e-05, 2.102181315422058e-05]
renderView1.CameraViewAngle = 17.366368433126866
renderView1.CameraParallelScale = 0.855805597213099

# save screenshot
SaveScreenshot('/home/cfduser/OpenFOAM/cfduser-12/run/01_cylinder_in_pipe_optimization/U.png', renderView1, ImageResolution=[1453, 790]) # <-- Path #3

# reset view to fit data bounds
renderView1.ResetCamera(-0.4000000059604645, 1.2999999523162842, -0.09949210286140442, 0.09953810274600983, 2.102181315422058e-05, 2.102181315422058e-05, True)

# change representation type
slice1Display.SetRepresentationType('Surface LIC')

# layout/tab size in pixels
layout1.SetSize(1453, 790)

# current camera placement for renderView1
renderView1.CameraPosition = [0.44999997317790985, 2.2999942302703857e-05, 3.306599936336643]
renderView1.CameraFocalPoint = [0.44999997317790985, 2.2999942302703857e-05, 2.102181315422058e-05]
renderView1.CameraViewAngle = 17.366368433126866
renderView1.CameraParallelScale = 0.855805597213099

# save screenshot
SaveScreenshot('/home/cfduser/OpenFOAM/cfduser-12/run/01_cylinder_in_pipe_optimization/LIC.png', renderView1, ImageResolution=[1453, 790]) # <-- Path #4

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
renderView1.CameraPosition = [0.44999997317790985, 2.2999942302703857e-05, 3.306599936336643]
renderView1.CameraFocalPoint = [0.44999997317790985, 2.2999942302703857e-05, 2.102181315422058e-05]
renderView1.CameraViewAngle = 17.366368433126866
renderView1.CameraParallelScale = 0.855805597213099

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).