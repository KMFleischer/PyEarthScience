import numpy as np
from cdo import *

'''
Convert a CSV data file to netCDF file

   - read the CSV file
   - generate the gridfile from the CSV lon and lat values
   - write data to file
   - write netcdf file

Input data columns:  
    lon, lat, value

'''

cdo = Cdo()

# Read the CSV data

csv_data = np.genfromtxt('data/input.csv', usecols=(0, 1, 2), skip_header=1, 
                          dtype=None, delimiter=',')

lon = list(map(float, csv_data['f0']))
lat = list(map(float, csv_data['f1']))
values = list(map(float, csv_data['f2']))

nlon = len(lon)
nlat = len(lat)
nlines = nlon

print('--> longitudes:   ', lon)
print('--> # longitudes: %d' % nlon)
print('--> latitudes:    ', lat)
print('--> # latitudes:  %d' % nlat)
print('--> values:       ', values)

# Set variable name

varname = 'var'

# Set time and reference time

time = '1950-01-01,12:00:00,1day'

# Write value array to file data/var.txt

fv = open('data/var.txt', 'w')
[fv.write(str(s)+'\n') for s in values]
fv.close()

# Write grid description file

f = open('data/gridfile.txt', 'w')
f.write('gridtype  = unstructured'+'\n')
f = open('data/gridfile.txt', 'a')
f.write('gridsize  = '+str(nlines)+'\n')
f.write('xname     = lon'+'\n')
f.write('xlongname = longitude'+'\n')
f.write('xunits    = degrees_east'+'\n')
f.write('yname     = lat'+'\n')
f.write('ylongname = latitude'+'\n')
f.write('yunits    = degrees_north'+'\n')
f.write('xsize     = ' + str(nlon)+'\n')
f.write('ysize     = ' + str(nlat)+'\n')
f.write('xvals     = ' + ', '.join(str(x) for x in tuple(lon))+'\n')
f.write('yvals     = ' + ', '.join(str(x) for x in tuple(lat))+'\n')
f.close()

# CDO command:

cdo.settaxis(
        time, 
        input='-setname,'+varname+ \
        ' -input,data/gridfile.txt < data/var.txt',
        output='input.nc',
        options = '-f nc')


