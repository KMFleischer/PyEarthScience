;
;  File:
;    TRANS_panel.ncl
;
;  Synopsis:
;    Illustrates how to create a panel plot
;
;  Categories:
;    contour plot
;    panel plot
;
;  Author:
;    Karin Meier-Fleischer
;  
;  Date of initial publication:
;    September 2018
;
;  Description:
;    This example shows how to create a panel plot.
;
;  Effects illustrated:
;    o  Read netCDF data
;    o  Drawing a contour fill plot
;    o  Creating a panel plot
; 
;  Output:
;    A single visualization is produced.
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide NCL Example: TRANS_panel.ncl

  -  Drawing a contour fill plot
  -  Creating a panel plot
  
  18-09-10  kmf
;/

;-- read data and set variable references
f =  addfile("../read_data/rectilinear_grid_2D.nc", "r")
t =  f->tsurf

;-- open a PNG file
wks = gsn_open_wks("png","plot_TRANS_panel_ncl")

;-- set resources for contour plots
res                     =  True
res@gsnDraw             =  False        ;-- don't draw plot, yet
res@gsnFrame            =  False        ;-- don't advance frame
res@gsnMaximize         =  True         ;-- maximize plots

res@cnFillOn            =  True         ;-- contour fill
res@cnFillPalette       = "cmp_b2r"     ;-- choose color map

res@mpGridAndLimbOn     =  True         ;-- draw grid lines

res@lbLabelBarOn        =  False        ;-- don't draw a labelbar

;-- create 4 plots time step 1 to 4 (NCL index 0-3)
plot_1 = gsn_csm_contour_map(wks,t(0,:,:),res)
plot_2 = gsn_csm_contour_map(wks,t(1,:,:),res)
plot_3 = gsn_csm_contour_map(wks,t(2,:,:),res)
plot_4 = gsn_csm_contour_map(wks,t(3,:,:),res)

;-- panel resources
pnlres                  =  True
pnlres@gsnPanelLabelBar =  True         ;-- common labelbar
pnlres@gsnPanelXWhiteSpacePercent =  5
pnlres@gsnPanelMainFontHeightF =  0.020 ;-- text font size
pnlres@gsnPanelMainString = "TRANS: panel example"

;-- create panel plot
gsn_panel(wks,(/plot_1,plot_2,plot_3,plot_4/),(/2,2/),pnlres)

  