days = 365
print(days)

days = 366
print(days)

#Data Types
#When we assign a value an integer value to a variable, we say that the variable is an instance of the integer class
#The two most common numerical types in Python are integer and float
#The most common non-numerical type is a string
str_test = "China"
int_test = 123
float_test = 122.5

print(str_test)
print(int_test)
print(float_test)

print(type(str_test))
print(type(int_test))
print(type(float_test))

str_eight = str(8)  
print (str_eight)
print (type(str_eight))
eight = 8
str_eight_two = str(eight)

str_eight = "8"
int_eight = int(str_eight)
int_eight += 10
print (type(int_eight))

str_test = 'test'
str_to_int = int(str_test)

"""
Addition: +
Subtraction: -
Multiplication: *
Division: /
Exponent: **
"""

china=10
united_states=100
china_plus_10 = china + 10
us_times_100 = united_states * 100
print(china_plus_10)
print(us_times_100)
print (china**2)

#LIST
months = []
print (type(months))
print (months)
months.append("January")
months.append("February")
print (months)

months = []
months.append(1)
months.append("January")
months.append(2)
months.append("February")
print (months)

temps = ["China", 122.5, "India", 124.0, "United States", 134.1]

countries = []
temperatures = []

countries.append("China")
countries.append("India")
countries.append("United States")

temperatures.append(30.5)
temperatures.append(25.0)
temperatures.append(15.1)

print (countries)
print (temperatures)
china = countries[0]
china_temperature = temperatures[1]
print (china)
print (china_temperature)

int_months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
length = len(int_months) # Contains the integer value 12.
print (length)

int_months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
index = len(int_months) - 1
last_value = int_months[index] # Contains the value at index 11.
print (last_value)
print (int_months[-1])


#Slicing 
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]
# Values at index 2, 3, but not 4.
two_four = months[2:4]
print (two_four)

three_six = months[3:]
print (three_six)
