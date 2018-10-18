;
;  File:
;    TRANS_xy_0.ncl
;
;  Synopsis:
;    Illustrates how to create a xy plot
;
;  Categories:
;    xy plot
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
;    o  Drawing xy plot
; 
;  Output:
;    A single visualization is produced.
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide NCL Example:   TRANS_xy_0.ncl

  -  Drawing a xy plot

  2018-08-21  kmf
;/

;--  define x and y variables
x = (/10., 20.0, 30., 40., 50., 60., 70., 80., 90./)
y = (/0., 0.7, 1., 0.7, 0., -0.7, -1., -0.7, 0./)
                 
;-- open a workstation
wks = gsn_open_wks("png","plot_TRANS_xy_0_ncl")

;-- set resources
res                  =  True    ;-- generate an res object for plot
res@gsnMaximize      =  True    ;-- maximize plot size

;-- draw the plot
plot = gsn_csm_xy(wks,x,y,res)
