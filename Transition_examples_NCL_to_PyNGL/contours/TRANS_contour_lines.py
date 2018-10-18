#
#  File:
#    TRANS_contour_lines.py
#
#  Synopsis:
#    Illustrates how to create a contour line plot
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
#    This example shows how to create a contour line plot.
#
#  Effects illustrated:
#    o  Drawing a contour line plot
# 
#  Output:
#    A single visualization is produced.
#
#  Notes: The data for this example can be downloaded from 
#    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
#    
'''
  Transition Guide Python Example: 	TRANS_contour_lines.py

  - contour line plot

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
wks = Ngl.open_wks("png","plot_TRANS_contour_line_py")

#-- resource settings
res                    =  Ngl.Resources()
res.nglPointTickmarksOutward = True         #-- point tickmarks outward

#-- create the contour plot
plot = Ngl.contour(wks,T,res)

Ngl.end()
