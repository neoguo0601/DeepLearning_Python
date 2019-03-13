#Files
#To open a file in Python, we use the open() function
f = open("test.txt", "w")
f.write('123456')
f.write('\n')
f.write('234567')
f.close()

f = open("test.txt", "r")
g = f.read()
print(g)
f.close()



# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

# Code from previous cells
f = open('test.txt', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:3])

#loop
cities = ["Austin", "Dallas", "Houston"]
for city in cities:        
    print(city)


i = 0
while i < 3:
    i += 1
    print (i)

for i in range(15):
    print (i)

cities = [["Austin", "Dallas", "Houston"],['Haerbin','Shanghai','Beijing']]
#print (cities)
for city in cities:
    print(city)
    

for i in cities:
    for j in i:
        print (j)

#Booleans
cat = True
dog = False
print(type(cat))

print(8 == 8) # True
print(8 != 8) # False
print(8 == 10) # False
print(8 != 10) # True

print ("abc" == "abc")
print (["January", "February"] == ["January", "February"])
print (5.0 == 5.0)

rates = [10, 15, 20]
print (rates[0] > rates[1]) # False
print (rates[0] >= rates[0]) # True

#If Statements
sample_rate = 700
greater = (sample_rate > 5)
if 0:                    #This is the conditional statement.
    print(sample_rate)
else:
    print('less than')

t = True
f = True
if t:
    print("Now you see me")
if f:
    print("Now you don't")