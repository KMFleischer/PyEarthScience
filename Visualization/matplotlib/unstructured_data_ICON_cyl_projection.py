#---------------------------------------------------------------
#-- DKRZ PyNGL Script:  compare_vis_tools_ICON_matplotlib.py
#--
#-- Description:        Python script using matplotlcompare_vis_tools_ICON_matplotlib.pyib Python module
#--                     - ICON data
#--                     - cell center
#--                     - cylindrical equidistant projection
#-- 20.07.15  kmf
#---------------------------------------------------------------
import math, time, sys, os
from   mpl_toolkits.basemap import Basemap, cm
import matplotlib.pyplot as plt
from   netCDF4 import Dataset as open_ncfile
import numpy as np

t1 = time.time()                                   #-- retrieve start time
print ""

#--  define variables
diri    = "./"                                     #-- data directory
fname   = "ta_ps_850.nc"                           #-- data file
gname   = "r2b4_amip.nc"                           #-- grid info file
VarName = "ta"                                     #-- variable name       

#--  open file and read variables
f = open_ncfile(diri + fname,"r")                  #-- add data file
g = open_ncfile(diri + gname,"r")                  #-- add grid file (not contained in data file!!!)

#-- read a timestep of "ta" 
variable =  f.variables["ta"]                      #-- first time step, lev, ncells
var      =  variable[0,0,:]                        #-- ta [time,lev,ncells]
var      =  var - 273.15                           #-- convert to degrees Celsius

#-- check if missing value set
if not hasattr(var,"_FillValue"):
   var._FillValue    =  np.array(1.e20,dtype='f')  #-- set _FillValue
if not hasattr(var,"missing_value"):
   var.missing_value =  np.array(1.e20,dtype='f')  #-- set missing_value

print "-----------------------"
print f.variables["ta"]                            #-- like printVarSummary
print "-----------------------"

title    = "ICON:  Surface temperature"            #-- title string
varMin   = -32                                     #-- data minimum
varMax   =  28                                     #-- data maximum
varInt   =   4                                     #-- data increment
levels   = np.arange(varMin,varMax,varInt)         #-- set levels array

#-------------------------------------------------------------------
#-- define the x-, y-values and the polygon points
#-------------------------------------------------------------------
rad2deg = 45./np.arctan(1.)                        #-- radians to degrees

x      =  g.variables["clon"][:]
y      =  g.variables["clat"][:]
vlon   =  g.variables["clon_vertices"][:]
vlat   =  g.variables["clat_vertices"][:]

ncells =  vlon.shape[0]                            #-- number of cells
nv     =  vlon.shape[1]                            #-- number of edges

minlon = -180
maxlon =  180
minlat =  -90
maxlat =   90

#-- create map
map = Basemap(projection = 'cyl',llcrnrlat = minlat,urcrnrlat = maxlat,\
              resolution = 'l',  llcrnrlon = minlon,urcrnrlon = maxlon)

#-- convert latitude/longitude values into degrees
x =  x * rad2deg                                   #-- cell center, lon
y =  y * rad2deg                                   #-- cell center, lat

#-- convert latitude/longitude values to plot x/y values
x0, y0 = map(x,y)

#-- information
print ""
print "Cell points:           ", nv
print "Cells:                 ", str(ncells)
print "Variable ta   min/max:  %.2f " % np.min(var) + "/" + " %.2f" % np.max(var)
print ""

#-- create figure and axes instances
fig = plt.figure(figsize=(8,8))
ax  = fig.add_axes([0.1,0.1,0.8,0.9])

#-- contour levels
varMin = -32                                       #-- data minimum
varMax =  28                                       #-- data maximum
varInt =   4                                       #-- data increment
levels =  range(varMin,varMax,varInt)              #-- set levels array

#-- contour levels
clevs = np.arange(varMin,varMax,varInt)

#-- draw filled contours
colormap = plt.cm.RdYlBu_r                                   #-- reversed colormap _r
cnplot = map.contourf(x0,y0,var,clevs,cmap=colormap,tri=True)

#-- add colorbar
cbar = map.colorbar(cnplot,location='bottom',pad="10%")      #-- pad: distance between map and colorbar
cbar.set_label('deg K')                                      #-- add colorbar title string

#-- draw coastlines, state and country boundaries, edge of map
map.drawcoastlines()
map.drawstates()
map.drawcountries()

#-- create and draw meridians and parallels grid lines
map.drawparallels(np.arange(minlat, maxlat, 30.),labels=[1,0,0,0],fontsize=10)
map.drawmeridians(np.arange(minlon, maxlon, 30.),labels=[0,0,0,1],fontsize=10)

#-- create the plot
plt.savefig('plot_compare_ICON_matplotlib_cyl.png', bbox_inches='tight')

#-- get wallclock time
t2 = time.time()
print "Wallclock time:  %0.3f seconds" % (t2-t1)
print ""
