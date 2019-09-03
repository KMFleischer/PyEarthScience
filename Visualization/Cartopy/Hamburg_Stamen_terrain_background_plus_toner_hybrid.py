#
#  File:
#    Hamburg_Stamen_terrain_background_plus_toner_hybrid.py
#
#  Synopsis:
#    Illustrates how to use the Stamen tile server and the 
#    http://www.naturalearthdata.com/features/ features
#
#  Categories:
#    cartopy
#    tiles
#    features
#
#  Author:
#    Karin Meier-Fleischer
#  
#  Date of initial publication:
#    August 2019
#
#  Description:
#    This example shows how to use the Stamen terrain with flavour background
#    and the RIVERS feature from naturalearthdata.com.
#
#  Effects illustrated:
#    o  Add Stamen terrain-background tile data to plot
#    o  Add rivers from naturalearthdata.com to plot
#    o  Add colorbar
#    o  Add gridlines
#    o  Add coastlines
# 
#  Output:
#    A single visualization is produced.
#   
'''
  DKRZ Cartopy example:  Hamburg_Stamen_terrain_background_plus_toner_hybrid.py

    -  Add Stamen terrain-background tile data to plot
    -  Add rivers from naturalearthdata.com to plot
    -  Add colorbar
    -  Add gridlines
    -  Add coastlines
	
  19-09-02  kmf
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.img_tiles as cimgt
import cartopy.util as cutil
from   cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

def main():
    #-- zoom into the map: lonmin, lonmax, latmin, latmax
    extent = [9.55, 10.4, 53.5, 53.8]
                   
    #-- create a Stamen terrain background instance
    tiles = cimgt.Stamen(style='terrain-background')
    print('---> add tiles')
  
    #-- create figure and axes instances
    fig = plt.figure(figsize=(12,12))
    ax  = plt.axes(projection=tiles.crs)

    #-- limit the extent of the map to a small longitude/latitude range
    ax.set_extent(extent)

    #-- use http://www.naturalearthdata.com/features/ to plot additional features
    #-- add rivers, lakes, and state borders
    ax.add_feature(cfeature.RIVERS.with_scale('10m'),  linewidth=1.0, edgecolor='blue',  facecolor='None')
    print('---> add rivers')
    
    ax.add_feature(cfeature.LAKES.with_scale('10m'),   linewidth=1.0, edgecolor='grey',  facecolor='None')
    print('---> add lakes')
    
    ax.add_feature(cfeature.BORDERS.with_scale('10m'), linewidth=1.0, edgecolor='black', facecolor='None')
    print('---> add borders')

    #-- add the Stamen data at zoom level 8
    ax.add_image(tiles, 10, interpolation='spline36')
    print('---> add image tiles')

    #-- add Stamen toner-hybrid to plot
    hybrid = cimgt.GoogleTiles(url="http://tile.stamen.com/toner-hybrid/{z}/{x}/{y}.png", desired_tile_form='RGBA')
    print('---> add hybrid')
    
    ax.add_image(hybrid, 10, interpolation='spline36')
    print('---> add image hybrid')

    #-- add coastlines
    ax.coastlines(resolution='10m', linewidth=1.0)
    print('---> add coastlines')

    #-- add gridlines
    gl = ax.gridlines(crs=ccrs.PlateCarree(), linewidth=1.0, color='black', alpha=0.5, 
                      linestyle='--', draw_labels=True)
    gl.xlocator   = mticker.FixedLocator(np.arange(9.,11.,0.1))
    gl.ylocator   = mticker.FixedLocator(np.arange(53.,54.,0.1))
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    print('---> add gridlines')

    #-- maximize and save PNG file
    plt.savefig('plot_Hamburg_stamen.png', bbox_inches='tight', dpi=100)


#-- call main
if __name__ == '__main__':
    main()

