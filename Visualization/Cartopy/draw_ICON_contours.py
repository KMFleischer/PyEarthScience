'''
DKRZ matplotlib script:  DKRZ_example_ICON_tricontourf.py

Description:        Python script using matplotlib
                    - ICON model data
                    - variable 'ta'
                    - extract subregion with python-cdo
                    - cell center
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

import cartopy.crs as ccrs
import cartopy.feature as cfeature

from cdo import *
cdo = Cdo()

#------------------------------------------------------------------------------
t1 = time.time()    #-- retrieve start time

#-- set title string
title = 'ICON tricontourf plot'

#--  define path, file and variable name
diri    = '/Users/k204045/data/ICON/'
fname   = 'ta_ps_850.nc'
gname   = 'grids/r2b4_amip.nc'
varName = 'ta'

#-- extract subregion of the global grid with CDO
minlon, maxlon, minlat, maxlat = -179.5, 179.5, -89.5, 89.5
#minlon, maxlon, minlat, maxlat = -30.0, 40.0, 40.0, 70.0

#-- compound the CDO command input
#-- make sure that nan, inf, and -inf are set to missing value
cdo_in1 = '-setmisstoc,-9999. -setgrid,'+diri+gname+' '
cdo_in2 = diri+'/'+fname+' '
cdo_all = cdo_in1 + cdo_in2

Data = cdo.sellonlatbox('{0},{1},{2},{3}'.format(minlon,maxlon,minlat,maxlat),
                        input=cdo_all, options='-r', returnXDataset=True)
#-- get missing_value
missing_value = Data[varName].encoding['missing_value']

#-- get variable
var = Data[varName][0,0,:].values
var = var - 273.15

#-- get coordinates and convert radians to degrees
clon = np.rad2deg(Data.clon.values)
clat = np.rad2deg(Data.clat.values)

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

#-- set colormap
cmap = plt.get_cmap('Spectral_r', nlevs)

#-- create figure and axes instances; we need subplots for plot and colorbar
fig, ax = plt.subplots(subplot_kw=dict(projection=projection), figsize=(8,8))

ax.set_global()

cnf = ax.tricontourf(clon, clat, var, vmin=varMin, vmax=varMax, levels=levels, 
                     cmap=cmap, extend='neither')
              
#-- plot land areas at last to get rid of the contour lines at land
ax.gridlines(draw_labels=True, linewidth=0.5, color='dimgray', alpha=0.4, 
             zorder=3)
ax.coastlines(linewidth=0.5)

#-- plot the title string
plt.title(title)

#-- add a color bar
cbar_ax = fig.add_axes([0.2, 0.25, 0.6, 0.015], autoscalex_on=True) #-- x,y,w,h
cbar = fig.colorbar(cnf, cax=cbar_ax, orientation='horizontal')                     
plt.setp(cbar.ax.get_xticklabels()[::2], visible=False) 
cbar.set_label('[deg C]')

#-- maximize and save the PNG file
plt.savefig('plot_ICON_tricontourf.png', bbox_inches='tight',dpi=300)

#-- get wallclock time
t2 = time.time()
print('Wallclock time:  %0.3f seconds' % (t2-t1))
print('')
