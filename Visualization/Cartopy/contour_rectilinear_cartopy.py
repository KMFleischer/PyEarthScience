"""
  PyEarthScience: Cartopy contour plot example
  
   - filled contour over map plot
   - rectilinear grid (lat/lon)
   - colorbar
   
   10.11.15  kmf
"""
import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs


def read_netCDF_file():
   """Read netcdf file and return arrays: ``lat``,``lon``, ``var``."""
   
   file_name = '/Users/k204045/NCL/general/data/new_data/rectilinear_grid_2D.nc'
   
   with nc.Dataset(file_name) as nco:
       var   = nco.variables['tsurf'][0,:,:]
       lat   = nco.variables['lat'][:]
       lon   = nco.variables['lon'][:]

   return lat, lon, var


def main():
    ax = plt.axes(projection=ccrs.Orthographic())

    lat, lon, var = read_netCDF_file()

    plot = ax.contourf(lon, lat, var, transform=ccrs.PlateCarree(), cmap='spectral')
    ax.coastlines()
    ax.set_global()

    plt.colorbar(plot, orientation='horizontal')  # draw colorbar

    plt.show()


if __name__ == '__main__':
    main()
