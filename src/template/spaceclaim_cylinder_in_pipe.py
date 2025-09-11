# Python Script, API Version = V252

D = 200.0 # diameter of pipe at the beginning (mm)


# Optimization Parameters
cyclinder_length = 100.0 # 100
cyclinder_diameter = 50 # 50


design_number = 2

try:
    cyclinder_length = float(argsDict["parameter_0"])
	cyclinder_diameter = float(argsDict["parameter_1"])
    

except NameError:
    pass


# Solidify Sketch
mode = InteractionMode.Solid
result = ViewHelper.SetViewMode(mode, None)
# EndBlock

######################### Main Pipe Generation #########################################


# Set Sketch Plane
sectionPlane = Plane.PlaneXY
result = ViewHelper.SetSketchPlane(sectionPlane, None)
# EndBlock

# Create Sketch Cylinder
result = CylinderBody.Create(Point.Create(MM(0), MM(0), MM(0)), Point.Create(MM(6*D+100), MM(-1.59198825996909E-13), MM(0)), Point.Create(MM(6*D+100), MM(D/2), MM(0)), ExtrudeType.None)
# EndBlock

# Solidify Sketch
mode = InteractionMode.Solid
result = ViewHelper.SetViewMode(mode, None)
# EndBlock

# Extrude 1 Face
selection = FaceSelection.Create(GetRootPart().Bodies[0].Faces[1])
options = ExtrudeFaceOptions()
result = ExtrudeFaces.Execute(selection, MM(2*D), options)
# EndBlock

######################### Name the Boundaries #########################################

# Create Named Selection Group
primarySelection = FaceSelection.Create(GetRootPart().Bodies[0].Faces[1])
secondarySelection = Selection.Empty()
result = NamedSelection.Create(primarySelection, secondarySelection, "Group1")
# EndBlock

# Rename Named Selection
result = NamedSelection.Rename("Group1", "bc_inlet")
# EndBlock

# Create Named Selection Group
primarySelection = FaceSelection.Create(GetRootPart().Bodies[0].Faces[0])
secondarySelection = Selection.Empty()
result = NamedSelection.Create(primarySelection, secondarySelection, "Group1")
# EndBlock

# Rename Named Selection
result = NamedSelection.Rename("Group1", "bc_outlet")
# EndBlock

# Create Named Selection Group
primarySelection = FaceSelection.Create(GetRootPart().Bodies[0].Faces[2])
secondarySelection = Selection.Empty()
result = NamedSelection.Create(primarySelection, secondarySelection, "Group1")
# EndBlock

# Rename Named Selection
result = NamedSelection.Rename("Group1", "wall_outer")
# EndBlock

######################### Inner Cylindr bluff body generation #########################################

# Set Sketch Plane
sectionPlane = Plane.PlaneXY
result = ViewHelper.SetSketchPlane(sectionPlane, None)
# EndBlock

# Create Sketch Cylinder
result = CylinderBody.Create(Point.Create(MM(0), MM(0), MM(0)), Point.Create(MM(cyclinder_length), MM(-1.22460635382238E-14), MM(0)), Point.Create(MM(cyclinder_length), MM(cyclinder_diameter/2), MM(0)), ExtrudeType.ForceIndependent)
# EndBlock

# Solidify Sketch
mode = InteractionMode.Solid
result = ViewHelper.SetViewMode(mode, None)
# EndBlock

# Intersecting bodies
targets = BodySelection.Create(GetRootPart().Bodies[0])
tools = BodySelection.Create(GetRootPart().Bodies[1])
options = MakeSolidsOptions()
options.KeepCutter = False
options.SubtractFromTarget = True
result = Combine.Intersect(targets, tools, options)
# EndBlock

######################### BOI body generation #########################################

# Set Sketch Plane
sectionPlane = Plane.PlaneXY
result = ViewHelper.SetSectionPlane(sectionPlane, None)
# EndBlock

# Set Sketch Plane
mode = InteractionMode.Sketch
result = ViewHelper.SetViewMode(mode, None)
# EndBlock

# Create Sketch Cylinder
result = CylinderBody.Create(Point.Create(MM(0), MM(0), MM(0)), Point.Create(MM(6*D+200), MM(2.69032116462925E-12), MM(0)), Point.Create(MM(6*D+200), MM(cyclinder_diameter/2+10), MM(0)), ExtrudeType.ForceIndependent)
# EndBlock

# Rename 'Solid' to 'boi'
selection = BodySelection.Create(GetRootPart().Bodies[1])
result = RenameObject.Execute(selection,"boi")
# EndBlock

# Change Object Visibility
selection = BodySelection.Create(GetRootPart().Bodies[1])
visibility = VisibilityType.Hide
inSelectedView = False
faceLevel = False
ViewHelper.SetObjectVisibility(selection, visibility, inSelectedView, faceLevel)
# EndBlock

# Solidify Sketch
mode = InteractionMode.Solid
result = ViewHelper.SetViewMode(mode, None)
# EndBlock

######################### Naming the inner Cylinder #########################################

# Create Named Selection Group
primarySelection = FaceSelection.Create([GetRootPart().Bodies[0].Faces[3],
	GetRootPart().Bodies[0].Faces[5],
	GetRootPart().Bodies[0].Faces[4]])
secondarySelection = Selection.Empty()
result = NamedSelection.Create(primarySelection, secondarySelection, "Group1")
# EndBlock


# Rename Named Selection
result = NamedSelection.Rename("Group1", "wall_inner")
# EndBlock