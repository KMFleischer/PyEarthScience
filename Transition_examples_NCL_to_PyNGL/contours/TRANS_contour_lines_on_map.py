#
#  File:
#    TRANS_contour_lines_on_map.py
#
#  Synopsis:
#    Illustrates how to create a contour line plot on a map
#
#  Categories:
#    contour plot
#    map plot
#
#  Author:
#    Karin Meier-Fleischer, based on NCL example
#  
#  Date of initial publication:
#    September 2018
#
#  Description:
#    This example shows how to create a contour line plot on a map.
#
#  Effects illustrated:
#    o  Drawing a contour line plot
#    o  Drawing a map
# 
#  Output:
#    A single visualization is produced.
#
#  Notes: The data for this example can be downloaded from 
#    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
#    
'''
  Transition Guide Python Example: 	TRANS_contour_lines_on_map.py

  - contour lines
  - map plot

  18-09-04  kmf
'''
from __future__ import print_function
import numpy as np
import Ngl,Nio

#--  open file and read variables
f    = Nio.open_file("../read_data/rectilinear_grid_3D.nc", "r")
var  = f.variables["t"][0,0,:,:]
lat  = f.variables["lat"][:]
lon  = f.variables["lon"][:]

#-- start the graphics
wks = Ngl.open_wks("png","plot_TRANS_contour_lines_on_map_py")

#-- resource settings
res                 =  Ngl.Resources()
res.nglFrame        =  False

res.sfXArray        =  lon
res.sfYArray        =  lat

res.mpFillOn        =  True
res.mpOceanFillColor = "Transparent"
res.mpLandFillColor = "Gray90"
res.mpInlandWaterFillColor = "Gray90"

#-- create the contour plot
plot = Ngl.contour_map(wks,var,res)

#-- write variable long_name and units to the plot
txres               = Ngl.Resources()
txres.txFontHeightF = 0.014

Ngl.text_ndc(wks,f.variables["t"].attributes['long_name'],0.14,0.78,txres)
Ngl.text_ndc(wks,f.variables["t"].attributes['units'],    0.95,0.78,txres)

#-- advance the frame
Ngl.frame(wks)

Ngl.end()
