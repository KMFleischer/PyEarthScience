;
;  File:
;    TRANS_bar_chart.ncl
;
;  Synopsis:
;    Illustrates how to create a bar chart plot
;
;  Categories:
;    bar chart plots
;    xy plot
;
;  Author:
;    Karin Meier-Fleischer
;  
;  Date of initial publication:
;    September 2018
;
;  Description:
;    This example shows how to create a bar chart plot.
;
;  Effects illustrated:
;    o  Drawing a bar chart plot
;    o  Customizing a x-axis labels
; 
;  Output:
;    A single visualization is produced.
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;     
/;
  Transition Guide NCL Example: TRANS_bar_chart.ncl

  - bar chart
  - x-labels

  18-09-03  kmf
;/

;-- create random x- and y-values
x = fspan(1.0,12.0,12)
y = (/ 8, 5, 11, 6, 9, 9, 6, 2, 4, 1, 3, 3/)

;-- open a workstation
 wks = gsn_open_wks("png","plot_TRANS_bar_chart_ncl")

;-- set resources
res                       =  True
res@gsnMaximize           =  True
res@gsnXYBarChart         =  True             ;-- use bar chart style
res@gsnXYBarChartBarWidth =  0.3              ;-- width of bars
res@gsnXYBarChartColors   = "blue"            ;-- color

res@tiXAxisString         = "x-values"        ;-- x-axis title
res@tiYAxisString         = "y-values"        ;-- y-axis title

res@trXMinF               =  0.0              ;-- x-axis min value
res@trXMaxF               = 13.0              ;-- x-axis max value
res@trYMinF               =  0.0              ;-- y-axis min value
res@trYMaxF               = 12.0              ;-- y-axis max value

res@tmXBMode              = "Explicit"        ;-- explicit labels
res@tmXBValues            =  ispan(1,12,1)    ;-- bottom x-axis tickmark values
res@tmXBLabels            = (/"Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep", \
                              "Oct","Nov","Dec"/) ;-- x-axis labels
res@tmXBLabelFontHeightF  =  0.015            ;-- x-axis font size

;-- create the plot
plots = gsn_csm_xy(wks, x, y, res)
