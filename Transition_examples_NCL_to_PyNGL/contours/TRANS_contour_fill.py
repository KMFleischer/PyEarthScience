#
#  File:
#    TRANS_contour_fill.py
#
#  Synopsis:
#    Illustrates how to create a contour fill plot
#
#  Categories:
#    contour plot
#
#  Author:
#    Karin Meier-Fleischer, based on NCL example
#  
#  Date of initial publication:
#    September 2018
#
#  Description:
#    This example shows how to create a contour fill plot.
#
#  Effects illustrated:
#    o  Drawing a contour fill plot
# 
#  Output:
#    A single visualization is produced.
#
#  Notes: The data for this example can be downloaded from 
#    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
#    
'''
  Transition Guide Python Example: 	TRANS_contour_fill.py

  - contour fill plot

  18-09-03  kmf
'''
from __future__ import print_function
import numpy as np
import Ngl

#-- create some dummy data to contour
T    = np.zeros((25,25),'f')
jspn = np.power(np.arange(-12,13),2)
ispn = np.power(np.arange(-12,13),2)

for i in range(0,len(ispn)):
	T[i,:] = (jspn + ispn[i]).astype('f')

T = 100.0 - np.sqrt(64 * T)

#-- start the graphics
wks = Ngl.open_wks("png","plot_TRANS_contour_fill_py")

#-- resource settings
res                    =  Ngl.Resources()
res.nglDraw            =  False           #-- don't draw plot
res.nglFrame           =  False           #-- don't advance the frame
res.nglPointTickmarksOutward = True       #-- point tickmarks outward

res.cnFillOn           =  True            #-- turn on contour level fill
res.cnLineLabelsOn     =  False           #-- turn off contour line labels
res.cnFillPalette      = "ncl_default"

res.lbLabelPosition    = "Center"
res.lbLabelFontHeightF =  0.018           #-- make labelbar labels smaller
res.lbLabelAlignment   = "BoxCenters"
res.lbLabelStrings     =  list(range(-30,110,10)) #-- doesn't appear to work

#-- create the contour plot
plot = Ngl.contour(wks,T,res)

#-- bug work-around (v1.5.2): apply the labels after the plot has been created
nrlist                   =  Ngl.Resources()
nrlist.lbLabelStrings    =  list(range(-30,110,10))
Ngl.set_values(plot,nrlist)

#-- draw the plot and advance the frame
Ngl.draw(plot)
Ngl.frame(wks)

Ngl.end()
