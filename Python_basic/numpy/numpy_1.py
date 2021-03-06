import numpy

#The numpy.array() function can take a list or list of lists as input. When we input a list, we get a one-dimensional array as a result:
vector = numpy.array([5, 10, 15, 20])
#When we input a list of lists, we get a matrix as a result:
matrix = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print (vector)
print (matrix)

#We can use the ndarray.shape property to figure out how many elements are in the array
vector = numpy.array([1, 2, 3, 4])
print(vector.shape)
#For matrices, the shape property contains a tuple with 2 elements.
matrix = numpy.array([[5, 10, 15], [20, 25, 30]])
print(matrix.shape)

#Each value in a NumPy array has to have the same data type
#NumPy will automatically figure out an appropriate data type when reading in data or converting lists to arrays. 
#You can check the data type of a NumPy array using the dtype property.
numbers = numpy.array([1, 2, 3, 4])
print(numbers.dtype)

world_alcohol = numpy.genfromtxt("world_alcohol.txt", delimiter=",")
print(type(world_alcohol))

#When NumPy can't convert a value to a numeric data type like float or integer, it uses a special nan value that stands for Not a Number
#nan is the missing data
#1.98600000e+03 is actually 1.986 * 10 ^ 3
print(world_alcohol)

world_alcohol = numpy.genfromtxt("world_alcohol.txt", delimiter=",", dtype="U75", skip_header=1)
print(world_alcohol)

uruguay_other_1986 = world_alcohol[1,4]
third_country = world_alcohol[2,2]
print (uruguay_other_1986)
print (third_country)


vector = numpy.array([5, 10, 15, 20])
print(vector[0:3])  

matrix = numpy.array([
                    [5, 10, 15], 
                    [20, 25, 30],
                    [35, 40, 45]
                 ])
print(matrix[:,1])

matrix = numpy.array([
                    [5, 10, 15], 
                    [20, 25, 30],
                    [35, 40, 45]
                 ])
print(matrix[:,0:2])

matrix = numpy.array([
                    [5, 10, 15], 
                    [20, 25, 30],
                    [35, 40, 45]
                 ])
print(matrix[1:3,0:2])

