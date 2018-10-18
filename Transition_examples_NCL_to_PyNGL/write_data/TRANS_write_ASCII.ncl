;
;  File:
;    TRANS_write_ASCII.ncl
;
;  Synopsis:
;    Illustrates how to write an ASCII file
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
;    This example shows how to write an ASCII file.
;
;  Effects illustrated:
;    o  Reading netCDF file
;    o  Converting data from Kelvin to degC
;    o  Writing ASCII data to new file
; 
;  Output:
;    ASCII data file.
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide NCL Example:   TRANS_write_ASCII.ncl

  -  Reading netCDF file
  -  Converting data from Kelvin to degC
  -  Writing ASCII data to new file
   
  2018-08-31  kmf
;/

;--  data file name
fname  = "../read_data/rectilinear_grid_3D.nc"

;--  open file
f = addfile(fname, "r")

;-- read variable, first time step, first level
var = f->t(0,0,:,:)
var = var - 273.15

print(var)

;-- write var to an ASCII file
asciiwrite("data_ncl.asc",sprintf("%10.6f",var(0:9,0:9)))
