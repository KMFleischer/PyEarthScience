;
;  File:
;    TRANS_read_ASCII_lat_lon_value_way2.ncl
;
;  Synopsis:
;    Illustrates how to read an ASCII file and create a 
;    contour fill plot on a map
;
;  Categories:
;    I/O
;    contour plot
;    map plot
;
;  Author:
;    Karin Meier-Fleischer
;  
;  Date of initial publication:
;    September 2018
;
;  Description:
;    This example shows how to read an ASCII file and 
;    create a contour fill plot on a map.
;
;  Effects illustrated:
;    o  Read ASCII data
;    o  Drawing contours
;    o  Drawing a map
; 
;  Output:
;    -
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide NCL Example:   TRANS_read_ASCII_lat_lon_value_way2.ncl

   based on read_asc6.ncl: http://ncl.ucar.edu/Applications/Scripts/read_asc6.ncl
   
   - read ASCII file asc6.txt
   - retrieve variable informations
   - draw contours on a map

	asc6.txt
	
    Lat     Lon     Temp (C)
    33.3    76.5    20.3
    33.3    76.6    20.3
    33.3    76.7    21.5
    33.3    76.8    20.0
	.....
	
  2018-08-27  kmf
;/

print("")

head  = readAsciiHead("asc6.txt",1)               ;-- 1 header line; unneeded
nrows = numAsciiRow("asc6.txt")                   ;-- retrieve all rows including the header lines
ncols = 3
nrows = nrows-1                                   ;-- without header line

print("-----------------------------------")
print("nrows:  "+nrows)
print("ncols:  "+ncols)
print("head:   "+head)
print("-----------------------------------")

;-- read data  
data   = asciiread("asc6.txt",(/nrows,ncols/),"float")  ;-- read rows and columns with numeric values; no header lines
lat    = data(:,0)                                ;-- column 1
lon    = data(:,1)                                ;-- column 2

;-- compute number of latitudes and longitude values
indeqlat = ind(lat .eq. lat(0))                   ;-- indices of same latitudes (= number of longitudes)
nlons    = dimsizes(indeqlat)                     ;-- number of longitudes
nlats    = nrows / nlons                          ;-- number of latitude

print("nlats = "+sprinti("%4i",nlats))
print("nlons = "+sprinti("%4i",nlons))
print("-----------------------------------")

;-- latitude array
lat1d       =  lat(::nlons)
lat1d!0     = "lat"
lat1d@units = "degrees_north"

;-- longitude array
lon1d       =  lon(0:nlons-1)
lon1d!0     = "lon"
lon1d@units = "degrees_east"

;-- data in 3rd column
temp1D     = data(:,2)

;-- convert 1D array to a 2D array
temp2D     =  onedtond(temp1D,(/nlats,nlons/))
temp2D!0   = "lat"
temp2D!1   = "lon"
temp2D&lat =  lat1d
temp2D&lon =  lon1d

;-- set units
temp2D@units     = "degC"
temp2D@long_name = "temperature"

;-- open a workstation
wks = gsn_open_wks("png","plot_read_ascii_lat_lon_temp")

;-- set resources
res                      =  True
res@gsnAddCyclic         =  False

res@cnFillOn             =  True
res@cnLinesOn            =  False
res@cnLevelSelectionMode = "ManualLevels"
res@cnMinLevelValF       =  min(temp1D)
res@cnMaxLevelValF       =  max(temp1D)
res@cnLevelSpacingF      =  2

res@mpMinLonF            =  min(lon1d)
res@mpMaxLonF            =  max(lon1d)
res@mpMinLatF            =  min(lat1d)
res@mpMaxLatF            =  max(lat1d)

;-- create the plot
plot = gsn_csm_contour_map(wks, temp2D, res)

