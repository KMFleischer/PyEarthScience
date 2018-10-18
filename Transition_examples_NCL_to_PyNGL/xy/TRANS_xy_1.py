#
#  File:
#    TRANS_xy_1.py
#
#  Synopsis:
#    Illustrates how to create a xy plot
#
#  Categories:
#    xy plot
#    lg-resources
#    pm-resources
#
#  Author:
#    Karin Meier-Fleischer, based on NCL example
#  
#  Date of initial publication:
#    September 2018
#
#  Description:
#    This example shows how to create a xy plot.
#
#  Effects illustrated:
#    o  Drawing an xy plot
#    o  Using explicit line labels
#    o  Changing the legend settings
# 
#  Output:
#    A single visualization is produced.
#
#  Notes: The data for this example can be downloaded from 
#    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
#   
'''
  Transition Guide Python Example: TRANS_xy_1.py

  -  Drawing an xy plot
  -  Using explicit line labels
  -  Changing the legend settings

  18-08-31  kmf
'''
from __future__ import print_function
import numpy
import Ngl

#--  define x and y variables
x = [10., 20., 30., 40., 50., 60., 70., 80., 90.]
y = numpy.array([[0., 0.7, 1., 0.7, 0., -0.7, -1., -0.7, 0.],  \
                 [2., 2.7, 3., 2.7, 2.,  1.3,  1.,  1.3, 2.],  \
                 [4., 4.7, 5., 4.7, 4.,  3.3,  3.,  3.3, 4.]],'f')
                 
#-- open a workstation
wkres           =  Ngl.Resources()            #-- generate an resources object for workstation
wks_type        = "png"                       #-- output type of workstation
wks             =  Ngl.open_wks(wks_type,"plot_TRANS_xy_1_py",wkres)

#-- set resources
res                  =  Ngl.Resources()       #-- generate an res object for plot
res.tiXAxisString    = "x-values"             #-- x-axis title
res.tiYAxisString    = "y-values"             #-- y-axis title

#-- xy-plot resources
res.xyLineColors     = ["red","green","blue"] #-- set 3 different colors for lines
res.xyLineThicknessF =  3.0                   #-- line thickness for all
res.xyExplicitLegendLabels = ["t1","t2","t3"] #-- set explicit legend labels

#-- legend resources
res.pmLegendDisplayMode = "Always"            #-- turn on the drawing
res.pmLegendZone     =  0                     #-- legend zone: 0 = topLeft; 6 = topRight
res.pmLegendOrthogonalPosF =  0.32            #-- move the legend upwards
res.lgJustification  = "BottomRight"          #-- legend justification
res.pmLegendWidthF   =  0.2                   #-- change width
res.pmLegendHeightF  =  0.10                  #-- change height
res.pmLegendSide     = "Top"                  #-- Change location
res.lgPerimOn        =  False                 #-- turn off the perimeter

#-- draw the plot
plot = Ngl.xy(wks,x,y,res)

#-- done
Ngl.end()
