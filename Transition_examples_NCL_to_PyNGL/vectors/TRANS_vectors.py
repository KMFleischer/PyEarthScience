#
#  File:
#    TRANS_vectors.py
#
#  Synopsis:
#    Illustrates how to create a vector plot
#
#  Categories:
#    vector plot
#
#  Author:
#    Karin Meier-Fleischer, based on NCL example
#  
#  Date of initial publication:
#    September 2018
#
#  Description:
#    This example shows how to create a vector plot.
#
#  Effects illustrated:
#    o  Read netCDF data
#    o  Drawing a vector plot
# 
#  Output:
#    A single visualization is produced.
#
#  Notes: The data for this example can be downloaded from 
#    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
#   
'''
  Transition Guide PyNGL Example: TRANS_vectors.py

  -  Read netCDF data
  -  Drawing a vector plot
  
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
wks = Ngl.open_wks("png","plot_TRANS_vectors_py")

#-- resource settings
vcres                  =  Ngl.Resources()
vcres.nglFrame         =  False

vcres.vfXArray         =  lon[::3]
vcres.vfYArray         =  lat[::3]

vcres.vcMinFracLengthF =  0.3           #-- length of smallest vector
vcres.vcRefLengthF     =  0.05          #-- length of reference vector
vcres.vcRefMagnitudeF  =  20.0          #-- define vector ref mag
vcres.vcRefLengthF     =  0.035         #-- define length of vec ref  
  
vcres.mpFillOn         =  True
vcres.mpOceanFillColor = "Transparent"
vcres.mpLandFillColor  = "Gray90"
vcres.mpInlandWaterFillColor = "Gray90"

#-- create the plot
plot = Ngl.vector_map(wks,ua[::3,::3],va[::3,::3],vcres)

#-- write variable long_name and units to the plot
txres               = Ngl.Resources()
txres.txFontHeightF = 0.014

Ngl.text_ndc(wks,f.variables["u10"].attributes['long_name'],0.16,0.8,txres)
Ngl.text_ndc(wks,f.variables["u10"].attributes['units'],    0.95,0.8,txres)

#-- advance the frame
Ngl.frame(wks)

Ngl.end()

