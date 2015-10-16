"""
  PyEarthScience: matplotlib xy-plot example

     - marker
     - different line colors
     - legend
     - title
     - x-labels
     - y-labels

  09.10.15  kmf
"""
#-- load python packages
import numpy as np
from matplotlib import pyplot as plt

#-- create x-values
x1 = np.arange(0,8,1)
x2 = np.arange(100)

#-- create y-values
data   = np.arange(1,40,5)
linear = np.arange(100)
square = [v * v for v in np.arange(0,10,0.1)]

#-- create the three lines in one plot
plt.plot(x1, data,   "ob")         # marker o=open circle, b=black
plt.plot(x2, linear, "g")          # no marker, g=green
plt.plot(x2, square, "+r")         # marker +=cross, r=red

#-- plot a legend
plt.legend(('data','linear','square'), loc='upper left')

#-- plot title and axis labels
plt.title('Title string')
plt.xlabel('x-axis label')
plt.ylabel('y-axis label')

#-- show on screen or save the plot to file
plt.show()
#plt.savefig('plot_xy_simple_matplotlib.png')
#plt.savefig('plot_xy_simple_matplotlib_bbox.png', bbox_inches='tight')
