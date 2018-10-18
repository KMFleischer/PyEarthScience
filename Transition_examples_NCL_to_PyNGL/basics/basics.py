#-- this is a comment

"""
This is a block comment
which can have multiple lines.
"""

#-- define variable 
var = 12
print(var)
print(type(var))

#-- define variable vf of type float
vf = 2.0

print(vf)
print(type(vf))

#-- convert var to float
var = float(var)

print(var)
print(type(var))

#-- convert var to string
var = str(var)

print(var)
print(type(var))

#-- define an array
array = [0,3,6,9]

print(array)

#-- its better to use NumPy for arrays
import numpy as np
array = np.array(array)

print(array)

#-- overwrite nparray with 0
array[:] = 0
print(array)

#-- overwrite nparray with 1
array[:] = 1
print(array)

#-- addition of arrays
a = np.array([1,2,3,4])
b = np.array([0,1,1,0])
c = np.array(a + b)
print(c)

#-- e.g. create new arrays; sizes: n=4, q=2x3x5, l=100 (missing value 1e20)
n = np.zeros(4,np.int)
q = np.zeros(shape=(2,3,5),dtype=float)
l = np.full(100,1.0e20)
print(n)
print(q)
print(l)

#-- array indexing (doesn't include the last index)
a_sub = a[1:3]
print(a_sub)
a_sub = a[1:4]
print(a_sub)

#-- reverse array
a_rev = a[::-1]
print(a_rev)

#-- select every second element
a_sec = a[::2]
print(a_sec)

#-- find values in array
ind_not0 = np.nonzero(b != 0)
print(b[ind_not0])


#-- generate equaly spaced arrays
i = np.arange(0,10,1)
print(i)

lat = np.arange(-180.0,210.0,30.0)
print(lat)


#-- dimension reshaping 
ra = np.array([[[1,2,3,4],[5,6,7,8],[5,4,2,0]],\
               [[1,2,3,4],[5,6,7,8],[5,4,2,0]]])
print(ra.shape)
ra1d = np.ravel(ra)
print(ra1d)
print(len(ra1d))
print(ra.shape)
print("---")
ra3d = np.reshape(ra,ra.shape)
print(ra3d.shape)


#-- if statements
t = 99
if t == 0:
	print("t = 0")
elif t == 1:
	print("t = 1")
else:
	print("t = ",t)


#-- for loop
for j in range(0,5,1):
	print("j = ",j)

str_array = ["Hamburg","Munich","Berlin"]

for city in str_array:
	print(city)

#-- while loops
j = 0
while(j <= 5):
	print("j = ",j)
	if j == 3:
		print("--> j = ",j)
	j = j + 1



