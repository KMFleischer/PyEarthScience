;
;  File:
;    TRANS_masking.ncl
;
;  Synopsis:
;    Illustrates how to mask data
;
;  Categories:
;    map plot
;    contour plot
;
;  Author:
;    Karin Meier-Fleischer
;  
;  Date of initial publication:
;    September 2018
;
;  Description:
;    This example shows how to mask data.
;
;  Effects illustrated:
;    o  Drawing contours on a map
;    o  Using manual levels
;    o  Change map resolution
;    o  Using area specifiers
; 
;  Output:
;    A single visualization is produced.
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide NCL Example: TRANS_masking.ncl

  -  Drawing contours on a map
  -  Using manual levels
  -  Change map resolution
  -  Using area specifiers
  
  18-09-11  kmf
;/

;-- countries where contours should appear
;-- too small countries: "Monaco","San Marino","Vatican City"
mask_specs = (/"Albania","Andorra","Armenia", \
               "Austria","Azerbaijan","Belarus","Belgium", \
               "Bosnia and Herzegovina","Bulgaria","Croatia", \
               "Cyprus","Czech Republic","Denmark","Estonia", \
               "Finland","France","Georgia","Germany","Greece", \
               "Hungary","Iceland","Ireland","Italy","Kazakhstan", \
               "Latvia","Liechtenstein","Lithuania","Luxembourg", \
               "Macedonia","Malta","Moldova","Montenegro", \
               "Netherlands","Norway","Poland","Portugal","Romania", \
               "Russia","Serbia","Slovakia","Slovenia", \
               "Spain","Sweden","Switzerland","Turkey","Ukraine", \
               "United Kingdom"/)

f = addfile("../read_data/rectilinear_grid_3D.nc","r")
var = f->t(0,0,:,:)
lon = f->lon
lat = f->lat

minlat =  30.0
maxlat =  80.0
minlon = -12.0
maxlon =  35.0

;-- start the graphics
wks = gsn_open_wks("png","plot_TRANS_masking_ncl")

;-- resource settings
res                    =  True
res@gsnMaximize        =  True

res@cnFillOn           =  True              ;-- turn on contour level fill
res@cnFillPalette      = "cmp_b2r"          ;-- choose color map
res@cnLinesOn          =  False             ;-- don't draw contour lines
res@cnLineLabelsOn     =  False             ;-- turn off contour line labels
res@cnLevelSelectionMode = "ManualLevels"   ;-- use manual contour line levels
res@cnMinLevelValF     =  250.0             ;-- contour min. value
res@cnMaxLevelValF     =  300.0             ;-- contour max. value
res@cnLevelSpacingF    =    2.5             ;-- contour interval
res@cnFillDrawOrder    = "Predraw"          ;-- contours first; then fills                          

res@lbBoxMinorExtentF  =  0.2               ;-- height of labelbar boxes

res@mpDataBaseVersion  = "MediumRes"        ;-- alias to Ncarg4_1
res@mpDataSetName      = "Earth..4"
res@mpMinLatF          =  minlat
res@mpMaxLatF          =  maxlat
res@mpMinLonF          =  minlon
res@mpMaxLonF          =  maxlon

res@mpOutlineBoundarySets = "National"
res@mpFillBoundarySets    = "NoBoundaries"
res@mpAreaMaskingOn       =  True
res@mpMaskAreaSpecifiers  =  mask_specs
res@mpFillAreaSpecifiers  = (/"land","water"/)

res@mpOceanFillColor       = "gray85"
res@mpLandFillColor        = "gray65"
res@mpInlandWaterFillColor = "gray65"

;-- create the contour plot
plot = gsn_csm_contour_map(wks,var,res)


