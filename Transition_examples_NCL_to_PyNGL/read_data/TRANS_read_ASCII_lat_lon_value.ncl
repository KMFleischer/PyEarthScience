;
;  File:
;    TRANS_read_ASCII_lat_lon_value.ncl
;
;  Synopsis:
;    Illustrates how to read an ASCII file
;
;  Categories:
;    I/O
;
;  Author:
;    Karin Meier-Fleischer
;  
;  Date of initial publication:
;    September 2018
;
;  Description:
;    This example shows how to read an ASCII file.
;
;  Effects illustrated:
;    o  Read ASCII data
; 
;  Output:
;    -
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide NCL Example:   TRANS_read_ASCII_lat_lon_value.ncl

   based on read_asc6.ncl: http://ncl.ucar.edu/Applications/Scripts/read_asc6.ncl
   
   - read ASCII file asc6.txt
   - retrieve variable informations

  Input file: asc6.txt
	
    Lat     Lon     Temp (C)
    33.3    76.5    20.3
    33.3    76.6    20.3
    33.3    76.7    21.5
    33.3    76.8    20.0
	.....
	
  2018-08-27  kmf
;/

;-- file has 21361 lines but 1 header line
;-- 3 columns
nrows   = 21360                         ;-- file has 21361 lines but 1 header line
ncols   =     3                         ;-- file has 3 columns
num_lon =   240                         ;-- number of longitudes
num_lat =    89                         ;-- number of latitudes

;-- read all data from file
data = asciiread("asc6.txt",(/nrows,ncols/),"float")

;-- select lat, lon and temp data
lat    = data(::num_lon,0)
lon    = data(:num_lon-1,1)
temp1D = data(:,2)

;-- size of lat, lon and temp1d
nlats  = dimsizes(lat)
nlons  = dimsizes(lon)
ntemp  = dimsizes(temp1D)

;-- reshape temp1d to 2D-array temp2d with size (89,240)
temp2D = onedtond(temp1D,(/nlats,nlons/))

;-- print information
print("rank  temp1D: " + dimsizes(dimsizes(temp1D)))
print("shape temp1D: " + ntemp)
print("rank  temp2D: " + dimsizes(dimsizes(temp2D)))
print("shape temp2D: " + dimsizes(temp2D))

