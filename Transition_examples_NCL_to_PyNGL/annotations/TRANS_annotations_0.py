#
#  File:
#    TRANS_annotations_0.py
#
#  Synopsis:
#    Illustrates how to change the axis annotations
#
#  Categories:
#    xy plot
#    tm-resources
#    ti-resources
#
#  Author:
#    Karin Meier-Fleischer, based on NCL example
#  
#  Date of initial publication:
#    September 2018
#
#  Description:
#    This example shows how to change the axis annotations.
#
#  Effects illustrated:
#    o  Drawing a xy plot
#    o  Changing the tickmark and axis label resources
# 
#  Output:
#    A single visualization is produced.
#
#  Notes: The data for this example can be downloaded from 
#    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
#   
'''
  Transition Guide Python Example:   TRANS_annotations_0.py

  -  Creating xy-plot
  -  Changing axis annotations
  -  Changing axis tickmarks

  2018-09-10  kmf
'''
from __future__ import print_function
import numpy as np
import Ngl

#--  define x and y variables
x = [  0.0, 10.0, 20.0, 30.0, 40.0, \
      50.0, 60.0, 70.0, 80.0, 90.0, 100.0]
y = [  0.1,  0.7,  1.0,  0.8,  0.75, \
       0.5,  0.6,  0.62, 0.61, 0.59,  0.4]

xmin = min(x)
xmax = max(x)
ymin = min(y)
ymax = max(y)

#-- x-axis spacing value, values and labels
xvalues = np.arange(0,120,20)     #-- define x-axis labels
xlabels = xvalues.astype('str')   #-- convert to type string
xlabels = [xl + "~S~o~N~E" for xl in xlabels] #-- add 'oE'
  
#-- open a workstation
wkres =  Ngl.Resources()
wks   =  Ngl.open_wks("png","plot_TRANS_anno_0_py",wkres)

#-- set resources
res =  Ngl.Resources()            #-- generate an res object for plot

res.xyLineThicknessF =  4.0       #-- line width
res.xyLineColor      = "springgreen4"   #-- line color
res.xyDashPattern    =  3         #-- line patter 3: dash-dot-dash

res.tiXAxisFont      = 22
res.tiXAxisFontHeightF = 0.014
res.tiXAxisString    = "longitudes"#-- x-axis title
res.tiYAxisFont      = 22
res.tiYAxisFontHeightF = 0.014
res.tiYAxisString    = "data"     #-- y-axis title

res.trXMinF          = xmin - 2.  #-- x-axis min value
res.trXMaxF          = xmax + 2.  #-- x-axis max value
res.trYMinF          = ymin - .1  #-- y-axis min value
res.trYMaxF          = ymax + .1  #-- y-axis max value

#-- x-axis tickmark resources
res.tmXBMode         = "Explicit" #-- set x-axis labeling to explicit
res.tmXBValues       =  xvalues   #-- values for x-axis tickmarks
res.tmXBLabels       =  xlabels   #-- set labels equal to values (type string)
res.tmXBLabelFontColor = "blue"   #-- x-axis label color
res.tmXBLabelFontHeightF = 0.012  #-- x-axis font size

res.tmXBMajorLineColor  = "blue"  #-- bottom x-axis major tickmark color
res.tmXBMinorLineColor  = "blue"  #-- bottom x-axis minor tickmark color
res.tmXBMajorThicknessF =  2.     #-- bottom x-axis major tickmarks thickness
res.tmXBMinorThicknessF =  2.     #-- bottom x-axis minor tickmarks thickness

#-- draw the tick marks outward the plot
res.tmXBMajorOutwardLengthF = 0.02
res.tmXTMajorOutwardLengthF = 0.02
res.tmXBMinorOutwardLengthF = 0.01
res.tmXTMinorOutwardLengthF = 0.01

#-- y-axis resources
res.tmYLLabelFontColor = "red"#-- x-axis label color
res.tmYLLabelFontHeightF = 0.012  #-- x-axis font size

res.tmYLMajorLineColor  = "red"   #-- bottom x-axis major tickmark color
res.tmYLMinorLineColor  = "red"   #-- bottom x-axis minor tickmark color
res.tmYLMajorThicknessF =  2.     #-- bottom x-axis major tickmarks thickness
res.tmYLMinorThicknessF =  2.     #-- bottom x-axis minor tickmarks thickness

#-- draw the tick marks outward the plot
res.tmYLMajorOutwardLengthF = 0.02
res.tmYRMajorOutwardLengthF = 0.02
res.tmYLMinorOutwardLengthF = 0.01
res.tmYRMinorOutwardLengthF = 0.01

#-- draw the plot
plot = Ngl.xy(wks,x,y,res)

#-- done
Ngl.end()
