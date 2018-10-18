#
#  File:
#    TRANS_overlay.py
#
#  Synopsis:
#    Illustrates how to draw a contour fill and a contour line plot over a map
#
#  Categories:
#    map plot
#    contour plot
#    overlay
#
#  Author:
#    Karin Meier-Fleischer, based on NCL example
#  
#  Date of initial publication:
#    September 2018
#
#  Description:
#    This example shows how to draw a contour fill and a contour line plot over a map.
#
#  Effects illustrated:
#    o  Read netCDF data
#    o  Drawing a map
#    o  Drawing a contour fill plot
#    o  Drawing a contour line plot
#    o  Using manual levels
#    o  Overlaying contour plots on a map
# 
#  Output:
#    A single visualization is produced.
#
#  Notes: The data for this example can be downloaded from 
#    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
#   
'''
  Transition Guide Python Example: TRANS_overlay.py
    
  -  Read netCDF data
  -  Drawing a map
  -  Drawing a contour fill plot
  -  Drawing a contour lines plot
  -  Using manual levels
  -  Overlaying contour plots on a map

  18-09-07  kmf
'''
from __future__ import print_function
import numpy as np
import Ngl,Nio

#--  open file and read variables
f    = Nio.open_file("../read_data/rectilinear_grid_3D.nc", "r")
t    = f.variables["t"][0,0,:,:]
rhum = f.variables["rhumidity"][0,0,:,:]
lat  = f.variables["lat"][:]
lon  = f.variables["lon"][:]

#-- define workstation
wks =  Ngl.open_wks("png","plot_TRANS_overlay_py")

#-- plot resources for the map
mpres                =  Ngl.Resources()
mpres.nglDraw        =  False              #-- don't draw plot
mpres.nglFrame       =  False              #-- don't advance frame
mpres.mpOutlineOn    =  True               #-- turn on map outlines
mpres.mpGeophysicalLineColor = "gray50"    #-- map outline color
mpres.mpLimitMode    = "LatLon"            #-- limit map via lat/lon
mpres.mpMinLatF      =  20.0               #-- min lat
mpres.mpMaxLatF      =  60.0               #-- max lat
mpres.mpMinLonF      = -10.0               #-- min lon
mpres.mpMaxLonF      =  40.0               #-- max lon

#-- plot resources for the temperature plot
tres                 =  Ngl.Resources()
tres.nglDraw         =  False              #-- don't draw plot
tres.nglFrame        =  False              #-- don't advance frame
tres.cnFillOn        =  True               #-- turn on color fill
tres.cnFillPalette   = "cmp_b2r"           #-- set the colormap to be used
tres.cnLinesOn       =  False              #-- turns off contour line labels
tres.cnLineLabelsOn  =  False              #-- turns off contour line labels
tres.cnInfoLabelOn   =  False              #-- turns off contour info label

tres.cnLevelSelectionMode = "ManualLevels" #-- select manual levels
tres.cnMinLevelValF  =  240.               #-- minimum contour value
tres.cnMaxLevelValF  =  310.               #-- maximum contour value
tres.cnLevelSpacingF =  2.                 #-- contour increment

tres.pmLabelBarOrthogonalPosF = -0.26 #-- move labelbar upward
tres.lbLabelFontHeightF =  0.009           #-- labelbar labe font size
tres.lbBoxMinorExtentF  =  0.17            #-- decrease height of labelbar box
tres.lbOrientation   = "horizontal"        #-- horizontal labelbar

tres.tiMainString    = "Colors: temperature, lines: rhumitity"
                                           #-- title string
tres.sfXArray        =  lon
tres.sfYArray        =  lat

#-- plot resources for the rhumidity plot
rres                 = Ngl.Resources()
rres.nglDraw         =  False              #-- don't draw plot
rres.nglFrame        =  False              #-- don't advance frame

rres.cnInfoLabelOrthogonalPosF = 0.13     #-- move info label upward

rres.sfXArray        =  lon
rres.sfYArray        =  lat

#-- generate tplot, but don't draw it yet
print("-- map --")
map   = Ngl.map(wks,mpres)

#-- generate tplot, but don't draw it yet
print("-- tplot --")
tplot = Ngl.contour(wks,t,tres)

#-- generate plot2, but don't draw it yet
print("-- rplot --")
rplot = Ngl.contour(wks,rhum,rres)

#-- overlay rplot on tplot
print("-- overlay tplot --")
Ngl.overlay(map, tplot)
print("-- overlay rplot --")
Ngl.overlay(map, rplot)

#-- draw the plot
Ngl.draw(map)

#-- write variable long_name and units to the plot
txres               = Ngl.Resources()
txres.txFontHeightF = 0.014
Ngl.text_ndc(wks,f.variables["t"].attributes['long_name'],0.17,0.88,txres)
Ngl.text_ndc(wks,f.variables["t"].attributes['units'],    0.95,0.88,txres)

#-- advance the frame
Ngl.frame(wks)
