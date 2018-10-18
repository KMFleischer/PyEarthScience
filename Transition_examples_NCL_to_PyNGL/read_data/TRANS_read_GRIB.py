#
#  File:
#    TRANS_read_GRIB.py
#
#  Synopsis:
#    Illustrates how to read an GRIB file
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
#    This example shows how to read an GRIB file.
#
#  Effects illustrated:
#    o  Read GRIB data
# 
#  Output:
#    -
#
#  Notes: The data for this example can be downloaded from 
#    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
#   
"""
  Transition Guide Python Example:   TRANS_read_GRIB.py

   - read GRIB file
   - retrieve variable informations

  2018-08-21  kmf
"""
from __future__ import print_function
import Ngl,Nio

#--  data file name
diri  = "/Users/k204045/local/miniconda2/envs/pyn_env/lib/ncarg/data/grb/"
fname = "MET9_IR108_cosmode_0909210000.grb2"

#--  open file
f = Nio.open_file(diri+fname, "r")

#-- retrieve the variables stored in file
print(f.variables)

#-- read variable, first time step
temp = f.variables["SBTMP_P31_GRLL0"][:,:]

#-- print variable summary
print(f.variables["SBTMP_P31_GRLL0"])

#-- print variable lat content
print(f.variables["gridlat_0"])

#-- print variable lon content
print(f.variables["gridlon_0"])


exit()

