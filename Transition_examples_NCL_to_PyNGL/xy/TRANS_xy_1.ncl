;
;  File:
;    TRANS_xy_1.ncl
;
;  Synopsis:
;    Illustrates how to create a xy plot
;
;  Categories:
;    xy plot
;    lg-resources
;    pm-resources
;
;  Author:
;    Karin Meier-Fleischer
;  
;  Date of initial publication:
;    September 2018
;
;  Description:
;    This example shows how to create a xy plot.
;
;  Effects illustrated:
;    o  Drawing an xy plot
;    o  Using explicit line labels
;    o  Changing the legend settings
; 
;  Output:
;    A single visualization is produced.
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide NCL Example: TRANS_xy_1.ncl

  -  Drawing an xy plot
  -  Using explicit line labels
  -  Changing the legend settings

  18-08-31  kmf
;/

;--  define x and y variables
x = (/10., 20.0, 30., 40., 50., 60., 70., 80., 90./)
y = (/(/0., 0.7, 1., 0.7, 0., -0.7, -1., -0.7, 0./),  \
      (/2., 2.7, 3., 2.7, 2.,  1.3,  1.,  1.3, 2./),  \
      (/4., 4.7, 5., 4.7, 4.,  3.3,  3.,  3.3, 4./)/)
                 
;-- open a workstation
wks = gsn_open_wks("png","plot_TRANS_xy_1_ncl")

;-- set resources
res                  =  True                  ;-- generate an res object for plot
res@gsnMaximize      =  True                  ;-- maximize plot size

res@tiXAxisString    = "x-values"             ;-- x-axis title
res@tiYAxisString    = "y-values"             ;-- y-axis title

;-- xy-plot resources
res@xyLineColors     = (/"red","green","blue"/);-- set 3 different colors for lines
res@xyDashPattern    =  0                     ;-- solid lines
res@xyLineThicknessF =  3.0                   ;-- line thickness for all
res@xyExplicitLegendLabels = (/"t1","t2","t3"/);-- set explicit legend labels

;-- legend resources
res@pmLegendDisplayMode = "Always"            ;-- turn on the drawing
res@pmLegendZone     =  0                     ;-- legend zone: 0 = topLeft; 6 = topRight
res@pmLegendOrthogonalPosF =  0.32            ;-- move the legend upwards
res@lgJustification  = "BottomRight"          ;-- legend justification
res@pmLegendWidthF   =  0.2                   ;-- change width
res@pmLegendHeightF  =  0.10                  ;-- change height
res@pmLegendSide     = "Top"                  ;-- Change location
res@lgPerimOn        =  False                 ;-- turn off the perimeter

;-- draw the plot
plot = gsn_csm_xy(wks,x,y,res)
