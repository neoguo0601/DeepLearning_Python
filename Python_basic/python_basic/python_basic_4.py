with open("./python_basic/la_weather.csv", 'r') as f:
    data = f.read()
rows = data.split('\n')

weather_data = []
for row in rows:
    split_row = row.split(",")
    weather_data.append(split_row)
print (weather_data)

weather = []
for row in weather_data:
    weather.append(row[1])
print (weather)

#find a value
animals = ["cat", "dog", "rabbit"]
for animal in animals:
    if animal == "cat":
        print("Cat found")


animals = ["cat", "dog", "rabbit"]
if "cat" in animals:
    print("Cat found")


animals = ["cat", "dog", "rabbit"]
cat_found = "cat" in animals
print (cat_found)


#Dictionaries
students = ["Tom", "Jim", "Sue", "Ann"]
scores = [70, 80, 85, 75]

indexes = [0,1,2,3]
name = "Sue"
score = 0
for i in indexes:
    if students[i] == name:
        score = scores[i]
print(score)


scores = {} #key value
print (type(scores))
scores["Jim"] = 80
scores["Sue"] = 85
scores["Ann"] = 75
print (scores.keys())
print (scores)
print (scores["Sue"])


students = {}
students["Tom"] = 60
students["Jim"] = 70
print (students)

students = {
    "Tom": 60,
    "Jim": 70
}
print (students)
students["Tom"] = 65
print (students)
students["Tom"] = students["Tom"] + 5
print (students)
print ('Tom' in students)


pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]
pantry_counts = {}

for item in pantry:
    if item in pantry_counts:
        pantry_counts[item] = pantry_counts[item] + 1
    else:
        pantry_counts[item] = 1
print (pantry_counts)
