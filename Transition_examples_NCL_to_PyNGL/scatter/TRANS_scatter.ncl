;
;  File:
;    TRANS_scatter.ncl
;
;  Synopsis:
;    Illustrates how to create a scatter plot
;
;  Categories:
;    xy plot
;    polymarker
;
;  Author:
;    Karin Meier-Fleischer
;  
;  Date of initial publication:
;    September 2018
;
;  Description:
;    This example shows how to create a scatter plot.
;
;  Effects illustrated:
;    o  Create random data
;    o  Drawing a scatter plot
;    o  polymarker
; 
;  Output:
;    A single visualization is produced.
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide NCL Example: TRANS_scatter.ncl

  -  Use different markers
  -  Use different marker colors
  -  Drawing a legend with markers and labels inside plot

  18-09-07  kmf
;/

;-- generate random data
npts  = 100
x     = ispan(1,npts,1)
data1 = random_uniform(0.1,50,npts)
data2 = random_uniform(0.1,50,npts)

;-- create data array containing data1 and data2
data = new((/2,npts/),typeof(data1))
data(0,:) =  data1
data(1,:) =  data2

;-- set explicit labels for legend
labels = (/"data 1","data 2"/)

;-- open workstation
wks = gsn_open_wks("png","plot_TRANS_scatter_ncl")
 
;-- set resources
res                  = True
res@gsnMaximize      = True                 ;-- maximize plot output
res@tiMainString     = "Marker Plot"        ;-- add title

;-- make plot space larger to have enough space for legend 
res@trYMinF          = min(data1)-20.       ;-- y-axis minimum
res@trYMaxF          = max(data1)+20.       ;-- y-axis maximum
res@trXMinF          = min(x)-5.            ;-- y-axis minimum
res@trXMaxF          = max(x)+5.            ;-- y-axis maximum

res@tmLabelAutoStride = True                ;-- use nice tick mark labels

res@xyMarkLineModes  = (/"Markers","Markers"/);-- set mark line mode
res@xyMarkers        = (/10,16/)            ;-- choose marker types 
res@xyMarkerColors   = (/"red","blue"/)     ;-- choose marker colors

res@lgJustification  = "TopRight"           ;-- position of legend
res@lgLabelFontHeightF = 0.01               ;-- legend label font size
res@lgItemOrder      = (/1,0/)              ;-- reverse the legend
res@xyExplicitLabels = labels               ;-- use explicit legend labels

res@pmLegendDisplayMode = "Always"          ;-- display legend always
res@pmLegendWidthF   = 0.10                 ;-- legend width
res@pmLegendHeightF  = 0.06                 ;-- legend height
res@pmLegendOrthogonalPosF = -0.22          ;-- move legend up
res@pmLegendParallelPosF = 0.98             ;-- move legend right

;-- create the plot
plot = gsn_csm_xy(wks,x,data,res)
