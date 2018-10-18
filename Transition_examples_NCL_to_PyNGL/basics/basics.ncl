;-- this is a comment

/;
This is a block comment
Which can have multiple lines.
;/

;-- define variable var 
var = 12
print(typeof(var))

;-- define variable vf of type float
vf = 2.0
print(typeof(vf))

;-- convert var to float
var := tofloat(var)
print(typeof(var))

;-- convert var to string
var := tostring(var)
print(typeof(var))

;-- define an array
array = (/0,3,6,9/)
print(array)

;-- overwrite array with 0
array = 0
print(array)

;-- overwrite array with 1
array = 1
print(array)

;-- addition of arrays
a = (/1,2,3,4/)
b = (/0,1,1,0/)
c = a + b
print(c)

;-- create new arrays; sizes: n=4, q=2x3x5, l=100 (missing value 1e20)
n = new(4,integer)
n = 0
q = new((/2,3,5/),float)
q  = 0.
l = new(100,float,1e20)
print(n)
print(q)
print(l)

;-- indexing (subscripting)
a_sub = a(1:3)
print(a_sub)

;-- reverse array
a_rev = a(::-1)
print(a_rev)

;-- select every second element
a_sec = a(::2)
print(a_sec)


;-- find values in array
ind_not0 = ind(b .gt. 0)
print(b(ind_not0))

;-- generate equaly spaced arrays
i = ispan(0,10,1)
print(i)

lat = fspan(-180.0,180.0,13)
print(lat)


;-- dimension reshaping 
ra = (/(/(/1,2,3,4/),(/5,6,7,8/),(/5,4,2,0/)/), \
       (/(/1,2,3,4/),(/5,6,7,8/),(/5,4,2,0/)/) /)
print(dimsizes(ra))
ra1d = ndtooned(ra)
print(""+ra1d)
print(dimsizes(ra1d))
ra3d = onedtond(ra,dimsizes(ra))
print(dimsizes(ra3d))


;-- if statements
t = 99
if(t .eq. 0) then
   print("t = 0")
elseif (t .eq. 1) then
   print("t = 1")
else
   print("t = "+t)
end if


;-- do loop
do j=0,5
  print("j = "+j)
end do

str_array = (/"Hamburg","Munich","Berlin"/)
do k = 0,dimsizes(str_array)-1
	print(str_array(k)+"")
end do

;-- while loops
j = 0
do while(j .lt. 5)
   print("j = "+j)
   if(j .eq. 3) then
     print("--> j = "+j)
   end if
   j = j + 1
end do










