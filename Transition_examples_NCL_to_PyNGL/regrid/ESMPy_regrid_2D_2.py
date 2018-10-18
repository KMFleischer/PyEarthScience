import ESMF
import numpy as np
import Ngl, Nio

#-- enable debug logging
mg = ESMF.Manager(debug=True)

#--  open file and read variables
f   = Nio.open_file("../read_data/rectilinear_grid_3D.nc", "r")
var = f.variables["t"][0,0,:,:]
lat = f.variables["lat"][:]
lon = f.variables["lon"][:]

var_shape = var.shape
print("------> var_shape: ",var_shape)

[i_lat,i_lon] = [1,0]

#-- source grid
print("-- source grid --")

srcgrid = ESMF.Grid(np.array([lon.size, lat.size]),coord_sys=ESMF.CoordSys.SPH_DEG,staggerloc=ESMF.StaggerLoc.CENTER,num_peri_dims=1,periodic_dim=0,pole_dim=1)

#-- get and set the source grid coordinates
srcGridCoordLon = srcgrid.get_coords(i_lon)
srcGridCoordLat = srcgrid.get_coords(i_lat)

slons_par = lon[srcgrid.lower_bounds[ESMF.StaggerLoc.CENTER][0]:srcgrid.upper_bounds[ESMF.StaggerLoc.CENTER][0]]
slats_par = lat[srcgrid.lower_bounds[ESMF.StaggerLoc.CENTER][1]:srcgrid.upper_bounds[ESMF.StaggerLoc.CENTER][1]]

#-- destination grid
print("-- destination grid --")

lat5  = np.arange(-90.0,95.0,5.0)
lon5  = np.arange(-180.0,185.0,5.0)
nlat5 = len(lat5)
nlon5 = len(lon5)

print("-- lat5 lon5")
print(lat5)
print(lon5)
print(nlat5)
print(nlon5)

dstgrid = ESMF.Grid(np.array([lon5.size, lat5.size]),coord_sys=ESMF.CoordSys.SPH_DEG,staggerloc=ESMF.StaggerLoc.CENTER,num_peri_dims=1,periodic_dim=0,pole_dim=1)

#-- get and set the source grid coordinates.
dstGridCoordLon = dstgrid.get_coords(i_lon)
dstGridCoordLat = dstgrid.get_coords(i_lat)

dlons_par = lon5[dstgrid.lower_bounds[ESMF.StaggerLoc.CENTER][0]:dstgrid.upper_bounds[ESMF.StaggerLoc.CENTER][0]]
dlats_par = lat5[dstgrid.lower_bounds[ESMF.StaggerLoc.CENTER][1]:dstgrid.upper_bounds[ESMF.StaggerLoc.CENTER][1]]

print("-- srcfield ----------------------")

srcfield = ESMF.Field(srcgrid, name="Temperature")

print(srcfield)

print("-- srcfield data ----------------------")

srcfield.data[:,:] = np.swapaxes(var,0,1)

print(srcfield)

print("-- dstfield ----------------------")

dstfield = ESMF.Field(dstgrid, name="Temperature")

print("-- ESMF.Regrid ----------------------")

#regrid = ESMF.Regrid(srcfield, dstfield, \
#                     filename="esmpy_example_weight_file.nc",\
#                     regrid_method=ESMF.RegridMethod.BILINEAR,\
#                     unmapped_action=ESMF.UnmappedAction.ERROR)
#
regrid = ESMF.Regrid(srcfield, dstfield, \
                     regrid_method=ESMF.RegridMethod.BILINEAR, \
                     unmapped_action=ESMF.UnmappedAction.IGNORE)

         
print("-- dstfield data ----------------------")

dstfield = regrid(srcfield,dstfield)

print(dstfield)


