;
;  File:
;    TRANS_slice.ncl
;
;  Synopsis:
;    Illustrates how to create a slice plot
;
;  Categories:
;    contour plot
;
;  Author:
;    Karin Meier-Fleischer
;  
;  Date of initial publication:
;    September 2018
;
;  Description:
;    This example shows how to create a slice plot.
;
;  Effects illustrated:
;    o  Read netCDF data
;    o  Drawing a slice plot
; 
;  Output:
;    A single visualization is produced.
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide NCL Example: TRANS_slice.ncl

  -  Read netCDF data
  -  Drawing a slice plot
  
  18-09-04  kmf
;/

fili  = "../read_data/rectilinear_grid_3D.nc"

f     =  addfile(fili, "r")  
var   =  f->t(0,:,{40},:)         ;-- first time step, lat=40N
lon_t =  f->lon                   ;-- lon
lev_t =  f->lev                   ;-- currently 17 levels

;-- define workstation
wks = gsn_open_wks("png","plot_TRANS_slice_ncl")

;-- set resources
res                 =  True
res@gsnMaximize     =  True

;-- viewport resources
res@vpXF            =  0.1        ;-- start x-position of viewport
res@vpYF            =  0.9        ;-- start y-position of viewport
res@vpWidthF        =  0.7        ;-- width of viewport
res@vpHeightF       =  0.6        ;-- height of viewport

res@cnFillOn        =  True       ;-- turn on color fill
res@cnFillPalette   = "temp_diff_18lev"
res@cnLineLabelsOn  =  False      ;-- turns off contour line labels
res@cnInfoLabelOn   =  False      ;-- turns off contour info label
res@cnLevelSelectionMode = "ManualLevels";-- select manual levels
res@cnMinLevelValF  =  200.       ;-- minimum contour value
res@cnMaxLevelValF  =  290.       ;-- maximum contour value
res@cnLevelSpacingF =  5.         ;-- contour increment

res@lbOrientation   = "vertical"  ;-- vertical label bar
res@tiYAxisString   =  var@long_name+"  [hPa]"

res@sfXArray        =  lon_t      ;-- uses lon_t as plot x-axis
res@sfYArray        =  lev_t/100  ;-- uses lev_t in hPa as plot y-axis

res@trYReverse      =  True       ;-- reverses y-axis
res@gsnYAxisIrregular2Log =  True ;-- irregular to linear depth

;-- generate the plot
plot = gsn_csm_contour(wks,var,res)
