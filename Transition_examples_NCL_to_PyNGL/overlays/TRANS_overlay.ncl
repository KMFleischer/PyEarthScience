;
;  File:
;    TRANS_overlay.ncl
;
;  Synopsis:
;    Illustrates how to draw a contour fill and a contour line plot over a map
;
;  Categories:
;    map plot
;    contour plot
;    overlay
;
;  Author:
;    Karin Meier-Fleischer
;  
;  Date of initial publication:
;    September 2018
;
;  Description:
;    This example shows how to draw a contour fill and a contour line plot over a map.
;
;  Effects illustrated:
;    o  Read netCDF data
;    o  Drawing a map
;    o  Drawing a contour fill plot
;    o  Drawing a contour line plot
;    o  Using manual levels
;    o  Overlaying contour plots on a map
; 
;  Output:
;    A single visualization is produced.
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide NCL Example: TRANS_overlay.ncl

  -  Read netCDF data
  -  Drawing a map
  -  Drawing a contour fill plot
  -  Drawing a contour lines plot
  -  Using manual levels
  -  Overlaying contour plots on a map

  18-09-07  kmf
;/

f     = addfile("../read_data/rectilinear_grid_3D.nc", "r")
t     = f->t(0,0,:,:)               ;-- 1st time step, 1st level
rhum  = f->rhumidity(0,0,:,:)       ;-- 1st time step, 1st level

;-- define workstation
wks = gsn_open_wks("png","plot_TRANS_overlay_ncl")

;-- set resources
res                  =  True
res@gsnDraw          =  False              ;-- don't draw plot
res@gsnFrame         =  False              ;-- don't advance frame

;-- plot resources for the temperature plot
tres = res
tres@gsnMaximize     =  True               ;-- maximize plot output

tres@cnFillOn        =  True               ;-- turn on color fill
tres@cnFillPalette   = "cmp_b2r"           ;-- set the colormap to be used
tres@cnLinesOn       =  False              ;-- turns off contour line labels
tres@cnLineLabelsOn  =  False              ;-- turns off contour line labels
tres@cnInfoLabelOn   =  False              ;-- turns off contour info label
tres@cnLevelSelectionMode = "ManualLevels" ;-- select manual levels
tres@cnMinLevelValF  =  240.               ;-- minimum contour value
tres@cnMaxLevelValF  =  310.               ;-- maximum contour value
tres@cnLevelSpacingF =  2.                 ;-- contour increment

tres@mpGeophysicalLineColor = "gray50"     ;-- map outline color

tres@mpMinLatF       =  20.0               ;-- min lat
tres@mpMaxLatF       =  60.0               ;-- max lat
tres@mpMinLonF       = -10.0               ;-- min lon
tres@mpMaxLonF       =  40.0               ;-- max lon

tres@tiMainString    = "Colors: temperature, lines: rhumitity"
	                                       ;-- title string
tres@lbBoxMinorExtentF =  0.17             ;-- decrease height of labelbar box

;-- plot resources for the rhumidity plot
rres = res

rres@gsnLeftString   = ""                  ;-- don't draw left string
rres@gsnRightString  = ""                  ;-- don't draw right string

rres@cnInfoLabelOrthogonalPosF = -0.05     ;-- move info label upward

;-- generate tplot, but don't draw it yet
tplot = gsn_csm_contour_map(wks,t,tres)

;-- generate plot2, but don't draw it yet
rplot = gsn_csm_contour(wks,rhum,rres)

;-- overlay rplot on tplot
overlay(tplot, rplot)

;-- draw the plot and advance the frame
draw(tplot)
frame(wks)
