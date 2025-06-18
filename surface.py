'''
Run this as follows
$visit -cli -nowin -s ./color.py sol sol.plt 
'''
#or
'''
Run this as follows to generate sequence of .png files
$visit -cli -nowin -s ./color.py sol 
'''
# sol -> denotes the variable name
# If you  wish you can also specify the output file name above as
'''
$visit -cli -nowin -s ./color.py sol sol.plt figurename
'''

#Contour color plot
import sys
from visit_utils import *


if len(sys.argv) == 1:
    print('Specify Density|Velx|Vely|Pressure')
    exit()

variable = sys.argv[1]
filename = sys.argv[2]
# Check if outputfile is provided, otherwise set it to False
outputfile = sys.argv[3] if len(sys.argv) > 3 else False

if len(sys.argv) > 2: 
    OpenDatabase(filename)
else: 
# use the below one to produce several plots
    OpenDatabase("sol_*.plt database")



s = SaveWindowAttributes()
if len(sys.argv) > 2: 
    s.format = s.POSTSCRIPT          # PNG or POSTSCRIPT
else: 
    s.format = s.PNG
s.width, s.height = 1120,1000
s.screenCapture = 0
#s.family = 1
s.resConstraint = s.NoConstraint
# If outputfile is not empty, save the figure with the given filename
if outputfile:
    s.fileName = outputfile
else:
    s.fileName = "sol_" + variable + "_"
#s.advancedMultiWindowSave = 0
SetSaveWindowAttributes(s)

AddPlot("Pseudocolor", variable)
#AddPlot("Contour", variable)
AddOperator("Elevate", 1)
opAtts = ElevateAttributes()
opAtts.zeroFlag = 0
SetOperatorOptions(opAtts)


# coppied this from the command window of visit
# This is accessed through: control --> comand --->Record ---> stop
# once it is stopped scripts will appear in the tab 1|2|3|...
# You need to plot the figure and keep it in a position we want to save, use the record button after that.

# Begin spontaneous state
# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.53411, -0.710854, 0.457617)
View3DAtts.focus = (0.5, 0.5, 0)
View3DAtts.viewUp = (-0.320738, 0.330444, 0.887656)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 1.21987
View3DAtts.nearPlane = -2.43974
View3DAtts.farPlane = 2.43974
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.5, 0.5, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.504351, -0.731075, 0.459521)
View3DAtts.focus = (0.5, 0.5, 0)
View3DAtts.viewUp = (-0.316181, 0.33885, 0.886121)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 1.21987
View3DAtts.nearPlane = -2.43974
View3DAtts.farPlane = 2.43974
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.5, 0.5, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.460708, -0.735237, 0.497167)
View3DAtts.focus = (0.5, 0.5, 0)
View3DAtts.viewUp = (-0.407867, 0.322124, 0.854331)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 1.21987
View3DAtts.nearPlane = -2.43974
View3DAtts.farPlane = 2.43974
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.5, 0.5, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.710472, -0.456872, 0.535254)
View3DAtts.focus = (0.5, 0.5, 0)
View3DAtts.viewUp = (-0.619159, -0.0443206, 0.784014)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 1.21987
View3DAtts.nearPlane = -2.43974
View3DAtts.farPlane = 2.43974
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.5, 0.5, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.946513, -0.217165, 0.238648)
View3DAtts.focus = (0.5, 0.5, 0)
View3DAtts.viewUp = (-0.247491, -0.0140617, 0.968788)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 1.21987
View3DAtts.nearPlane = -2.43974
View3DAtts.farPlane = 2.43974
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.5, 0.5, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.8034, 0.363267, 0.471789)
View3DAtts.focus = (0.5, 0.5, 0)
View3DAtts.viewUp = (-0.447991, -0.153178, 0.880818)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 1.21987
View3DAtts.nearPlane = -2.43974
View3DAtts.farPlane = 2.43974
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.5, 0.5, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.855725, -0.0437144, 0.515581)
View3DAtts.focus = (0.5, 0.5, 0)
View3DAtts.viewUp = (-0.502408, 0.168165, 0.84812)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 1.21987
View3DAtts.nearPlane = -2.43974
View3DAtts.farPlane = 2.43974
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.5, 0.5, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.645006, -0.510103, 0.569002)
View3DAtts.focus = (0.5, 0.5, 0)
View3DAtts.viewUp = (-0.485416, 0.301585, 0.820621)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 1.21987
View3DAtts.nearPlane = -2.43974
View3DAtts.farPlane = 2.43974
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.5, 0.5, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

DrawPlots()

# we need to set this manually
# Set legend
plotName = GetPlotList().GetPlots(0).plotName
legend = GetAnnotationObject(plotName)
#legend.numberFormat = "%1.1f"
legend.managePosition = 0
legend.position = (0.02,0.81)
legend.fontFamily = legend.Times
legend.fontBold = 1
legend.fontItalic= 0
legend.fontHeight = 0.039
legend.drawMinMax = 1
legend.drawTitle =0
#legend.minFlag, legend.maxFlag = 0, 0
legend.xScale = 0.7
legend.yScale = 1.5

# Save images of all timesteps and add each image filename to a list.
for state in range(TimeSliderGetNStates()):
   SetTimeSliderState(state)
   # Save the image
   SaveWindow()

quit()