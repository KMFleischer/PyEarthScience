;
;  File:
;    TRANS_shapefile.ncl
;
;  Synopsis:
;    Illustrates how to use shapefiles
;
;  Categories:
;    map plot
;    contour plot
;    shapefiles
;
;  Author:
;    Karin Meier-Fleischer
;  
;  Date of initial publication:
;    September 2018
;
;  Description:
;    This example shows how to use shapefiles.
;
;  Effects illustrated:
;    o  Reading netCDF data
;    o  Drawing contours on a map
;    o  Using manual levels
;    o  Reading shapefile content
;    o  Drawing shapefile polylines
; 
;  Output:
;    A single visualization is produced.
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide NCL Example: TRANS_shapefile.ncl

  -  Reading netCDF data
  -  Drawing contours on a map
  -  Using manual levels
  -  Reading shapefile content
  -  Drawing shapefile polylines
	
  18-09-11  kmf
;/

f = addfile("$HOME/data/CORDEX/tas_AFR-44_CNRM-CM5_rcp45_r1i1p1_CCLM_4-8-17_ym_20060101-20981231.nc","r")
;-- the input file has no coordinate units degrees_north and degrees_east
;-- this must be set in the script
var            =  f->tas(0,0,:,:)
var&rlat@units = "degrees_north"
var&rlon@units = "degrees_east"

;-- open graphic object
wks =  gsn_open_wks("png","plot_TRANS_shapefile_ncl")

res = True
res@gsnDraw         =  False
res@gsnFrame        =  False
res@gsnMaximize     =  True          ;-- maximize plot in frame
res@gsnAddCyclic    =  False         ;-- don't add a cyclic point

res@cnLevelSelectionMode = "ManualLevels" ;-- set levels
res@cnMinLevelValF  =  240.0         ;-- minimum contour level
res@cnMaxLevelValF  =  310.0         ;-- maximum contour level
res@cnLevelSpacingF =  0.5           ;-- contour level spacing
res@cnFillOn        =  True          ;-- turn on contour fill
res@cnFillPalette   = "NCL_BYR-03"   ;-- choose color map
res@cnFillMode      = "RasterFill"   ;-- turn on contour fill
res@cnLinesOn       =  False         ;-- turn off contour lines

res@lbBoxLinesOn    =  False         ;-- turn off labelbar box lines
res@lbLabelStride   =  10            ;-- skip every other label
res@lbOrientation   = "Vertical"     ;-- labelbar orientation is vertical

mres = res

mres@mpLimitMode    = "LatLon"
mres@mpMinLatF      = -36.0
mres@mpMaxLatF      =  42.6
mres@mpMinLonF      = -23.0
mres@mpMaxLonF      =  60.3

mres@pmTickMarkDisplayMode = "Always"       ; turn on tickmarks

map = gsn_csm_contour_map(wks,var,mres)

;-- open shapefile
shpf = addfile("$HOME/data/Shapefiles/act4567/country.shp", "r")

;-- read data off shapefile
segments = shpf->segments
geometry = shpf->geometry
segsDims = dimsizes(segments)
geomDims = dimsizes(geometry)

;-- read global attributes  
geom_segIndex = shpf@geom_segIndex
geom_numSegs  = shpf@geom_numSegs
segs_xyzIndex = shpf@segs_xyzIndex
segs_numPnts  = shpf@segs_numPnts
numFeatures   = geomDims(0)

;-- add polylines to map
lines = new(segsDims(0),graphic)   ; array to hold polylines

plres             = True           ; resources for polylines
plres@gsLineColor = "black"

lon = shpf->x
lat = shpf->y

segNum = 0       ; Counter for adding polylines
do i=0, numFeatures-1  
   startSegment = geometry(i, geom_segIndex)
   numSegments  = geometry(i, geom_numSegs)
   do seg=startSegment, startSegment+numSegments-1
      startPT = segments(seg, segs_xyzIndex)
      endPT   = startPT + segments(seg, segs_numPnts) - 1
      lines(segNum) = gsn_add_polyline(wks, map, lon(startPT:endPT),\
      lat(startPT:endPT), plres)
      segNum = segNum + 1
   end do
end do

;-- draw map and advance the plot
draw(map)
frame(wks)

