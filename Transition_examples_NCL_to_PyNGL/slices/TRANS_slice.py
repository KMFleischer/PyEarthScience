#
#  File:
#    TRANS_slice.py
#
#  Synopsis:
#    Illustrates how to create a slice plot
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
#    This example shows how to create a slice plot.
#
#  Effects illustrated:
#    o  Read netCDF data
#    o  Drawing a slice plot
# 
#  Output:
#    A single visualization is produced.
#
#  Notes: The data for this example can be downloaded from 
#    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
#   
'''
  Transition Guide PyNGL Example: TRANS_slice.py

  -  Read netCDF data
  -  Drawing a slice plot
  
  18-09-04  kmf
'''
from __future__ import print_function
import numpy as np
import Ngl,Nio

#--  define variables
fname  = "../read_data/rectilinear_grid_3D.nc"  #-- data file name

#--  open file and read variables
f    =  Nio.open_file(fname,"r")         #-- open data file
t    =  f.variables["t"][0,:,::-1,:]     #-- first time step, reverse latitude
lev  =  f.variables["lev"][:]            #-- all levels
lat  =  f.variables["lat"][::-1]         #-- reverse latitudes
lon  =  f.variables["lon"][:]            #-- all longitudes
nlat =  len(lat)                         #-- number of latitudes

longname = f.variables["t"].attributes['long_name']
units    = f.variables["t"].attributes['units']

ind40    = 69                            #-- index close to lat 40 degrees
t40      = t[:,ind40,:]                  #-- variable at lat ~40 degrees
strlat40 = lat[ind40]                    #-- retrieve data of lat ~40 degrees

#-- open a workstation
wks =  Ngl.open_wks("png","plot_TRANS_slice_py")

#-- set resources
res                 =  Ngl.Resources()   #-- generate an res object for plot
res.nglFrame        =  False

#-- viewport resources
res.vpXF            =  0.1               #-- start x-position of viewport
res.vpYF            =  0.9               #-- start y-position of viewport
res.vpWidthF        =  0.7               #-- width of viewport
res.vpHeightF       =  0.6               #-- height of viewport

#-- contour resources
res.cnFillOn        =  True              #-- turn on contour fill
res.cnFillPalette   = "temp_diff_18lev"
res.cnLineLabelsOn  =  False             #-- turn off line labels
res.cnInfoLabelOn   =  False             #-- turn off info label
res.cnLevelSelectionMode = "ManualLevels"#-- select manual levels
res.cnMinLevelValF  =  200.              #-- minimum contour value
res.cnMaxLevelValF  =  290.              #-- maximum contour value
res.cnLevelSpacingF =  5.                #-- contour increment

res.tiYAxisString   =  longname+"  [hPa]"

#-- grid resources
res.sfXArray        =  lon               #-- scalar field x
res.sfYArray        =  lev/100               #-- scalar field y

#-- reverse y-axis
res.trYReverse      =  True              #-- reverse the Y axis
res.nglYAxisType    = "LogAxis"          #-- y axis log

#-- draw slice contour plot
plot = Ngl.contour(wks,t40,res)

#-- write variable long_name and units to the plot
txres               = Ngl.Resources()
txres.txFontHeightF = 0.014

Ngl.text_ndc(wks,longname,0.18,0.81,txres)
Ngl.text_ndc(wks,units,   0.77,0.81,txres)

#-- advance the frame
Ngl.frame(wks)

#-- done
Ngl.end()
