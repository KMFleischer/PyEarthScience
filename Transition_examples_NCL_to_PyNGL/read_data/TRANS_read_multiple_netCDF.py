#
#  File:
#    TRANS_read_multiple_netCDF.py
#
#  Synopsis:
#    Illustrates how to read multiple netCDF files
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
#    This example shows how to read multiple netCDF files.
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
  Transition Guide Python Example:   TRANS_read_multiple_netCDF.py

   - read multiple netCDF files
   - retrieve variable informations

  2018-08-31  kmf
"""
from __future__ import print_function
import netCDF4 as nc

#-- list of files
file_list  = "file_*.nc"

#-- open file
f = nc.MFDataset(file_list)

#-- read variable
var = f.variables['tsurf']
print(var.dimensions)

#-- read dimension time variable
time = f.variables['time']
print(time[:])

#-- read dimensions lat and lon variables
lat = f.variables['lat']
print(lat[:])

lon = f.variables['lon']
print(lon[:])

exit()

