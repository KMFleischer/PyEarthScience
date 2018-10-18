;
;  File:
;    TRANS_contour_fill.ncl
;
;  Synopsis:
;    Illustrates how to create a contour fill plot
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
;    This example shows how to create a contour fill plot.
;
;  Effects illustrated:
;    o  Drawing a contour fill plot
; 
;  Output:
;    A single visualization is produced.
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;  
/;
  Transition Guide NCL Example: TRANS_contour_fill.ncl

  Description:      simple contour fill plot

  18-09-03  kmf
;/

;-- create some dummy data to contour
T    = new((/25,25/),float)
vals = ispan(-12,12,1)
jspn = vals*vals
ispn = vals*vals

do i=0,dimsizes(jspn)-1
   T(i,:) = tofloat(jspn + ispn(i))
end do

T = 100.0 - sqrt(64 * T)

;-- start the graphics
wks = gsn_open_wks("png","plot_TRANS_contour_fill_ncl")

;-- resource settings
res                    =  True
res@gsnMaximize        =  True

res@cnFillOn           =  True              ;-- turn on contour level fill
res@cnLineLabelsOn     =  False             ;-- turn off contour line labels
res@cnFillPalette      = "ncl_default"

res@lbLabelFontHeightF =  0.018             ;-- make labelbar labels smaller
res@lbLabelAlignment   = "BoxCenters"
res@lbLabelPosition    = "Center"
res@lbLabelStrings     =  ispan(-30,110,10) ;-- label strings
res@lbOrientation      = "vertical"         ;-- vertical labelbar

;-- create the contour plot
plot = gsn_csm_contour(wks,T,res)
