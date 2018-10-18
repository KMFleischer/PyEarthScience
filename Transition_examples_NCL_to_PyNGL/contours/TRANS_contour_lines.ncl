;
;  File:
;    TRANS_contour_lines.ncl
;
;  Synopsis:
;    Illustrates how to create a contour line plot
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
;    This example shows how to create a contour line plot.
;
;  Effects illustrated:
;    o  Drawing a contour line plot
; 
;  Output:
;    A single visualization is produced.
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;
/;
  Transition Guide NCL Example: TRANS_contour_line.ncl

  Description:      simple contour line plot

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
wks = gsn_open_wks("png","plot_TRANS_contour_line_ncl")

;-- resource settings
res                    =  True
res@gsnMaximize        =  True

;-- create the contour plot
plot = gsn_csm_contour(wks,T,res)
