import array as arr
import numpy as np

#basic 
x = arr.array('i', (1,2,3))

print(x)

x.append(4)
print(x)

x.append('l')
print(x)

"float"
x = arr.array('d', (1,2,3))



#Basic array with Numpy
ar = np.array((1,2,3,4,5))
print(ar)

for i in ar:
    print(i)

ar = np.array((1,2,3,4.0))
print(ar)


#Storing the data in different Dimensions
#0D array
zeroDarr = np.array([13])
zeroDarr.ndim
print(zeroDarr)

#1D array
oneDarr = np.array([1,2,3,4,5])
oneDarr.ndim
print(oneDarr)
oneDarr[4]



#2D array
twoDarr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
twoDarr.ndim
print(twoDarr)

twoDarr[0,0]
twoDarr[1,2]
twoDarr[0,4]


#3D array
threeDarr = np.array([[[1,2,3,4,5], [6,7,8,9,10]], [[11,12,13,14,15], [16,17,18,19,20]]])
threeDarr.ndim
print(threeDarr)
threeDarr[0,1,1]
threeDarr[1,0,2]

#Accessing /Indexing Array

#one Dim
print(oneDarr)
oneDarr[2]

#three Dim
print(threeDarr)
threeDarr[1]
threeDarr[1,0]
threeDarr[1,0,3]

print(threeDarr)
threeDarr[0]
threeDarr[0,1]
threeDarr[0,1,-1]

