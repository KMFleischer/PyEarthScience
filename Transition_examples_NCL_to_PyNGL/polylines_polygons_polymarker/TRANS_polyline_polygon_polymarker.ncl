;
;  File:
;    TRANS_polyline_polygon_polymarker.ncl
;
;  Synopsis:
;    Illustrates how to use polylines, polygons and polymarker
;
;  Categories:
;    map plot
;    polylines
;    polygons
;    polymarker
;
;  Author:
;    Karin Meier-Fleischer
;  
;  Date of initial publication:
;    September 2018
;
;  Description:
;    This example shows how to use polylines, polygons and polymarker.
;
;  Effects illustrated:
;    o  Drawing polylines
;    o  Drawing polygons
;    o  Drawing polymarker
; 
;  Output:
;    A single visualization is produced.
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide NCL Example:   TRANS_polyline_polygon_polymarker.ncl

  -  Drawing a map
  -  Drawing polylines
  -  Drawing polygons
  -  Drawing all available (16) polymarkers
   
  2018-09-11  kmf
;/

;-- open a workstation and define colormap
wks = gsn_open_wks("png","plot_TRANS_poly_ncl")

;-- set resources
res                    =  True  
res@gsnDraw            =  False       ;-- don't draw the plot yet
res@gsnFrame           =  False       ;-- don't advance the frame yet
res@gsnMaximize        =  True

res@mpFillOn           =  True

;-- create the map, but don't draw it yet
map = gsn_csm_map(wks,res)

;----------------------------------------------------------------
;-- polyline coordinates (Germany)
;----------------------------------------------------------------
x = (/ 6.,  15.,  15.,   6.,   6./)
y = (/47.5, 47.5, 54.5, 54.5, 47.5/)
  
;-- polyline resources
plres                  =  True
plres@gsLineThicknessF =  2.0         ;-- set line thickness
plres@gsLineColor      = "red"        ;-- set line color

;-- add polyline to map
box_1 = gsn_add_polyline(wks, map, x, y, plres)

;----------------------------------------------------------------
;-- polygon coordinates (Australia)
;----------------------------------------------------------------
x = (/110., 160., 160., 110., 110./)
y = (/-45., -45., -10., -10., -45./)
  
;-- polygon resources
pgres                  =  True
pgres@gsFillColor      = "green"      ;-- fill color
pgres@gsFillOpacityF   =  0.3         ;-- set opacity of polygon

;-- add filled polygon to map
gon_1 = gsn_add_polygon(wks, map, x, y, pgres)

;----------------------------------------------------------------
;-- polygon coordinates (Greenland)
;----------------------------------------------------------------
x = (/-75., -10., -10., -75., -75./)  ;-- define polygon x-array
y = (/ 55.,  55.,  87.,  87.,  57./)  ;-- define polygon y-array

;-- polygon resources
pres                =  True
pres@gsFillColor    = "orange"        ;-- fill color
pres@gsFillOpacityF =  0.2            ;-- set opacity

;-- add polygon to map
gon_2 = gsn_add_polygon(wks, map, x, y, pres)
plres@gsLineColor   = "darkorange"    ;-- set line color
box_2 = gsn_add_polyline(wks, map, x, y, plres)

;----------------------------------------------------------------
;-- polymarker resources
;----------------------------------------------------------------
pmres                  =  True
pmres@gsMarkerColor    = "blue"       ;-- marker color
pmres@gsMarkerIndex    =  1           ;-- use marker 1
pmres@gsMarkerSizeF    =  0.03        ;-- set size of marker
pmres@gsLineThicknessF =  3.          ;-- marker line thickness

;-- unique identifier name for polymarker drawing, here marker_1
marker_1 = gsn_add_polymarker(wks, map, -100., 30., pmres)

;----------------------------------------------------------------
;-- draw all 16 marker on plot using unique identifier name and 
;-- additional map attribute settings
;----------------------------------------------------------------
x = -160.                             ;-- x-position of first marker
y =  -80.                             ;-- y-position of first marker
do i = 0,15                           ;-- 16 different marker
   pmres@gsMarkerIndex  =  i+1
   str = unique_string("poly")        ;-- result is poly0-poly15
;-- add marker to map
   map@$str$ = gsn_add_polymarker(wks, map, x+(i*20.), y+(i*10.), pmres)
end do

;----------------------------------------------------------------
;-- write strings at the bottom of the plot
;----------------------------------------------------------------
txres               =  True
txres@txFontHeightF =  0.014          ;-- default size is HUGE!
txres@txFontColor   = "blue"
txres@txJust        = "CenterLeft"    ;-- puts text on top of bars
dty = 0.23
gsn_text_ndc(wks,"Marker", 0.1, dty, txres)

txres@txFontColor   = "red"
gsn_text_ndc(wks,"Polyline", 0.2, dty, txres)

txres@txFontColor   = "green"
gsn_text_ndc(wks,"Polygon transparent", 0.3, dty, txres)

txres@txFontColor   = "orange"
gsn_text_ndc(wks,"Polyline/Polygon transparent", 0.5, dty, txres)

;-- create the plot and advance the frame
draw(map)
frame(wks)
