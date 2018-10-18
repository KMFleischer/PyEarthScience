;
;  File:
;    TRANS_maps.ncl
;
;  Synopsis:
;    Illustrates how to create a map
;
;  Categories:
;    map plot
;
;  Author:
;    Karin Meier-Fleischer
;  
;  Date of initial publication:
;    September 2018
;
;  Description:
;    This example shows how to create a map.
;
;  Effects illustrated:
;    o  Drawing a map
; 
;  Output:
;    A single visualization is produced.
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide NCL Example: 	TRANS_maps.ncl

  - drawing a map
  
  18-09-03  kmf
;/
;-- open workstation
wks_type = "png"
wks = gsn_open_wks(wks_type,"plot_TRANS_maps_ncl")

;-- which projection do we want to plot
projections = (/"CylindricalEquidistant","Mollweide","Robinson","Orthographic"/)

;-- resource settings
mpres              =  True              ;-- resource object

mpres@vpWidthF     =  0.8               ;-- make the aspect ratio square
mpres@vpHeightF    =  0.8

mpres@mpGridAndLimbOn =  True
mpres@mpPerimOn    =  True
mpres@mpOutlineOn    =  True

do i=0,dimsizes(projections)-1
	mpres@mpProjection = projections(i)
	mpres@tiMainString = projections(i)
	map = gsn_csm_map(wks,mpres)
end do
