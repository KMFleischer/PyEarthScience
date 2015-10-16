"""
  PyEarthScience: matplotlib vector example

   - vectors on map plot
   - rectilinear grid (lat/lon)
   
   09.10.15  kmf
"""
from   mpl_toolkits.basemap import Basemap, cm, shiftgrid, addcyclic
import matplotlib.pyplot as plt
from   netCDF4 import *
import numpy as np

#-- open netcdf file
nc = Dataset('/Users/k204045/NCL/general/data/new_data/rectilinear_grid_2D.nc', mode='r')

#-- read variable
u10 = nc.variables['u10'][0,:,:]
v10 = nc.variables['v10'][0,:,:]
lat = nc.variables['lat'][::-1]
lon = nc.variables['lon'][:]

u, lonsout = addcyclic(u10, lon)
v, lonsout = addcyclic(v10, lon)
print "lon[0]: ", lonsout[0], "lon[-1]: ", lonsout[-1]
print "lat[0]: ", lat[0], "lat[-1]: ", lat[-1]
print lonsout[:]
print lat[:]

#-- create figure and axes instances
fig = plt.figure(figsize=(8,8))
ax  = fig.add_axes([0.1,0.4,0.7,0.7])

#-- create map
map = Basemap(projection='cyl',llcrnrlat= -90.,urcrnrlat= 90.,\
              resolution='c',  llcrnrlon=-180.,urcrnrlon=180.)

#-- draw coastlines, state and country boundaries, edge of map
map.drawcoastlines()
map.drawstates()
map.drawcountries()

#-- create and draw meridians and parallels grid lines
map.drawparallels(np.arange( -90., 90.,30.),labels=[1,0,0,0],fontsize=10)
map.drawmeridians(np.arange(-180.,180.,30.),labels=[0,0,0,1],fontsize=10)

#-- convert latitude/longitude values to plot x/y values
x, y = map(*np.meshgrid(lon,lat))

#-- transform vector and coordinate data
veclon = u10.shape[1]/2                    #-- only every 2nd vector
veclat = u10.shape[0]/2                    #-- only every 2nd vector
uproj,vproj,xx,yy = map.transform_vector(u,v,lonsout,lat,veclon,veclat,returnxy=True,masked=True)

#-- create vector plot on map
vecplot = map.quiver(xx,yy,uproj,vproj,scale=600)
qk = plt.quiverkey(vecplot, 0.2, -0.2, 20, '20 m/s', labelpos='W')  #-- position and reference label

#-- add plot title
plt.title('Wind velocity')

plt.show()
#plt.savefig('plot_vector_matplotlib.png')
