import json

student = {
    "name": "Harsh",
    "age": 21
}

json_data = json.dumps(student)

print(json_data)
print(type(json_data)) #converted into json format



import json
data = '{"name":"Harsh","age":21}'
python_data = json.loads(data)

print(python_data) #connverted into python data
print(type(python_data))


# Function	Converts
# dumps()	Python → JSON String
# loads()	JSON String → Python



# 1) json.dump() is used to write a Python object into a JSON file.
import json
student = {
    "name": "Harsh",
    "age": 21,
    "city": "Ahmedabad"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully.")



# 2)json.load() is used to read a JSON file and convert it into a Python object. [Run this in TERMINAL if u get error like fileNOTFOUND ]
import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data)
print(type(data))