;
;  File:
;    TRANS_streamline.ncl
;
;  Synopsis:
;    Illustrates how to create a streamline plot
;
;  Categories:
;    streamline plot
;
;  Author:
;    Karin Meier-Fleischer
;  
;  Date of initial publication:
;    September 2018
;
;  Description:
;    This example shows how to create a streamline plot.
;
;  Effects illustrated:
;    o  Read netCDF data
;    o  Drawing a streamline plot
; 
;  Output:
;    A single visualization is produced.
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide NCL Example: TRANS_streamline.ncl

  -  Read netCDF data
  -  Drawing a streamline plot

  18-09-04  kmf
;/

;-- open a file and read variables
f =  addfile("../read_data/rectilinear_grid_2D.nc", "r")  
u =  f->u10(0,:,:)         		;-- first time step
v =  f->v10(0,:,:)         		;-- first time step

;-- open a workstation
wks =  gsn_open_wks("png","plot_TRANS_streamline_ncl")

;-- resource settings
stres                    =  True

stres@mpGridAndLimbOn    =  True          ;-- draw grid lines

;-- create the plot
plot = gsn_csm_streamline_map(wks,u(::3,::3),v(::3,::3),stres)
