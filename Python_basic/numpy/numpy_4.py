import numpy as np

B = np.arange(3)
print (B)
print (np.exp(B))
print (np.sqrt(B))

#Return the floor of the input
a = np.floor(10*np.random.random((3,4)))
#print a

print (a.shape)
## flatten the array
print (a.ravel())
a.shape = (6, 2)
print (a) 
print (a.T)
a.resize((2,6))
print (a)

#If a dimension is given as -1 in a reshaping operation, the other dimensions are automatically calculated:
a = a.reshape(3,-1)
print (a)

a = np.floor(10*np.random.random((2,2)))
b = np.floor(10*np.random.random((2,2)))
print (a)
print ('---')
print (b)
print ('---')
print (np.hstack((a,b)))

a = np.floor(10*np.random.random((2,12)))
print (a)
print (np.hsplit(a,3))
print (np.hsplit(a,(3,4)))   # Split a after the third and the fourth column
a = np.floor(10*np.random.random((12,2)))
print (a)
print (np.vsplit(a,3))


#Simple assignments make no copy of array objects or of their data.
a = np.arange(12)
b = a
# a and b are two names for the same ndarray object
print (b is a)
b.shape = 3,4
print (a.shape)
print (id(a))
print (id(b))


#The view method creates a new array object that looks at the same data.
c = a.view()
print(c is a)
c.shape = 2,6
print (a.shape)
c[0,4] = 1234
print(a)


#The copy method makes a complete copy of the array and its data.
d = a.copy() 
d is a
d[0,0] = 9999
print (d)
print (a)

