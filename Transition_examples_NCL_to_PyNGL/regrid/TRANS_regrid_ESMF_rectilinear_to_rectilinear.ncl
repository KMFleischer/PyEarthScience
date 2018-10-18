;
;  File:
;    TRANS_regrid_ESMF_rectilinear_to_rectilinear.ncl
;
;  Synopsis:
;    Illustrates how to create a contour fill plot on a map
;
;  Categories:
;    contour plot
;    map plot
;
;  Author:
;    Karin Meier-Fleischer, based on NCL example
;  
;  Date of initial publication:
;    October 2018
;
;  Description:
;    This example shows how to create a contour fill plot on a map.
;
;  Effects illustrated:
;    o  Drawing a contour fill plot
;    o  Drawing a map
; 
;  Output:
;    Two visualizations are produced, original data and regridded data.
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide Python Example: 	TRANS_regrid_ESMF_rectilinear_to_rectilinear.ncl

  - read netCDF file
  - regrid to higher resolution grid 
  - drawing contour fill plots
  - drawing a map
  
  18-10-15  kmf
;/
;load "$NCARG_ROOT/lib/ncarg/nclscripts/esmf/ESMF_regridding.ncl"

;--  open file and read variables
data = addfile("../read_data/rectilinear_grid_3D.nc","r")

t   = data->t(0,0,:,:)
lat = data->lat
lon = data->lon

;-- destination lat/lon
dst_lat = fspan(-89.5,89.5,180)
dst_lon = fspan(-179.5,179.5,360)

printVarSummary(lat)
printVarSummary(lon)
printVarSummary(dst_lat)
printVarSummary(dst_lon)

;-- set resources
Opt                =  True
Opt@InterpMethod   = "bilinear"                         ;-- interpolation method
Opt@ForceOverwrite =  True                              ;-- force overwrite 
Opt@SrcMask2D      =  where(.not.ismissing(t),1,0)      ;-- what to mask
Opt@DstGridType    = "rectilinear"                      ;-- Destination grid
Opt@DstGridLon     =  dst_lon
Opt@DstGridLat     =  dst_lat

;-- call ESMF_regrid
t_regrid = ESMF_regrid(t,Opt)

;-- plotting
wks = gsn_open_wks("png","plot_TRANS_regrid_ESMF_ncl")

res                 =  True
res@gsnFrame        =  False
res@cnFillOn        =  True
res@cnFillPalette   = "NCL_default"
res@cnLineLabelsOn  =  False
res@cnLevelSelectionMode = "ManualLevels"   ;-- use manual contour line levels
res@cnMinLevelValF  =  235.0                ;-- contour min. value
res@cnMaxLevelValF  =  310.0                ;-- contour max. value
res@cnLevelSpacingF =    5.0                ;-- contour interval
res@lbOrientation   = "horizontal"
res@mpGridAndLimbOn =  True                 ;-- draw grid lines

plot = gsn_csm_contour_map(wks,t_regrid,res)

frame(wks)

plot = gsn_csm_contour_map(wks,t,res)

frame(wks)

;-- clean-up
system("rm -rf source_grid_file.nc destination_grid_file.nc weights_file.nc PET0.RegridWeightGen.Log")

