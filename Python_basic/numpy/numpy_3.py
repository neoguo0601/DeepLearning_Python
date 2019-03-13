import numpy as np
from numpy import pi

a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)
#the number of axes (dimensions) of the array
print(a.ndim)
print(a.dtype.name)
#the total number of elements of the array
print(a.size)

print(np.zeros ((3,4)) )
print(np.ones( (2,3,4), dtype=np.int32 ))

#To create sequences of numbers
print(np.arange( 10, 30, 5 ))
print(np.arange( 0, 2, 0.3 ))
print(np.arange(12).reshape(4,3))
print(np.random.random((2,3)))

print(np.linspace( 0, 2*pi, 100 ))
print(np.sin(np.linspace( 0, 2*pi, 100 )))

#the product operator * operates elementwise in NumPy arrays
a = np.array( [20,30,40,50] )
b = np.arange( 4 )
print (a) 
print (b)
c = a-b
print (c)
print (b**2)
print (a<35)


#The matrix product can be performed using the dot function or method
A = np.array( [[1,1],
               [0,1]] )
B = np.array( [[2,0],
               [3,4]] )
print (A)
print (B)
print (A*B)
print (A.dot(B))
print (np.dot(B, A)) 


