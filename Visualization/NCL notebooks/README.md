# NCL-ipython-notebooks

NCL notebook examples using an NCL kernel for Jupyter notebooks. 

## Used Software

### NCL kernel

You need to install suvarchal's IPyNCL IPython notebook NCL kernel before you can start using the examples.
https://github.com/suvarchal/IPyNCL

### NCL

Install the newest version of NCL (current version is 6.5.0) from http://ncl.ucar.edu/Download/. I recommend to use conda to install the software.

### CDO

In some notebooks the CDO (Climate Data Operators) are used to do computations. NCL and CDO complement one another very well. See installation instructions https://code.mpimet.mpg.de/projects/cdo/wiki#Installation-and-Supported-Platforms

### ImageMagicks

The scripts use ImageMagicks convert to cut off white space of the plot files. See https://www.imagemagick.org/script/index.php

### Used data sets

Most of the data sets used in the notebooks are part of the NCL software package. If NCL is installed you can find the data sets in the directory $NCARG_ROOT/lib/ncarg/data/nug/.

## Known Problems

The examples won't run correctly online in GitHub because the NCL kernel and ImageMagicks is not installed.
Download the notebooks, install the NCL kernel and ImageMagicks and run the notebooks on your local computer

	jupyter notebook

Sometimes you have to run all cells again when the plots won't be updated. If this won't help save the notebook, click on 'file -> close and halt' and reopen the notebook.
