#
#  File:
#    TRANS_write_ASCII.py
#
#  Synopsis:
#    Illustrates how to write an ASCII file
#
#  Categories:
#    I/O
#
#  Author:
#    Karin Meier-Fleischer, based on NCL example
#  
#  Date of initial publication:
#    September 2018
#
#  Description:
#    This example shows how to write an ASCII file.
#
#  Effects illustrated:
#    o  Reading netCDF file
#    o  Converting data from Kelvin to degC
#    o  Writing ASCII data to new file
# 
#  Output:
#    ASCII data file.
#
#  Notes: The data for this example can be downloaded from 
#    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
#   
"""
  Transition Guide Python Example:   TRANS_write_ASCII.py

  -  Reading netCDF file
  -  Converting data from Kelvin to degC
  -  Writing ASCII data to new file
   
  2018-08-30  kmf
"""
from __future__ import print_function
import os, sys
import numpy as np
import Ngl,Nio

#--  data file name
fname  = "../read_data/rectilinear_grid_3D.nc"

#--  open file
f = Nio.open_file(fname, "r")

#-- read variable, first time step, first level
var = f.variables["t"][0,0,:,:]

#--  convert var from Kelvin to degC while retaining the missing values
var = var - 273.15
print(var)

# -- write var to an ASCII file
os.system("/bin/rm -f data_py.asc")        #-- delete file
sys.stdout = open("data_py.asc","w")       #-- redirect stdout to file
for i in range(0,10):
	for j in range(0,10):
		print "%10.6f" % (var[i,j])     #-- write to file

exit()

