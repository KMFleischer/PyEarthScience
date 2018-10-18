; 
;  File:
;    TRANS_vectors.ncl
; 
;  Synopsis:
;    Illustrates how to create a vector plot
; 
;  Categories:
;    vector plot
; 
;  Author:
;    Karin Meier-Fleischer
;  
;  Date of initial publication:
;    September 2018
; 
;  Description:
;    This example shows how to create a vector plot.
; 
;  Effects illustrated:
;    o  Read netCDF data
;    o  Drawing a vector plot
; 
;  Output:
;    A single visualization is produced.
; 
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide NCL Example: TRANS_vectors.ncl

  -  Read netCDF data
  -  Drawing a vector plot
  
  18-09-04  kmf
;/

;-- open a file and read variables
f =  addfile("../read_data/rectilinear_grid_2D.nc", "r")  
u =  f->u10(0,:,:)         		;-- first time step
v =  f->v10(0,:,:)         		;-- first time step

;-- open a workstation
wks =  gsn_open_wks("png","plot_TRANS_vectors_ncl")

;-- resource settings
vcres                    =  True

vcres@vcMinFracLengthF   =  0.3           ;-- length of smallest vector
vcres@vcRefLengthF       =  0.05          ;-- length of reference vector
vcres@vcRefMagnitudeF    =  20.0          ;-- define vector ref mag
vcres@vcRefLengthF       =  0.035         ;-- define length of vec ref  
  
vcres@mpGridAndLimbOn    =  True          ;-- draw grid lines

;-- create the plot
plot = gsn_csm_vector_map(wks,u(::3,::3),v(::3,::3),vcres)
