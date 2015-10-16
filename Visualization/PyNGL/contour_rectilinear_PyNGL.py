"""
  PyEarthScience: PyNGL contour plot example

   - filled contour over map plot
   - rectilinear grid (lat/lon)
   - colorbar
   
  2015-06-04  kmf
"""
import Ngl,Nio

#-- define variables
diri   = "$HOME/NCL/general/data/new_data/"    #-- data directory
fname  = "rectilinear_grid_2D.nc"              #-- data file name

minval =  250.                                 #-- minimum contour level
maxval =  315                                  #-- maximum contour level
inc    =    5.                                 #-- contour level spacing
ncn    = (maxval-minval)/inc + 1               #-- number of contour levels.

#-- open file and read variables
f      =  Nio.open_file(diri + fname,"r")      #-- open data file
temp   =  f.variables["tsurf"][0,::-1,:]       #-- first time step, reverse latitude
lat    =  f.variables["lat"][::-1]             #-- reverse latitudes
lon    =  f.variables["lon"][:]                #-- all longitudes

tempac =  Ngl.add_cyclic(temp[:,:])

#-- open a workstation
wkres                  =  Ngl.Resources()      #-- generate an res object for workstation
wkres.wkColorMap       = "rainbow"             #-- choose colormap
wks_type               = "x11"                 #-- graphics output type
wks                    =  Ngl.open_wks(wks_type,"plot_contour_PyNGL",wkres)  #-- open workstation

#-- set resources
res                    =  Ngl.Resources()      #-- generate an resource object for plot

if hasattr(f.variables["tsurf"],"long_name"):
   res.tiMainString = f.variables["tsurf"].long_name  #-- set main title

res.vpXF                  =  0.1               #-- start x-position of viewport
res.vpYF                  =  0.9               #-- start y-position of viewport
res.vpWidthF              =  0.7               #-- width of viewport
res.vpHeightF             =  0.7               #-- height of viewport

res.cnFillOn              =  True              #-- turn on contour fill.
res.cnLinesOn             =  False             #-- turn off contour lines
res.cnLineLabelsOn        =  False             #-- turn off line labels.
res.cnInfoLabelOn         =  False             #-- turn off info label.
res.cnLevelSelectionMode  = "ManualLevels"     #-- select manual level selection mode
res.cnMinLevelValF        =  minval            #-- minimum contour value
res.cnMaxLevelValF        =  maxval            #-- maximum contour value
res.cnLevelSpacingF       =  inc               #-- contour increment

res.mpGridSpacingF        =  30                #-- map grid spacing

res.sfXCStartV            =  float(min(lon))   #-- x-axis location of 1st element lon
res.sfXCEndV              =  float(max(lon))   #-- x-axis location of last element lon
res.sfYCStartV            =  float(min(lat))   #-- y-axis location of 1st element lat
res.sfYCEndV              =  float(max(lat))   #-- y-axis location of last element lat

res.pmLabelBarDisplayMode = "Always"           #-- turn on the label bar.
res.lbOrientation         = "Horizontal"       #-- labelbar orientation

map = Ngl.contour_map(wks,tempac,res)          #-- draw contours over a map.

#-- end
Ngl.end()

