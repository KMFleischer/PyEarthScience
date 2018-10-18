import ESMF
import numpy as np
import Ngl, Nio

#-- enable debug logging
mg = ESMF.Manager(debug=True)

#--  open file and read variables
f   =  Nio.open_file("../read_data/rectilinear_grid_3D.nc", "r")
var =  f.variables["t"][0,0,:,:]
lat =  f.variables["lat"][:]
lon =  f.variables["lon"][:]

var_shape = var.shape

print("------> var_shape: ",var_shape)

lat5  = np.arange(-90.0,95.0,5.0)
lon5  = np.arange(-180.0,185.0,5.0)
nlat5 = len(lat5)
nlon5 = len(lon5)

print("------------------------")
print(lat5)
print(lon5)
print(nlat5)
print(nlon5)

print("-- grid5 ----------------------")

grid5      = np.ndarray([nlat5,nlon5])
grid_shape = grid5.shape

print("------> grid_shape: ",grid_shape)

print("-- srcgrid ----------------------")

#srcgrid = ESMF.Grid(np.array(var_shape),staggerloc=ESMF.StaggerLoc.CENTER,\
srcgrid = ESMF.Grid(np.array([lat.size,lon.size]),\
                    staggerloc=ESMF.StaggerLoc.CENTER,\
                    coord_sys=ESMF.CoordSys.SPH_DEG)
                    
src_lon = srcgrid.get_coords(0)
src_lat = srcgrid.get_coords(1)
src_lon = lon
src_lat = lat

print(src_lat)
print(src_lon)

print("-- dstgrid ----------------------")

#dstgrid = ESMF.Grid(np.array(grid_shape),\
dstgrid = ESMF.Grid(np.array([lat5.size,lon5.size]),\
                    staggerloc=ESMF.StaggerLoc.CENTER,\
                    coord_sys=ESMF.CoordSys.SPH_DEG)

dst_lon = dstgrid.get_coords(0)
dst_lat = dstgrid.get_coords(1)
dst_lon = lon5
dst_lat = lat5

print(dst_lat)
print(dst_lon)

print("-- srcfield ----------------------")

srcfield = ESMF.Field(srcgrid, name="Temperature")

print(srcfield)

print("-- srcfield data ----------------------")

srcfield.data[:][:] = var

print(srcfield)

print("-- dstfield ----------------------")

dstfield = ESMF.Field(dstgrid, name="Temperature")

print("-- ESMF.Regrid ----------------------")

regrid = ESMF.Regrid(srcfield, dstfield, \
                     filename="esmpy_example_weight_file.nc",\
                     regrid_method=ESMF.RegridMethod.BILINEAR,\
                     unmapped_action=ESMF.UnmappedAction.ERROR)
                     
print("-- dstfield data ----------------------")

dstfield = regrid(srcfield,dstfield)

print(dstfield)


