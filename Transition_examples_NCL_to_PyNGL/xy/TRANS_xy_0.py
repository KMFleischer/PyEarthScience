#
#  File:
#    TRANS_xy_0.py
#
#  Synopsis:
#    Illustrates how to create a xy plot
#
#  Categories:
#    xy plot
#
#  Author:
#    Karin Meier-Fleischer, based on NCL example
#  
#  Date of initial publication:
#    September 2018
#
#  Description:
#    This example shows how to create a xy plot.
#
#  Effects illustrated:
#    o  Drawing xy plot
# 
#  Output:
#    A single visualization is produced.
#
#  Notes: The data for this example can be downloaded from 
#    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
#   
'''
  Transition Guide Python Example:   TRANS_xy_0.py

  -  Drawing a xy plot

  2018-08-21  kmf
'''
from __future__ import print_function
import numpy
import Ngl

#--  define x and y variables
x = [10., 20., 30., 40., 50., 60., 70., 80., 90.]
y = numpy.array([0., 0.7, 1., 0.7, 0., -0.7, -1., -0.7, 0.],'f')
                 
#-- open a workstation
wkres           =  Ngl.Resources()
wks_type        = "png"            #-- output type of workstation
wks             =  Ngl.open_wks(wks_type,"plot_TRANS_xy_0_py",wkres)

#-- set resources
res             =  Ngl.Resources() #-- generate an res object for plot

#-- draw the plot
plot = Ngl.xy(wks,x,y,res)

#-- done
Ngl.end()
