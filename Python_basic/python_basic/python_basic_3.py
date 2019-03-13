with open('./python_basic/dq_unisex_names.csv', 'r') as f:
    names = f.read()

names_list = names.split('\n')
first_five = names_list[0:5]
print (first_five)

#Convert The List Of Strings To A List Of Lists
nested_list = []
for line in names_list:
    comma_list = line.split(',')
    nested_list.append(comma_list)
print(nested_list[0:5])

nested_list = nested_list[0:5]
numerical_list = []
for line in nested_list:
    name = line[0]
    count = float(line[1])
    new_list = [name, count]
    numerical_list.append(new_list)
print(numerical_list[0:5])