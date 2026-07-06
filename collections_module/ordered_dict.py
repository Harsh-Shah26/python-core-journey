from collections import OrderedDict

#used wehn dict are unoredred python3.6
student = OrderedDict()

student["name"] = "Harsh"
student["age"] = 21
student["city"] = "Ahmedabad"

print(student)
student.move_to_end("name")
print(student)