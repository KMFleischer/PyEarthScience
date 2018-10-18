#
#  File:
#    TRANS_streamline.py
#
#  Synopsis:
#    Illustrates how to create a streamline plot
#
#  Categories:
#    streamline plot
#
#  Author:
#    Karin Meier-Fleischer, based on NCL example
#  
#  Date of initial publication:
#    September 2018
#
#  Description:
#    This example shows how to create a streamline plot.
#
#  Effects illustrated:
#    o  Read netCDF data
#    o  Drawing a streamline plot
# 
#  Output:
#    A single visualization is produced.
#
#  Notes: The data for this example can be downloaded from 
#    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
#   
'''
  Transition Guide PyNGL Example: TRANS_streamline.py

  -  Read netCDF data
  -  Drawing a streamline plot
  
  18-09-04  kmf
'''
from __future__ import print_function
import Ngl,Nio

#-- open a file and read variables
f    = Nio.open_file("../read_data/rectilinear_grid_2D.nc", "r")

u    = f.variables["u10"]
v    = f.variables["v10"]
ua   = f.variables["u10"][0,:,:]
va   = f.variables["v10"][0,:,:]

lat  = f.variables["lat"]
lon  = f.variables["lon"]
nlon = len(lon)
nlat = len(lat)

#-- open a workstation
wks = Ngl.open_wks("png","plot_TRANS_streamline_py")

#-- resource settings
stres                  =  Ngl.Resources()
stres.nglFrame         =  False

stres.vfXArray         =  lon[::3]
stres.vfYArray         =  lat[::3]
  
stres.mpFillOn         =  True
stres.mpOceanFillColor = "Transparent"
stres.mpLandFillColor  = "Gray90"
stres.mpInlandWaterFillColor = "Gray90"

#-- create the plot
plot = Ngl.streamline_map(wks,ua[::3,::3],va[::3,::3],stres)

#-- write variable long_name and units to the plot
txres               = Ngl.Resources()
txres.txFontHeightF = 0.014

Ngl.text_ndc(wks,f.variables["u10"].attributes['long_name'],0.16,0.76,txres)
Ngl.text_ndc(wks,f.variables["u10"].attributes['units'],    0.95,0.76,txres)

#-- advance the frame
Ngl.frame(wks)

Ngl.end()

