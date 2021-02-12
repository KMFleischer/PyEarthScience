# PyEarthScience: Tutorial

### Author: Karin Meier-Fleischer, DKRZ

This tutorial will give an introduction into the software which is needed for 
the use of PyNGL.

More precisely, this is a collection of jupyter notebooks for Python, IO of 
scientific datasets (ASCII, netCDF, GRIB), computing, and plotting. While the 
main focus is on PyNGL, numpy, PyNIO, and xarray. 

It should also be mentioned that it was written from the point of view of NCL
users to find an easier way into the Python world.


## Content

- 01\_Python\_basics - Notebook about Python
	- Functions
    - Data types
    - Lists
    - Tuples
    - Computations
    - Statements
    - Import Python modules


- 02\_NumPy\_basics_ - Notebook about numpy
    - Import numpy
	- Numpy arrays
	- Create and reshape arrays
	- Mathematical attributes and functions
	- Creating arrays for masking
	- Array stacking
	- Shallow and deep copy
	- Most useful functions
	- Read data from CSV file
	- Masking
	- Some hints
    

- 03\_Xarray\_PyNIO\_basics - Notebook about file handling
    - Read from netCDF file
    - Read from GRIB file
    
- 03a\_xarray\_introduction - Notebook about xarray
	- DataArray
	- Dataset
    - Read from netCDF file
    - Read from GRIB file
    
    
- 04\_PyNGL\_basics - Notebook about the basics of plotting with PyNGL
    - Basics

- 04a\_PyNGL\_xy.ipynb - Notebook about xy-plots
	- create a simple xy- plot
	- multiple variables in one xy-plot
	- xy resources

- 04b\_PyNGL\_maps.ipynb - Notebook about maps
	- create a map
	- use different projections
	- map resources

- 04c\_PyNGL\_contour\_on\_maps.ipynb - Notebook about contours on maps
	- create a contour plot on a map
	- zoom into the contour plot
	- cn resources

**_Work in progress_**
```
- 04*_cartopy_*

    - Projections
    - Contours
    - Vectors
    - Slices
    - Curvilinear grids
    - Rotated curvilinear grids
    
- 04*_PyNGL_*  ???

    - Contours
    - Vectors
    - Streamlines
    - Slices
    - Panel
    - Overlays

- 05_xESMF_basics - Notebook about regridding with xESMF


- 06_Shapefile_basics - Notebook about shapefiles

- 07_Conversions - CSV to netCDF

```
	
	