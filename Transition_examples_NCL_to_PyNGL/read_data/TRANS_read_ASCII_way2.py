#
#  File:
#    TRANS_read_ASCII_way2.py
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
  Transition Guide Python Example:   TRANS_read_ASCII_way2.py

   - read ASCII file
   - retrieve variable informations

	Test_6h.csv
	
	2.00;3.50;5.10;8.20
	2.40;3.10;4.80;8.90
	2.60;3.70;5.30;10.10
	2.75;3.90;5.55;10.25
	3.00;4.10;6.05;10.50

  2018-08-28  kmf
"""
from __future__ import print_function
import numpy as np

print("")

#--  data file name

diri = "/Users/k204045/local/miniconda2/envs/pyn_env/lib/ncarg/data/nug/"
fili = "Test_6h.csv"

#-- delimiter

delim = ';'

#-- read the data

f      = open(diri+fili,'r')
data  = f.readlines()

#-- assign list to append elements

vals = []

for i in data:
	line = i.strip()
	cols = line.split(delim)
	vals.append(cols[:])

#-- convert string to float

vals = np.array(vals).astype(float)

nlines = vals[:,0]
ncols  = vals[0,:]

print("vals: " + str(vals))

#-- rows by column

print("--> columns count:    " + str(len(ncols)))
print("--> lines count:      " + str(len(nlines)))
print("--> rank of vals:     " + str(len(vals.shape)))
print("--> shape vals:       " + str(vals.shape))


exit()
