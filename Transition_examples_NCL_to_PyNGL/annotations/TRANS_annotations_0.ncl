;
;  File:
;    TRANS_annotations_0.ncl
;
;  Synopsis:
;    Illustrates how to change the axis annotations
;
;  Categories:
;    xy plot
;    tm-resources
;    ti-resources
;
;  Author:
;    Karin Meier-Fleischer
;  
;  Date of initial publication:
;    September 2018
;
;  Description:
;    This example shows how to change the axis annotations.
;
;  Effects illustrated:
;    o  Drawing a xy plot
;    o  Changing the tickmark and axis label resources
; 
;  Output:
;    A single visualization is produced.
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide NCL Example:   TRANS_annotations_0.ncl

  -  Creating xy-plot
  -  Changing axis annotations
  -  Changing axis tickmarks
   
  2018-09-10  kmf
;/

;--  define x and y variables
x = (/ 0.0, 10.0, 20.0, 30.0, 40.0, \
      50.0, 60.0, 70.0, 80.0, 90.0, 100.0/)
y = (/ 0.1,  0.7,  1.0,  0.8,  0.75, \
       0.5,  0.6,  0.62, 0.61, 0.59,  0.4/)

;-- x-axis spacing value, values and labels
xsp     = 20                      ;-- x-axis values spacing
xvalues = ispan(0,100,xsp)        ;-- define x-axis labels
xlabels = xvalues+"~S~o~N~E"      ;-- add "oE" to x-axis labels
             
;-- open a workstation
wks = gsn_open_wks("png","plot_TRANS_anno_0_ncl")

;-- set resources
res                  =  True      ;-- generate an res object for plot
res@gsnMaximize      =  True      ;-- maximize plot size

res@xyLineThicknessF =  4.0       ;-- line width
res@xyLineColor      = "springgreen4"   ;-- line color
res@xyDashPattern    =  3         ;-- line patter 3: dash-dot-dash

res@tiXAxisFont      = 22
res@tiXAxisFontHeightF = 0.014
res@tiXAxisString    = "longitudes";-- x-axis title
res@tiYAxisFont      = 22
res@tiYAxisFontHeightF = 0.014
res@tiYAxisString    = "data"     ;-- y-axis title

res@trXMinF          = min(x)-2.  ;-- x-axis min value
res@trXMaxF          = max(x)+2.  ;-- x-axis max value
res@trYMinF          = min(y)-.1  ;-- y-axis min value
res@trYMaxF          = max(y)+.1  ;-- y-axis max value

;-- x-axis tickmark resources
res@tmXBMode         = "Explicit" ;-- set x-axis labeling to explicit
res@tmXBValues       =  xvalues   ;-- values for x-axis tickmarks
res@tmXBLabels       =  xlabels   ;-- set labels equal to values (type string)
res@tmXBLabelFontColor = "blue"   ;-- x-axis label color
res@tmXBLabelFontHeightF = 0.012  ;-- x-axis font size

res@tmXBMajorLineColor  = "blue"  ;-- bottom x-axis major tickmark color
res@tmXBMinorLineColor  = "blue"  ;-- bottom x-axis minor tickmark color
res@tmXBMajorThicknessF =  2.     ;-- bottom x-axis major tickmarks thickness
res@tmXBMinorThicknessF =  2.     ;-- bottom x-axis minor tickmarks thickness

;-- y-axis resources
res@tmYLLabelFontColor = "red"    ;-- x-axis label color
res@tmYLLabelFontHeightF = 0.012  ;-- x-axis font size

res@tmYLMajorLineColor  = "red"   ;-- bottom x-axis major tickmark color
res@tmYLMinorLineColor  = "red"   ;-- bottom x-axis minor tickmark color
res@tmYLMajorThicknessF =  2.     ;-- bottom x-axis major tickmarks thickness
res@tmYLMinorThicknessF =  2.     ;-- bottom x-axis minor tickmarks thickness

;-- draw the plot
plot = gsn_csm_xy(wks,x,y,res)
