#  DKRZ python functions library:  dkrz_utils.py
# 
#  Functions: 
#
#   - Fahrenheit to Celsius		conv_F2C
#	- Fahrenheit to Kelvin		conv_F2K
#	- Kelvin to Celsius			conv_K2C
#	- Celsius to Kelvin			conv_C2K
#	- Kelvin to Fahrenheit		conv_K2F
#	- Celsius to Fahrenheit		conv_C2F
#   - Compute data anomaly  	comp_anom
#
#
#  Author:
#	Karin Meier-Fleischer
#	meier-fleischer@dkrz.de
#
#  Date:
#	2019/09/10
#
#
"""
  Functions
  
    Conversion routines
    
	    - Fahrenheit to Celsius		conv_F2C
	    - Fahrenheit to Kelvin		conv_F2K
	    - Kelvin to Celsius			conv_K2C
	    - Celsius to Kelvin			conv_C2K
	    - Kelvin to Fahrenheit		conv_K2F
	    - Celsius to Fahrenheit		conv_C2F
	
	Computations
	
		- Compute data anomaly  	comp_anom
		
"""
import numpy as np

#-----------------------------------------------------------
# Convert Fahrenheit to Celsius 
#-----------------------------------------------------------
def conv_F2C(value):
    """Converts degree Fahrenheit to degree Celsius.
       Input parameter:   scalar or array
    """
    value_c = (value-32)*(5/9)
    
    if(hasattr(value_c, 'units')):    
       value_c.attrs.update(units='degC')
    
    return(value_c)

#-----------------------------------------------------------
# Convert Fahrenheit to Kelvin 
#-----------------------------------------------------------
def conv_F2K(value):
    """Converts degree Fahrenheit to Kelvin.
       Input parameter:   scalar or array
    """
    value_k = (value-32)*(5/9)+273.15
    
    if(hasattr(value_k, 'units')):    
       value_k.attrs.update(units='K')
       
    return(value_k)

#-----------------------------------------------------------
# Convert Fahrenheit to Kelvin 
#-----------------------------------------------------------
def conv_F2K_2(value):
    """Converts degree Fahrenheit to Kelvin.
       Input parameter:   scalar or array
    """
    value_c = conv_F2C(value)
    
    return(conv_C2K(value_c))

#-----------------------------------------------------------
# Convert Celsius to Kelvin
#-----------------------------------------------------------
def conv_C2K(value):
    """Converts degree Celsius to Kelvin.
       Input parameter:   scalar or array
    """
    value_k = value+273.15
    
    if(hasattr(value_k, 'units')):    
       value_k.attrs.update(units='K')
       
    return(value_k)

#-----------------------------------------------------------
# Convert Celsius to Kelvin
#-----------------------------------------------------------
def conv_K2C(value):
    """Converts Kelvin to degree Celsius.
       Input parameter:   scalar or array
    """

    if(isinstance(value,(float,int))):
       assert(value >= 0),"value < 0 -> Colder than absolute zero!"
    else:
       assert(value.any() >= 0),"value < 0 -> Colder than absolute zero!"

    value_c = value-273.15

    if(hasattr(value_c, 'units')):    
       value_c.attrs.update(units='degC')
       
    return(value_c)

#-----------------------------------------------------------
# Convert Kelvin to Fahrenheit
#-----------------------------------------------------------
def conv_K2F(value):
    """Converts Kelvin to degree Fahrenheit.
       Input parameter:   scalar or array
    """
    if(isinstance(value,(float,int))):
       assert(value >= 0),"value < 0 -> Colder than absolute zero!"
    else:
       assert(value.any() >= 0),"value < 0 -> Colder than absolute zero!"

    value_f = (value-273.15)*(9/5)+32
    
    if(hasattr(value_f, 'units')):    
       value_f.attrs.update(units='degF')
       
    return(value_f)

#-----------------------------------------------------------
# Convert Celsius to Fahrenheit
#-----------------------------------------------------------
def conv_C2F(value):
    """Converts degree Celsius to degree Fahrenheit.
       Input parameter:   scalar or array
    """
    value_f = (value*(9/5))+32
    
    if(hasattr(value_f, 'units')):    
       value_f.attrs.update(units='degF')
       
    return(value_f)


#-----------------------#
#  Computation routines #
#-----------------------#

#-- Compute the data anomaly
def comp_anom(data):
    """Compute the anomaly of data.
       Input parameter:   scalar or array
    """
    return((data-np.mean(data)))
    
    
    
