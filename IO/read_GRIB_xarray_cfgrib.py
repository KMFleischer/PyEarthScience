#
#  File:
#    read_GRIB_with_xarray_cfgrib.py
#
#  Synopsis:
#    Illustrates how to read a GRIB file with xarray.
#
#  Description:
#    This example shows how to read a GRIB file using xarray / cfgrib.
#
#  Author:
#    Karin Meier-Fleischer
#  
#  Date of initial publication:
#    September, 2019
#
'''
  PyEarthScience:   read_GRIB_with_xarray_cfgrib.py

  Description:
    Demonstrate the use of xarray/cfgrib to open and read the content of
    a GRIB file. 

  - xarray / cfgrib
  - GRIB
  
  2019-01-22  kmf
'''

from __future__ import print_function
import cfgrib
import xarray as xr
import Ngl, os

#-- data directory and file name, we use an example GRIB file from the NCL package
ncarg  = Ngl.pynglpath("data")
fname  = ncarg+'/grb/MET9_IR108_cosmode_0909210000.grb2'

#--  open file
ds = xr.open_dataset(fname, engine='cfgrib')

print('------------------------------------------------------')
print()
print('--> ds:              ', ds)
print()

#-- print file variables
print('------------------------------------------------------')
print()
print('--> file variables:  ', ds.variables)
print()

#-- read variable 'p260532'
var  = ds.variables['p260532']

#-- print variable information
print('------------------------------------------------------')
print()
print('--> var')
print()
print(var)
print()

#-- print the size and shape of the variable
print('------------------------------------------------------')
print()
print('--> var.dims           ',var.dims)

#-- print the size and shape of the variable
print('------------------------------------------------------')
print()
print('--> var.size           ',var.size)
print('--> var.shape          ',var.shape)

#-- read variables lat and lon
lat  = ds.variables['latitude']
lon  = ds.variables['longitude']

#-- print the size of the coordinates
nlat = len(lat[0])
nlon = len(lat[1])
print('------------------------------------------------------')
print()
print('--> lat:               %8d %8d' % (lat.shape[0],lat.shape[1]))
print('--> lon:               %8d %8d' % (lon.shape[0],lon.shape[1]))
print()

#-- print the minimum and maximum of lat and lon
print('------------------------------------------------------')
print()
print('--> lat min             ', lat.min().values)
print('--> lat max             ', lat.max().values)
print('--> lon min             ', lon.min().values)
print('--> lon max             ', lon.max().values)
print()

#-- get the attribute content
lat_spol = var.attrs['GRIB_latitudeOfSouthernPoleInDegrees']
lon_spol = var.attrs['GRIB_longitudeOfSouthernPoleInDegrees']

#-- retrieve the name of the coordinates lat/lon and the values of 
#-- the shape of the coordinates
dimslat  = lat.dims[0]
shapelat = lat.shape[0]
dimslon  = lon.dims[0]
shapelon = lon.shape[0]
nrlat    = shapelat
nrlon    = shapelon

print('------------------------------------------------------')
print()
print('--> dimslat: ',dimslat, '  dimslon: ',dimslon,'  nrlat: ',nrlat,'  nrlon: ',nrlon)
print()

#-- print the variable attributes
print('------------------------------------------------------')
print()
print('--> attributes:       ',var.attrs)
print()

#-- print the variable values
print('------------------------------------------------------')
print()
print('--> values            ')
print()
print(var.values)
print()

#-- print the type of the variable p260532 (DataArray)
print('------------------------------------------------------')
print()
print('--> type(var)         ',type(var))
print()

#-- print the type of the variable p260532 values (numpy.ndarray)
print('------------------------------------------------------')
print()
print('--> type(var.values)  ',type(var.values))
print()

#-- select variable p260532 from dataset for first timestep
print('------------------------------------------------------')
print()
print('--> dataset variable p260532 (y=0)')
print()
print(ds.p260532.isel(y=0).values)
print()

#-- select variable p260532 from dataset, lat index 1 and lon index 2
print('------------------------------------------------------')
print()
print('--> dataset variable p260532 select data which is closest to y=1 and x=2')
print()
print(ds.p260532.isel(y=1, x=2).values)
print()

#-- select a sub-region (slice)
print('------------------------------------------------------')
print()
print('--> select sub-region')
print()
print(ds.p260532.sel(y=slice(20, 0), x=slice(-25, 0)))
print()

#-- print dataset minimum/maximum: prints the name of the variables, 
#-- their types and minimum value
print('------------------------------------------------------')
print()
print('--> print dataset min')
print()
print(ds.min().values)
print()
print('--> print dataset max')
print()
print(ds.max().values)
print()

#-- print median values of variable p260532 of dataset, one value for each level
print('------------------------------------------------------')
print()
print('--> variable p260532 median')
print()
print(ds.p260532.median(dim=['y', 'x']).values)
print()

#-- compute the means of the variable p260532 of the dataset, one value for each level
print('------------------------------------------------------')
print()
print('--> variable p260532 mean')
print()
mean = ds.p260532.mean(dim=['y', 'x'])
print(mean.values)
print()


