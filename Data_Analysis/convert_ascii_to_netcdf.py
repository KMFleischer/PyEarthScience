import numpy as np
from cdo import *
import csv

'''
Convert a CSV data to netCDF

Read the CSV file, generate the gridfile from the CSV lon and lat data, 
write data to file. Then use cdo to write the data to an netCDF file.
'''

cdo = Cdo()

# Read Ascii data

ascii_data = np.genfromtxt('data/1901_1.csv', dtype=None, delimiter=',')

# Get number of lines and columns

nlines = ascii_data.shape[0]
ncols = ascii_data.shape[1]

print('\nWrong form of data!')
print('--> data shape        = (%d,%d) ' % ascii_data.shape)
print('--> number of lines   = %d ' % nlines)
print('--> number of columns = %d ' % ncols)

# The data is in the wrong shape (columns x lines). The rows and columns must be swapped (lines x columns). 

data = ascii_data.T
nlat = data.shape[0]
nlon = data.shape[1]

print('\nCorrect form of data!')
print('--> data shape      = (%d,%d) ' % data.shape)
print('--> number of lat   = %d ' % nlat)
print('--> number of lon   = %d ' % nlon)

# Set variable name

varname = 't'

# Set missing value

missing = 1e20

# Set time and reference time

reftime = '1900-01-01,00:00:00,1day'
time = '1901-01-01,12:00:00,1day'

# Set NaN to missing value.

data = np.nan_to_num(data, nan=missing)

# Write data array to file data/var.txt.

np.savetxt('data/var.txt', data, delimiter=', ', fmt='%1.2e') 

# Write grid description file.

f = open('data/gridfile_ascii.txt', 'w')
f.write('gridtype  = lonlat'+'\n')
f = open('data/gridfile_ascii.txt', 'a')
f.write('gridsize  = '+str(nlines*ncols)+'\n')
f.write('xsize     = ' + str(nlon)+'\n')
f.write('ysize     = ' + str(nlat)+'\n')
f.write('xname     = lon'+'\n')
f.write('xlongname = longitude'+'\n')
f.write('xunits    = degrees_east'+'\n')
f.write('xfirst    = -179.75'+'\n')
f.write('xinc      = 0.5'+'\n')
f.write('yname     = lat'+'\n')
f.write('ylongname = latitude'+'\n')
f.write('yunits    = degrees_north'+'\n')
f.write('yfirst    = -89.75'+'\n')
f.write('yinc      = 0.5'+'\n')
f.close()

# CDO command:
#   - read the ASCII data
#   - set variable name
#   - set the calendar, time and reference time
#   - set the missing value
#   - convert to netCDF file format

cdo.settaxis(
        time, input='-setreftime,1900-01-01,00:00:00,1day '+ \
        '-setcalendar,standard '+ \
        '-setmissval,'+str(missing)+ \
        ' -setname,'+varname+ \
        ' -input,data/gridfile_ascii.txt < data/var.txt',
        output='tmp.nc', 
        options = '-f nc')
        
# CDO command:
#   - add variable attributes long_name and units
#   - add global attribute source

cdo.setattribute(
        varname+'@long_name="monthly mean temperature",'+\
        varname+'@units="deg C",'+ \
        'source="CRU"',
        input='tmp.nc', 
        output='1901_1.nc')

