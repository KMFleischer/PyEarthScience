;
;  File:
;    TRANS_contour_fill_on_map.ncl
;
;  Synopsis:
;    Illustrates how to create a contour fill plot on a map
;
;  Categories:
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
;    This example shows how to create a contour fill plot on a map.
;
;  Effects illustrated:
;    o  Drawing a contour fill plot
;    o  Drawing a map
; 
;  Output:
;    A single visualization is produced.
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide NCL Example: TRANS_contour_fill_on_map.ncl

  - drawing contour fill plot
  - drawing a map
  
  18-09-04  kmf
;/

f = addfile("../read_data/rectilinear_grid_3D.nc","r")
var = f->t(0,0,:,:)

;-- start the graphics
wks = gsn_open_wks("png","plot_TRANS_contour_fill_on_map_ncl")

;-- resource settings
res                    =  True
res@gsnMaximize        =  True

res@cnFillOn           =  True              ;-- turn on contour level fill
res@cnLineLabelsOn     =  False             ;-- turn off contour line labels

res@mpGridAndLimbOn    =  True              ;-- draw grid lines

;-- create the contour plot
plot = gsn_csm_contour_map(wks,var,res)
