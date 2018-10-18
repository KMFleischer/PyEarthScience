#
#  File:
#    TRANS_read_ASCII_lat_lon_value_way2.py
#
#  Synopsis:
#    Illustrates how to read an ASCII file and create a 
#    contour fill plot on a map
#
#  Categories:
#    I/O
#    contour plot
#    map plot
#
#  Author:
#    Karin Meier-Fleischer, based on NCL example
#  
#  Date of initial publication:
#    September 2018
#
#  Description:
#    This example shows how to read an ASCII file and 
#    create a contour fill plot on a map.
#
#  Effects illustrated:
#    o  Read ASCII data
#    o  Drawing contours
#    o  Drawing a map
# 
#  Output:
#    -
#
#  Notes: The data for this example can be downloaded from 
#    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
#   
"""
  Transition Guide Python Example:   TRANS_read_ASCII_lat_lon_value_way2.py

   based on read_asc6.ncl: http://ncl.ucar.edu/Applications/Scripts/read_asc6.ncl
   
   - read ASCII file asc6.txt
   - retrieve variable informations
   - draw contours on a map

	asc6.txt
	
    Lat     Lon     Temp (C)
    33.3    76.5    20.3
    33.3    76.6    20.3
    33.3    76.7    21.5
    33.3    76.8    20.0
	.....
	
  2018-08-27  kmf
"""
from __future__ import print_function
import numpy as np

print("")

#-- read the data

f      = open("asc6.txt",'r')
data   = f.readlines()                          #-- data: type list

nrows  = len(data)

#-- assign lists to append elements

lat0 = []
lon0 = []
vals = []

for i in data[1::]:
	line = i.strip()
	print(line)
	cols = line.split()
	lat0.append(cols[0])
	lon0.append(cols[1])
	vals.append(cols[2])

#-- convert string to float
print(len(lat0))
print(len(lon0))
print(len(vals))

lat0   = np.array(lat0).astype(float)
lon0   = np.array(lon0).astype(float)
temp1d = np.array(vals).astype(float)

indeqlat = np.array(np.where(lat0 == lat0[0]))
print(type(indeqlat))

nlons    = indeqlat.shape                       #-- number of longitudes
nlons    = nlons[1]                             #-- number of longitudes
nlats    = nrows / nlons                        #-- number of latitude

lat = lat0[::nlons]
lon = lon0[0:nlons]

#setattr(lat, 'units', 'degrees_north')
#setattr(lon, 'units', 'degrees_east')

#-- rows by column

print("--> nlats:            " + str(len(lat)))
print("--> nlons:            " + str(len(lon)))
print("--> rank of vals:     " + str(len(temp1d.shape)))
print("--> shape temp1d:     " + str(temp1d.shape))

temp2d = np.reshape(temp1d,(nlats,nlons))

#setattr(temp2d, 'units', 'degC')
#setattr(telp2d, 'long_name', 'temperature')

print("--> shape temp2d:     " + str(temp2d))
print("--> shape temp2d:     " + str(temp2d.shape))

exit()

