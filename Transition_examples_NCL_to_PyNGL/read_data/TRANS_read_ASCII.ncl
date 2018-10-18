;
;  File:
;    TRANS_read_ASCII.ncl
;
;  Synopsis:
;    Illustrates how to read an ASCII file
;
;  Categories:
;    I/O
;
;  Author:
;    Karin Meier-Fleischer
;  
;  Date of initial publication:
;    September 2018
;
;  Description:
;    This example shows how to read an ASCII file.
;
;  Effects illustrated:
;    o  Read ASCII data
; 
;  Output:
;    -
;
;  Notes: The data for this example can be downloaded from 
;    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
;   
/;
  Transition Guide NCL Example:   TRANS_read_ASCII.ncl

   - read ASCII file
   - retrieve variable informations

  Input file: Test_6h.csv
	
	2.00;3.50;5.10;8.20
	2.40;3.10;4.80;8.90
	2.60;3.70;5.30;10.10
	2.75;3.90;5.55;10.25
	3.00;4.10;6.05;10.50
	
  2018-08-27  kmf
;/

;--  data file name
diri = "/Users/k204045/local/miniconda2/envs/pyn_env/lib/ncarg/data/nug/"
fili = "Test_6h.csv"

;-- number of lines and columns in input file
nrows = 5
ncols = 4

;-- read the data
vals  = asciiread(diri+fili,(/nrows,ncols/), "float")

print("vals: " + vals)
print("")
print("--> rank of vals:     " + dimsizes(dimsizes(vals)))
print("--> shape vals:       " + dimsizes(vals))

