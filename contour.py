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

# Begin spontaneous state
View2DAtts = View2DAttributes()
#left,right,bottom, top
View2DAtts.windowCoords = (0.005, 0.995, 0.005, 0.995)
#adjust (left, right, bottom, top)  to move
View2DAtts.viewportCoords = (0.15, 0.95, 0.15, 0.9)
# Here changing the third value changes the right border space
#View2DAtts.viewportCoords = (0.24, 0.9, 0.3, 0.95) 
View2DAtts.fullFrameActivationMode = View2DAtts.Auto  # On, Off, Auto
View2DAtts.fullFrameAutoThreshold = 100
View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.windowValid = 1
SetView2D(View2DAtts)
# End spontaneous state

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

# Customize x-axis and y-axis labels
a = AnnotationAttributes()
# Customize x-axis 
a.axes2D.xAxis.title.visible = 0  # (0,1): Disable/enable display of axis title
a.axes2D.xAxis.title.visible = 1
a.axes2D.xAxis.title.font.font = a.axes2D.xAxis.title.font.Times  # Arial, Courier, Times
a.axes2D.xAxis.title.font.scale = 2.2
a.axes2D.xAxis.title.font.useForegroundColor = 1
a.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
a.axes2D.xAxis.title.font.bold = 1
a.axes2D.xAxis.title.font.italic = 1
a.axes2D.xAxis.title.userTitle = 1
a.axes2D.xAxis.title.userUnits = 1
a.axes2D.xAxis.title.title = "x"
a.axes2D.xAxis.title.units = ""

# Customize  y-axis labels
a.axes2D.yAxis.title.visible = 1
a.axes2D.yAxis.title.font.font = a.axes2D.yAxis.title.font.Times  # Arial, Courier, Times
a.axes2D.yAxis.title.font.scale = 2.2
a.axes2D.yAxis.title.font.useForegroundColor = 1
a.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
a.axes2D.yAxis.title.font.bold = 1
a.axes2D.yAxis.title.font.italic = 1
a.axes2D.yAxis.title.userTitle = 1
a.axes2D.yAxis.title.userUnits = 1
a.axes2D.yAxis.title.title = "y"
a.axes2D.yAxis.title.units = ""

a.axes2D.xAxis.label.visible = 1
a.axes2D.yAxis.label.visible = 1
a.axes2D.xAxis.label.font.font = a.axes2D.xAxis.label.font.Times
a.axes2D.xAxis.label.font.italic = 0
a.axes2D.xAxis.label.font.bold = 1
a.axes2D.xAxis.label.font.scale = 1.5

a.axes2D.yAxis.label.font.font = a.axes2D.yAxis.label.font.Times
a.axes2D.yAxis.label.font.italic = 0
a.axes2D.yAxis.label.font.bold = 1
a.axes2D.yAxis.label.font.scale = 1.5

a.axes2D.autoSetTicks = 0  # Disable automatic tick placement

a.axes2D.xAxis.tickMarks.visible = 1  # Ensure tick marks are visible
a.axes2D.xAxis.tickMarks.majorMinimum =0.0  # Set minimum value for major ticks
a.axes2D.xAxis.tickMarks.majorMaximum = 1.0   # Set maximum value for major ticks
a.axes2D.xAxis.tickMarks.majorSpacing = 0.2   # Set spacing between major ticks
a.axes2D.xAxis.tickMarks.minorSpacing = 0.1   # Set spacing between major ticks

a.axes2D.yAxis.tickMarks.visible = 1  # Ensure tick marks are visible
a.axes2D.yAxis.tickMarks.majorMinimum = 0.0  # Set minimum value for major ticks
a.axes2D.yAxis.tickMarks.majorMaximum = 1.0   # Set maximum value for major ticks
a.axes2D.yAxis.tickMarks.majorSpacing = 0.2   # Set spacing between major ticks
a.axes2D.yAxis.tickMarks.minorSpacing = 0.1   # Set spacing between major ticks


a.userInfoFlag = 0                # disables username display
a.databaseInfoFlag = 0            # diables database display

AddPlot("Contour", variable)
SetAnnotationAttributes(a)

c = ContourAttributes()
c.lineWidth = 1                    # Set line width of contours from here
c.colorType = 1                    # (0, 1): This selects color by (single,     multiple) color/s:
#c.singleColor = (0, 0, 0, 255)     # This combination is for black color
c.contourNLevels = 40              # Set number of contour levels from here.
c.legendFlag = 1                   # (0, 1): Disable/enable display of legend   for contours
#c.minFlag, c.maxFlag = 1, 1
#c.min, c.max = 0.1, 1.8
SetPlotOptions(c)



DrawPlots()  # position of the line is important

# Set legend
plotName = GetPlotList().GetPlots(0).plotName
legend = GetAnnotationObject(plotName)
legend.numberFormat = "%1.2f"   # turn this on to print only decimals like 0.1, 0.2, etc
legend.managePosition = 0
legend.position = (0.85, 0.9) 
legend.fontFamily = legend.Times
legend.fontBold = 1
legend.fontItalic= 0
legend.fontHeight = 0.049
legend.drawMinMax = 0
legend.drawTitle =0
#legend.minFlag, legend.maxFlag = 0, 0
legend.xScale = 0.75
legend.yScale = 2.88

# Save images of all timesteps and add each image filename to a list.
for state in range(TimeSliderGetNStates()):
   SetTimeSliderState(state)
   # Save the image
   SaveWindow()

quit()
