;
;  File:
;    TRANS_write_netCDF.ncl
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
;    o  Detailed version
;
;  Output:
;    netCDF data file.
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide NCL Example:   TRANS_write_netCDF.ncl

  -  Reading netCDF file
  -  Converting data from Kelvin to degC
  -  Writing data to new netCDF file
  -  Detailed version
   
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

;-- dimension sizes
ntime = dimsizes(time)
nlat  = dimsizes(lat)
nlon  = dimsizes(lon)

;-- convert data from units Kelvin to degC
varC =  var(:,0,:,:)                    ;-- variable at level=0; retain metadata
varC =  varC-273.15                     ;-- convert to degC
varC@long_name = "temperature"          ;-- change units attribute
varC@units     = "degC"                 ;-- change units attribute

print(getvardimnames(varC))

;-- open new netCDF file
system("rm -rf t_degC_ncl.nc")          ;-- delete file if it exists
outf = addfile("t_degC_ncl.nc","c")     ;-- open new netCDF file

;-- begin output file settings
setfileoption(outf,"DefineMode",True)   ;-- explicitly declare file definition mode

;-- predefine the coordinate variables and their dimensionality
dimNames = (/"time", "lat", "lon"/)  
dimSizes = (/ -1   ,  nlat,  nlon/) 
dimUnlim = (/ True , False, False/)   
filedimdef(outf,dimNames,dimSizes,dimUnlim)

;-- predefine the the dimensionality of the variables to be written out
filevardef(outf, "time" ,typeof(time), getvardimnames(time)) 
filevardef(outf, "lat"  ,typeof(lat),  getvardimnames(lat))                          
filevardef(outf, "lon"  ,typeof(lon),  getvardimnames(lon))                          
filevardef(outf, "t"    ,typeof(varC), getvardimnames(varC))

;-- copy attributes associated with each variable to the file
filevarattdef(outf,"time" ,time)       ;-- copy time attributes
filevarattdef(outf,"lat"  ,lat)        ;-- copy lat attributes
filevarattdef(outf,"lon"  ,lon)        ;-- copy lon attributes
filevarattdef(outf,"t"    ,varC)       ;-- copy varC attributes

;-- explicitly exit file definition mode (not required)
  setfileoption(outf,"DefineMode",False)
  
;-- write data to new file
outf->time = (/time/)
outf->lat  = (/lat/)
outf->lon  = (/lon/)
outf->t    = (/varC/)

;-- close output stream (not necessary)
delete(outf)
