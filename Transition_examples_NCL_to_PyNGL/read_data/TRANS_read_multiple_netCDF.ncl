;
;  File:
;    TRANS_read_multiple_netCDF.ncl
;
;  Synopsis:
;    Illustrates how to read multiple netCDF files
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
;    This example shows how to read multiple netCDF files.
;
;  Effects illustrated:
;    o  Read netCDF data
; 
;  Output:
;    -
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide NCL Example:   TRANS_read_multiple_netCDF.ncl

   - read multiple netCDF files
   - retrieve variable informations

  2018-08-31  kmf
;/

;-- list of files
file_list  = systemfunc("ls file_*.nc")

;-- open file
f = addfiles(file_list,"r")

;-- read variables
var = f[:]->tsurf
print(getvardimnames(var))

;-- read dimension time variable
time = f[:]->time
print(time)

;-- read dimensions lat and lon variables
lat = f[0]->lat
print(lat)

lon = f[0]->lon
print(lon)
