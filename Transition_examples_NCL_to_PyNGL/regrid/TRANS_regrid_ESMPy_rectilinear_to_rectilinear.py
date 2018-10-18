#
#  File:
#    TRANS_regrid_ESMPy_rectilinear_to_rectilinear.py
#
#  Synopsis:
#    Illustrates how to create a contour fill plot on a map
#
#  Categories:
#    contour plot
#    map plot
#
#  Author:
#    Karin Meier-Fleischer, based on NCL example
#  
#  Date of initial publication:
#    October 2018
#
#  Description:
#    This example shows how to create a contour fill plot on a map.
#
#  Effects illustrated:
#    o  Drawing a contour fill plot
#    o  Drawing a map
# 
#  Output:
#    Two visualizations are produced, original data and regridded data.
#
#  Notes: The data for this example can be downloaded from 
#    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
#   
'''
  Transition Guide Python Example: 	TRANS_regrid_ESMPy_rectilinear_to_rectilinear.py

  - read netCDF file
  - regrid to higher resolution grid 
  - drawing contour fill plots
  - drawing a map
  
  18-10-15  kmf
'''
from __future__ import print_function
import numpy as np
import xarray as xr
import ESMF
import Ngl

#--  open file and read variables
print("---- xarray: lat lon ----")

data = xr.open_dataset("../read_data/rectilinear_grid_3D.nc")

print("---- xarray: data t ----")

t   = data['t'][0,0,:,:]
lat = np.array(data['lat'][:])
lon = np.array(data['lon'][:])
#print(data['lat'].values)
#print(data['lon'].values)
#print(data['t'].values)

print("---- xarray: dstgrid ----")

dst_lat = np.arange(-89.5,89.5,1.0)
dst_lon = np.arange(-179.4,179.5,1.0)

#dstgrid = xr.Dataset({'lat': (['lat'], dst_lat),
#                      'lon': (['lon'], dst_lon),})
dstgrid = ESMF.Grid(np.array([dst_lat.size,dst_lon.size]),\
                    staggerloc=ESMF.StaggerLoc.CENTER,\
                    coord_sys=ESMF.CoordSys.SPH_DEG)
print(dstgrid)

print("---- xarray: regrid data set ----")

srcgrid = ESMF.Grid(np.array([lat.size,lon.size]),\
                    staggerloc=ESMF.StaggerLoc.CENTER,\
                    coord_sys=ESMF.CoordSys.SPH_DEG)
srcfield = ESMF.Field(srcgrid, name="Temperature")
srcfield.data[:][:] = t

dstfield = ESMF.Field(dstgrid, name="Temperature")

regridder = ESMF.Regrid(srcfield, dstfield, \
                     filename="esmpy_example_weight_file.nc",\
                     regrid_method=ESMF.RegridMethod.BILINEAR,\
                     unmapped_action=ESMF.UnmappedAction.ERROR)
print(regridder)                           #-- print basic regridder information

print("---- xarray: retrieve regridded variable t_regrid ----")

t_regrid = regridder(t)
#print(t_regrid[:,:])

print("---- xarray: retrieve regridded variable lat_regrid, lon_regrid ----")

lat_regrid = regridder(t).lat
lon_regrid = regridder(t).lon
#print(lat_regrid[:])
#print(lon_regrid[:])

print("---- plotting ----")
wks = Ngl.open_wks("png","plot_TRANS_regrid_ESMPy_py")

res                 =  Ngl.Resources()
res.nglFrame        =  False
res.cnFillOn        =  True
res.cnFillPalette   = "NCL_default"
res.cnLineLabelsOn  =  False
res.cnLevelSelectionMode = "ManualLevels"   #-- use manual contour line levels
res.cnMinLevelValF  =  235.0                #-- contour min. value
res.cnMaxLevelValF  =  310.0                #-- contour max. value
res.cnLevelSpacingF =    5.0                #-- contour interval
res.lbOrientation   = "horizontal"

res.sfXArray        =  dst_lon
res.sfYArray        =  dst_lat

plot = Ngl.contour_map(wks,t_regrid,res)

Ngl.frame(wks)

res.sfXArray        =  lon
res.sfYArray        =  lat

plot = Ngl.contour_map(wks,t,res)

Ngl.frame(wks)

print("---- clean-up ----")
regridder.clean_weight_file()

