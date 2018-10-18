;
;  File:
;    TRANS_read_netCDF.ncl
;
;  Synopsis:
;    Illustrates how to read a netCDF file
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
;    This example shows how to read a netCDF file.
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
  Transition Guide NCL Example:   TRANS_read_netCDF.ncl

   - read netCDF file
   - retrieve variable informations

  2018-08-21  kmf
;/

print("")

;--  data file name
fname  = "./rectilinear_grid_3D.nc"

;--  open file
f = addfile(fname, "r")

;-- get the sizes of all dimensions in the same order as the names
dims = getfiledimsizes(f)
print("--> Dimensions:              "+ dims)
print("")

;-- retrive the dimension names of the file
dimnames = getfiledimnames(f)
print("--> Dimension names of file: "+ dimnames)
print("")

;-- get only the variable names not the dimension names
varnames = getfilevarnames(f)
print ("--> Variable names:         "+ varnames)
print("")

var_list = ""
do i=0,dimsizes(varnames)-1
   if(any(varnames(i) .eq. dimnames)) then
      continue
   else
      var_list := array_append_record(var_list,varnames(i),0)
   end if
end do
var_list := var_list(1:)
print ("--> Variables:              "+ var_list)
print("")

;-- read variable
var = f->t

;-- get type, rank, shape, dimension names and attributes of the variable
type  = typeof(var)
shape = dimsizes(var)
attr  = getfilevaratts(f,"t")
dimsv = getfilevardimnames(f,"t")
rank  = dimsizes(dims)

print("--> Type:        "+ type)
print("")
print("--> Shape:       "+ shape)
print("")
print("--> Attributes:  "+ attr)
print("")
print("--> Dimensions:  "+ dimsv)
print("")
print("--> Rank:        "+ rank)
print("")

;-- print variable lat content
lat = f->lat
lon = f->lon
printVarSummary(lat)
printVarSummary(lon)

;-- check if variable has attribute

if(isatt(lon,"units")) then
	print("--> Has units attribute: "+lon@units)
end if

