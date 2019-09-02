#
#  PyEarthScience:  read_netCDF_with_PyNIO.py
#
#  Description:
#    Demonstrate the use of PyNIO to open and read the content of 
#    a netCDF file. 
# 
#  Author:
#    Karin Meier-Fleischer
#  
#  Date of initial publication:
#    August, 2019
#
'''
  PyEarthScience:  read_netCDF_with_PyNIO.py

  Description:
    Demonstrate the use of PyNIO to open and read the content of
    a netCDF file. 

  - PyNIO
  - PyNGL
  - numpy
  - netCDF
'''
import os
import numpy as np
import Ngl, Nio

#-----------------------------------------------------------------------
#-- Function: getVariableNames() - return the variable names (without coordinates)
#-----------------------------------------------------------------------
def getVariableNames(file):
    dims   = file.dimensions
    coords = list(dims.keys())
    names  = list(file.variables.keys())
    vnames = [n for n in names if n not in coords]

    return(vnames, coords)

#-----------------------------------------------------------------------
#-- Function:   main
#-----------------------------------------------------------------------
def main():

    #-- input file rectilinear_grid_3d.nc from the NCL User Guide
    #-- is available in the PyNGL installation
    home  = os.environ.get('HOME')
    fname = os.path.join(home,"local/miniconda2/envs/pyngl_py3/lib/python3.7/site-packages/ngl/ncarg/data/nug/rectilinear_grid_3D.nc") #-- data file name
    
    #-- open file and print some information similar to ncdump and others
    file =  Nio.open_file(fname,"r")
    
    print('------------------------------------------------------')
    print()
    print('--> file        ', file)
    print()
    
    print('--> file attributes ', file.attributes)
    print()
    
    dims = file.dimensions
    
    print('--> file dimensions ', dims.values)
    print()
    
    print('--> file size of dimension time = ', dims['time'])
    print('--> file size of dimension lat  = ', dims['lat'])
    print('--> file size of dimension lon  = ', dims['lon'])
    #-- same as above
    #print('--> file size of dimension time = ', file.dimensions['time'])
    #print('--> file size of dimension lat  = ', file.dimensions['lat'])
    #print('--> file size of dimension lon  = ', file.dimensions['lon'])
    print()
    
    #-- get the variable and coordinates names (using function defined at the top of the script)
    vnames, coords = getVariableNames(file)
    
    print('--> Variable names (no coordinates):  ', vnames)
    print('--> Variable names for coordinates:   ', coords)
    print()
    
    #-- get the attributes of variable 't'    
    vattr = [getattr(file.variables['t'],a) for a in file.variables['t'].attributes.keys()]
    print('--> file variable attributes ', list(vattr))
    print()

    #-- read variable 't', first timestep, first level
    var = file.variables['t'][0,0,:,:]
    
    #-- print the size and shape of the variable
    print('------------------------------------------------------')
    print()
    print('--> var.size           ',var.shape[0] * var.shape[1])
    print('--> var.shape          ',var.shape)
    
    #-- same as
    #print('--> var.size           ',f.dimensions['lat'] * f.dimensions['lon'])
    #print('--> var.shape          ',var.shape)
    print()
    
    #-- read variable latitude and longitude arrays
    lat = file.variables['lat'][:]
    lon = file.variables['lon'][:]
    
    #-- print the minimum and maximum of lat and lon
    print('------------------------------------------------------')
    print()
    print('--> lat min             ', lat.min().item())
    print('--> lat max             ', lat.max())
    print('--> lon min             ', lon.min())
    print('--> lon max             ', lon.max())
    
    #-- the above notation has the same results as below
    #print('--> lat min             ', lat.min().item())
    #print('--> lat max             ', lat.max().item())
    #print('--> lon min             ', lon.min().item())
    #print('--> lon max             ', lon.max().item())
    print()
    

    #-- retrieve the name of the coordinates lat/lon variables and the values of 
    #-- the shape of the coordinates
    dimslat  = coords[0]
    shapelat = lat.shape[0]
    dimslon  = coords[1]
    shapelon = lon.shape[0]
    nrlat    = shapelat
    nrlon    = shapelon
    
    print('------------------------------------------------------')
    print()
    print('--> dimslat: ',dimslat, '  dimslon: ',dimslon,'  nrlat: ',nrlat,'  nrlon: ',nrlon)
    print()

    #-- print variable information
    print('------------------------------------------------------')
    print()
    print('--> var information')
    print()
    print(var)
    print()
    
    ##-- print the variable attributes
    #print('------------------------------------------------------')
    #print()
    #print('--> attributes:       ',var.key())
    #print()
    
    #-- print the variable values
    #print('------------------------------------------------------')
    #print()
    #print('--> values            ')
    #print()
    #print(var.values)
    #print()
    
    #-- print the type of the variable (DataArray)
    print('------------------------------------------------------')
    print()
    print('--> type(var)         ',type(var))
    print()
    
    #-- print the type of the variable values (numpy.ndarray)
    print('------------------------------------------------------')
    print()
    print('--> type(var.values)  ',type(var[:,:]))
    print()
    
    #-- select variable t from dataset for first timestep
    print('------------------------------------------------------')
    print()
    print('--> dataset variable t (time=0, lev=6)')
    print()
    print(file.variables['t'][0,6,:,:])
    print()
    
    #-- select variable t from dataset, lat index 1 and lon index 2
    print('------------------------------------------------------')
    print()
    print('--> dataset variable t select data which is closest to lat=1 and lon=2')
    print()
    print(file.variables['t'][:,:,1,2])
    print()
    
    #-- select variable t, timestep 2001-01-01
    print('------------------------------------------------------')
    print()
    print('--> time(0) = "2001-01-01"')
    print()
    print(file.variables['t'][0,:,:,:])
    print()
    
    #-- select a sub-region (slice) - Take attention to the strange notation of the selection!
    #-- The leading i tells PyNIO to use the index instead of coordinate values, e.g. time|i0
    print('------------------------------------------------------')
    print()
    print('--> select sub-region')
    print()
    print(file.variables['t']['time|i0 lev|: lat|20:0 lon|-25:0'])
    print()
    
    #-- print median values of variable t of dataset, one value for each level (axis=lat,lon)
    print('------------------------------------------------------')
    print()
    print('--> variable median')
    print()
    print(np.median(file.variables['t'],axis=(2,3)))
    print()
    
    #-- compute the means of the variable t of the dataset, one value for each level (axis=lat,lon)
    print('------------------------------------------------------')
    print()
    print('--> means')
    print()
    means = np.mean(file.variables['t'], axis=(2,3))
    print(means)
    print()
    
    #-- compute the mean of the variable t which are greater than 273.15 K
    print('------------------------------------------------------')
    print()
    print('--> only means greater than 273.15 K')
    print()
    print(means[np.where(means > 273.15)])
    print()

#-------------------------------------------------------------
#-- run main
#-------------------------------------------------------------
if __name__ == "__main__":
   main()
