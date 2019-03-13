import numpy
#it will compare the second value to each element in the vector
# If the values are equal, the Python interpreter returns True; otherwise, it returns False
vector = numpy.array([5, 10, 15, 20])
print(vector == 10)

matrix = numpy.array([
                    [5, 10, 15], 
                    [20, 25, 30],
                    [35, 40, 45]
                 ])
print(matrix == 25)

#Compares vector to the value 10, which generates a new Boolean vector [False, True, False, False]. It assigns this result to equal_to_ten
vector = numpy.array([5, 10, 15, 20])
equal_to_ten = (vector == 10)
print (equal_to_ten)
print(vector[equal_to_ten])

matrix = numpy.array([
                [5, 10, 15], 
                [20, 25, 30],
                [35, 40, 45]
             ])
second_column_25 = (matrix[:,1] == 25)
print (second_column_25)
print(matrix[second_column_25, :])

#We can also perform comparisons with multiple conditions
vector = numpy.array([5, 10, 15, 20])
equal_to_ten_and_five = (vector == 10) & (vector == 5)
print (equal_to_ten_and_five)

vector = numpy.array([5, 10, 15, 20])
equal_to_ten_or_five = (vector == 10) | (vector == 5)
print (equal_to_ten_or_five)

vector = numpy.array([5, 10, 15, 20])
equal_to_ten_or_five = (vector == 10) | (vector == 5)
vector[equal_to_ten_or_five] = 50
print(vector)

matrix = numpy.array([
            [5, 10, 15], 
            [20, 25, 30],
            [35, 40, 45]
         ])
second_column_25 = matrix[:,1] == 25
print (second_column_25)
matrix[second_column_25, 1] = 10
print (matrix)

#We can convert the data type of an array with the ndarray.astype() method.
vector = numpy.array(["1", "2", "3"])
print (vector.dtype)
print (vector)
vector = vector.astype(float)
print (vector.dtype)
print (vector)

vector = numpy.array([5, 10, 15, 20])
print(vector.sum())

# The axis dictates which dimension we perform the operation on
#1 means that we want to perform the operation on each row, and 0 means on each column
matrix = numpy.array([
                [5, 10, 15], 
                [20, 25, 30],
                [35, 40, 45]
             ])
print(matrix.sum(axis=1))

matrix = numpy.array([
                [5, 10, 15], 
                [20, 25, 30],
                [35, 40, 45]
             ])
print(matrix.sum(axis=0))


#replace nan value with 0
world_alcohol = numpy.genfromtxt("world_alcohol.txt", delimiter=",")
#print world_alcohol
is_value_empty = numpy.isnan(world_alcohol[:,4])
#print is_value_empty
world_alcohol[is_value_empty, 4] = '0'
alcohol_consumption = world_alcohol[:,4]
alcohol_consumption = alcohol_consumption.astype(float)
total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()
print (total_alcohol)
print (average_alcohol)