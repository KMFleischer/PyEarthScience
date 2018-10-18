#
#  File:
#    TRANS_maps.py
#
#  Synopsis:
#    Illustrates how to create a map
#
#  Categories:
#    map plot
#
#  Author:
#    Karin Meier-Fleischer
#  
#  Date of initial publication:
#    September 2018
#
#  Description:
#    This example shows how to create a map.
#
#  Effects illustrated:
#    o  Drawing a map
# 
#  Output:
#    A single visualization is produced.
#
#  Notes: The data for this example can be downloaded from 
#    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
#   
'''
  Transition Guide Python Example: 	TRANS_maps.py

  - drawing a map
  
  18-09-03  kmf
'''
from __future__ import print_function
import Ngl

#-- open workstation
wks_type = "png"
wks = Ngl.open_wks(wks_type,"plot_TRANS_maps_py")

#-- which projection do we want to plot
projections = ["CylindricalEquidistant","Mollweide","Robinson","Orthographic"]

#-- resource settings
mpres              =  Ngl.Resources()   #-- resource object

mpres.vpWidthF     =  0.8               #-- make the aspect ratio square
mpres.vpHeightF    =  0.8

mpres.mpFillOn     =  True
mpres.mpOceanFillColor = "Transparent"
mpres.mpLandFillColor  = "Gray90"
mpres.mpInlandWaterFillColor = "Gray90"

for i in range(len(projections)):
	mpres.mpProjection = projections[i]
	mpres.tiMainString = projections[i]
	map = Ngl.map(wks,mpres)

Ngl.end()
