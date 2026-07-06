from collections import ChainMap

# # Combines multiple dictionaries into a single view.

student = {"name": "Harsh"}
marks = {"python":95}

data = ChainMap(student, marks)
print(data)

print(data["name"])