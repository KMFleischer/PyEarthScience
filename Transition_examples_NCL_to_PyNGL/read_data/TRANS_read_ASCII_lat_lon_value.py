#
#  File:
#    TRANS_read_ASCII_lat_lon_value.py
#
#  Synopsis:
#    Illustrates how to read an ASCII file
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
#    This example shows how to read an ASCII file.
#
#  Effects illustrated:
#    o  Read ASCII data
# 
#  Output:
#    -
#
#  Notes: The data for this example can be downloaded from 
#    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
#   
"""
  Transition Guide Python Example:   TRANS_read_ASCII_lat_lon_value.py
   
   - read ASCII file asc6.txt
   - retrieve variable informations

  Input file: asc6.txt
	
    Lat     Lon     Temp (C)
    33.3    76.5    20.3
    33.3    76.6    20.3
    33.3    76.7    21.5
    33.3    76.8    20.0
	.....
	
  2018-08-28  kmf
"""
from __future__ import print_function
import numpy as np
import Ngl

#-- file has 21361 lines but 1 header line
#-- 3 columns
nrows   = 21360                     #-- file has 21361 lines but 1 header line
ncols   =     3                     #-- file has 3 columns
num_lon =   240                     #-- number of longitudes
num_lat =    89                     #-- number of latitudes

#-- read all data
data = Ngl.asciiread("asc6.txt",(nrows,ncols),"float")

#-- select lat, lon and temp data
lat    = data[::num_lon,0]
lon    = data[:num_lon,1]
temp1D = data[:,2]

#-- size of lat, lon and temp1d
nlats  = len(lat)
nlons  = len(lon)
ntemp  = len(temp1D)

#-- reshape temp1d to 2D-array temp2d with size (89,240)
temp2D = np.reshape(temp1D,(nlats,nlons))

#-- print information
print("rank  temp1D: " + str(len(temp1D.shape)))
print("shape temp1D: " + str(ntemp))
print("rank  temp2D: " + str(len(temp2D.shape)))
print("shape temp2D: " + str(temp2D.shape))

exit()

