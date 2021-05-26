'''
DKRZ matplotlib script:  DKRZ_example_ICON_triangles.py

Description:        Python script using matplotlib
                    - ICON model data
                    - variable 'ta'
                    - extract subregion with python-cdo
                    - cell vertices
                    - add colorbar           
25.05.21 kmf
'''
import time
import xarray as xr

import numpy as np
import numpy.ma as ma

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.tri as tri
from   matplotlib.collections import PolyCollection

import cartopy.crs as ccrs
import cartopy.feature as cfeature

from cdo import *
cdo = Cdo()

#------------------------------------------------------------------------------
t1 = time.time()    #-- retrieve start time

#-- set title string
title = 'ICON triangles plot'

#--  define path, file and variable name
diri    = '/Users/k204045/data/ICON/'
fname   = 'ta_ps_850.nc'
gname   = 'grids/r2b4_amip.nc'
varName = 'ta'

ds     = xr.open_dataset(diri+fname)
dsgrid = xr.open_dataset(diri+gname)

#-- get variable
var = ds[varName][0,0,:].values
var = var - 273.15

#-- get coordinates and convert radians to degrees
clon = np.rad2deg(dsgrid.clon.values)
clat = np.rad2deg(dsgrid.clat.values)
clon_vertices = np.rad2deg(dsgrid.clon_vertices.values)
clat_vertices = np.rad2deg(dsgrid.clat_vertices.values)

ncells, nv = clon_vertices.shape[0], clon_vertices.shape[1]

#-- set contour levels, labels
varMin, varMax, varInt = -32, 28, 2 
levels = np.arange(varMin, varMax+varInt, varInt)
nlevs  = levels.size
labels = ['{:.2f}'.format(x) for x in levels] 

#-- print information to stdout
print('')
print('Cells:            %6d ' % clon.size)
print('Variable min/max: %6.2f ' % np.nanmin(var)+'/'+' %.2f' % np.nanmax(var))
print('Contour  min/max: %6.2f ' % varMin+'/'+' %.2f' % varMax)
print('')

#-- set projection
projection = ccrs.PlateCarree()

#-- create figure and axes instances; we need subplots for plot and colorbar
fig, ax = plt.subplots(subplot_kw=dict(projection=projection), figsize=(8,8))

ax.set_global()
              
#-- plot land areas at last to get rid of the contour lines at land
ax.coastlines(linewidth=0.5)
ax.gridlines(draw_labels=True, linewidth=0.5, color='dimgray',  
             alpha=0.4, zorder=3)

#-- plot the title string
plt.title(title)

#-- define color map
cmap     = plt.get_cmap('Spectral_r', nlevs)        #-- read the color map
cmaplist = [i for i in range(cmap.N)]               #-- color bar indices
ncol     = len(cmaplist)                            #-- number of colors
colors   = np.ndarray([ncells,4], np.float32)       #-- assign color array for triangles

print('levels:      ',levels)
print('nlevs:       %3d' %nlevs)
print('ncol:        %3d' %ncol)
print('')

#-- set color index of all cells in between levels
for m in range(0,ncol-1):
    vind = []
    for i in range(0,ncells-2, 1):    
        if (var[i] >= levels[m] and var[i] < levels[m+1]):
           colors[i,:] = cmap(cmaplist[m])
           vind.append(i)
    print('set colors: finished level %3d' % m , ' -- %5d ' % len(vind) , ' polygons considered')
    del vind

colors[np.where(var < varMin),:]  = cmap(cmaplist[0])
colors[np.where(var >= varMax),:] = cmap(cmaplist[ncol-1])

#-- create the triangles
clon_vertices = np.where(clon_vertices < -180., clon_vertices + 360., clon_vertices)
clon_vertices = np.where(clon_vertices >  180., clon_vertices - 360., clon_vertices)

triangles = np.zeros((ncells, nv, 2), np.float32)

for i in range(0, ncells, 1):
    triangles[i,:,0] = np.array(clon_vertices[i,:])
    triangles[i,:,1] = np.array(clat_vertices[i,:])

print('')
print('--> triangles done')

#-- create polygon/triangle collection
coll = PolyCollection(triangles, array=None, fc=colors, edgecolors='none', 
                      linewidth=0.05, transform=ccrs.Geodetic())
ax.add_collection(coll)

print('--> polygon collection done')

#-- add a color bar  
ax   = fig.add_axes([0.2, 0.25, 0.6, 0.015], autoscalex_on=True) #-- x,y,w,h
cbar = mpl.colorbar.ColorbarBase(ax, cmap=cmap, orientation='horizontal', 
                                 ticks=levels, boundaries=levels, format='%0.0f')
plt.setp(cbar.ax.get_xticklabels()[::2], visible=False) 
cbar.set_label('[deg C]')

#-- maximize and save the PNG file
plt.savefig('plot_ICON_triangles.png', bbox_inches='tight',dpi=300)

#-- get wallclock time
t2 = time.time()
print('Wallclock time:  %0.3f seconds' % (t2-t1))
print('')
