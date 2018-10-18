#
#  File:
#    TRANS_read_ASCII.py
#
#  Synopsis:
#    Illustrates how to read an ASCII file
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
#    This example shows how to read an ASCII file.
#
#  Effects illustrated:
#    o  Read ASCII data
# 
#  Output:
#    -
#
#  Notes: The data for this example can be downloaded from 
#    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
#   
"""
  Transition Guide Python Example:   TRANS_read_ASCII.py

   - read netCDF file
   - retrieve variable informations

  Input file: Test_6h.csv
	
	2.00;3.50;5.10;8.20
	2.40;3.10;4.80;8.90
	2.60;3.70;5.30;10.10
	2.75;3.90;5.55;10.25
	3.00;4.10;6.05;10.50

  2018-08-28  kmf
"""
from __future__ import print_function
import numpy as np
import Ngl

#--  data file name
diri = "/Users/k204045/local/miniconda2/envs/pyn_env/lib/ncarg/data/nug/"
fili = "Test_6h.csv"

#-- number of lines and columns in input file
nrows = 5
ncols = 4

#-- read all data
vals   = Ngl.asciiread(diri+fili,(nrows,ncols),"float",sep=';')

#-- print information
print("vals: " + str(vals))
print("")
print("--> rank of vals:     " + str(len(vals.shape)))
print("--> shape vals:       " + str(vals.shape))

exit()
