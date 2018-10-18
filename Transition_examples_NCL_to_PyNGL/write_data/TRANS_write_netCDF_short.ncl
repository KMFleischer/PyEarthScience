;
;  File:
;    TRANS_write_netCDF_short.ncl
;
;  Synopsis:
;    Illustrates how to write a netCDF file
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
;    This example shows how to write a netCDF file.
;
;  Effects illustrated:
;    o  Reading netCDF file
;    o  Converting data from Kelvin to degC
;    o  Writing data to new netCDF file
; 
;  Output:
;    netCDF data file.
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide NCL Example:   TRANS_write_netCDF_short.ncl

  -  Reading netCDF file
  -  Converting data from Kelvin to degC
  -  Writing data to new netCDF file

  2018-08-28  kmf
;/

;--  data file name
fname  = "../read_data/rectilinear_grid_3D.nc"

;-- open file
f = addfile(fname,"r")

;-- read temperature, time, latitude and longitude arrays
var  =  f->t
time =  f->time
lat  =  f->lat
lon  =  f->lon

;-- convert data from units Kelvin to degC
varC       =  var(:,0,:,:)              ;-- copy variable at level=0; retain metadata
varC       =  varC-273.15               ;-- convert to degC
varC@units = "degC"                     ;-- change units attribute

;-- open new netCDF file
system("rm -rf t_degC_ncl_short.nc")        ;-- delete file if it exists
outf = addfile("t_degC_ncl_short.nc","c")   ;-- open new netCDF file

;-- write data to new file
outf->time = time
outf->lat  = lat
outf->lon  = lon
outf->t    = varC

;-- close output stream (not necessary)
delete(outf)
