#
#  File:
#    TRANS_read_netCDF.py
#
#  Synopsis:
#    Illustrates how to read a netCDF file
#
#  Categories:
#    I/O
#
#  Author:
#    Karin Meier-Fleischer, based on NCL example
#  
#  Date of initial publication:
#    September 2018
#
#  Description:
#    This example shows how to read a netCDF file.
#
#  Effects illustrated:
#    o  Read netCDF data
# 
#  Output:
#    -
#
#  Notes: The data for this example can be downloaded from 
#    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
#   
"""
  Transition Guide Python Example:   TRANS_read_netCDF.py

   - read netCDF file
   - retrieve variable informations

  2018-08-21  kmf
"""
from __future__ import print_function
import Ngl,Nio

print("")

#--  data file name
fname  = "./rectilinear_grid_3D.nc"

#--  open file
f = Nio.open_file(fname, "r")

#-- get the sizes of all dimensions in the same order as the names
dims = f.dimensions.values()
print("--> Dimensions:              "+ str(dims))

#-- retrive the dimension names of the file
dimnames = f.dimensions.keys()
print("--> Dimension names of file: "+ str(dimnames))

#-- get only the variable names not the dimension names
varnames = f.variables.keys()
print ("--> Variable names:         "+ str(varnames))

var_list = [i for i in varnames if i not in dimnames]
print ("--> Variables:              "+ str(var_list))
print("")

#-- read variable, first time step
var = f.variables["t"]

#-- get type, rank, shape, dimension names and attributes of the variable
type  = var.typecode()
shape = var.shape
attr  = var.attributes.keys()
dims  = var.dimensions
rank  = var.rank

print("")
print("--> Type:        "+ str(type))
print("--> Shape:       "+ str(shape))
print("--> Attributes:  "+ str(attr))
print("--> Dimensions:  "+ str(dims))
print("--> Rank:        "+ str(rank))
print("")

#-- print variable lat content
lat = f.variables["lat"]
lon = f.variables["lon"]
print(lat)
print(lon)

#-- check if variable has attribute

if hasattr(lon,'units'):
	print("--> Has units attribute: "+var.attributes['units'])

exit()

