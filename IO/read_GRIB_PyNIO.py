#
#  File:
#    read_GRIB_with_PyNIO.py
#
#  Synopsis:
#    Illustrates how to read a GRIB file with PyNIO.
#
#  Description:
#    This example shows how to read a GRIB file using PyNIO.
#
#  Author:
#    Karin Meier-Fleischer
#  
#  Date of initial publication:
#    September, 2019
#
'''
  PyEarthScience:   read_GRIB_with_PyNIO.py

  Description:
    Demonstrate the use of PyNIO to open and read the content of
    a GRIB file. 

  - PyNIO
  - GRIB
  
  2019-01-22  kmf
'''

from __future__ import print_function
import Ngl,Nio
import numpy as np

#-- data directory and file name, we use an example GRIB file from the NCL package
ncarg  = Ngl.pynglpath("data")
fname  = ncarg+'/grb/MET9_IR108_cosmode_0909210000.grb2'

#--  open file
ds = Nio.open_file(fname, "r")

print('------------------------------------------------------')
print()
print('--> ds:              ', ds)
print()

#-- print the size and shape of the variable
print('------------------------------------------------------')
print()
print('--> ds.dimensions            ',ds.dimensions)
print()

#-- print file variables
print('------------------------------------------------------')
print()
print('--> file variables:  ', ds.variables)
print()

#-- read variable 'SBTMP_P31_GRLL0_I207'
var  = ds.variables['SBTMP_P31_GRLL0_I207']

#-- print variable information
print('------------------------------------------------------')
print()
print('--> var')
print()
print(var)
print()

#-- print the dimension names, size and shape of the variable
dimnames = var.dimensions

print('------------------------------------------------------')
print()
print('--> var.dimensions           ',var.dimensions)

#-- print the size and shape of the variable
print('------------------------------------------------------')
print()
print('--> var.size           ',var.size)
print('--> var.shape          ',var.shape)
print()

#-- read variables lat and lon
lat  = ds.variables['gridlat_0']
lon  = ds.variables['gridlon_0']

#-- print the size of the coordinates
nlat = len(lat[0])
nlon = len(lat[1])

print('------------------------------------------------------')
print()
print('--> lat:               (%4d,%4d)' % (lat.shape[0],lat.shape[1]))
print('--> lon:               (%4d,%4d)' % (lon.shape[0],lon.shape[1]))
print()

#-- print the minimum and maximum of lat and lon
print('------------------------------------------------------')
print()
print('--> lat min             %12.6f' % np.min(lat))
print('--> lat max             %12.6f' % np.max(lat))
print('--> lon min             %12.6f' % np.min(lon))
print('--> lon max             %12.6f' % np.max(lon))
print()

#-- get the attribute content
lat_spol = lat.attributes['Latitude_of_southern_pole']
lon_spol = lat.attributes['Longitude_of_southern_pole']

#-- retrieve the name of the coordinates lat/lon and the values of 
#-- the shape of the coordinates
dimslat  = dimnames[0]
shapelat = lat.shape
dimslon  = dimnames[1]
shapelon = lon.shape
nrlat    = shapelat
nrlon    = shapelon

print('------------------------------------------------------')
print()
print('--> dimslat: ',dimslat, '  dimslon: ',dimslon,'  nrlat: ',nrlat,'  nrlon: ',nrlon)
print()

#-- print the variable attributes
print('------------------------------------------------------')
print()
print('--> variable attributes: ',var.attributes)
print()

#-- print the variable values
print('------------------------------------------------------')
print()
print('--> values            ')
print()
print(var[:])
print()

#-- print the type of the variable SBTMP_P31_GRLL0_I207 (DataArray)
print('------------------------------------------------------')
print()
print('--> type(var)         ',type(var))
print()

#-- print the type of the variable SBTMP_P31_GRLL0_I207 values (numpy.ndarray)
print('------------------------------------------------------')
print()
print('--> type(var[:])  ',type(var[:]))
print()

#-- select variable SBTMP_P31_GRLL0_I207 from dataset
print('------------------------------------------------------')
print()
print('--> dataset variable SBTMP_P31_GRLL0_I207')
print()
print(ds.variables['SBTMP_P31_GRLL0_I207'][:])
print()

#-- select variable SBTMP_P31_GRLL0_I207 from dataset, lat index 1 and lon index 2
print('------------------------------------------------------')
print()
print('--> dataset variable SBTMP_P31_GRLL0_I207 select data indexing lat=1 and lon=2')
print()
print(ds.variables['SBTMP_P31_GRLL0_I207'][1,2])
print()

#-- select a sub-region (slice) using lat/lon array indexing
print('------------------------------------------------------')
print()
print('--> select sub-region')
print()
print(ds.variables['SBTMP_P31_GRLL0_I207'][0:10,5:25])
print()

#-- print median values of variable SBTMP_P31_GRLL0_I207 of dataset
print('------------------------------------------------------')
print()
print('--> variable SBTMP_P31_GRLL0_I207 median')
print()
print(np.median(ds.variables['SBTMP_P31_GRLL0_I207']))
print()

#-- compute the means of the variable SBTMP_P31_GRLL0_I207 of the dataset
print('------------------------------------------------------')
print()
print('--> variable SBTMP_P31_GRLL0_I207 mean')
print()
mean = np.mean(ds.variables['SBTMP_P31_GRLL0_I207'])
print(mean)
print()

