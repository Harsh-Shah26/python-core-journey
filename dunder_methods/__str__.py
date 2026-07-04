# __str__ method
# Used to define how the whole object should look when printed


# ---------------- Without __str__() ----------------

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


emp1 = Employee("Harsh", 50000)

print("Without __str__():")
print(emp1)          # Prints object address
print(emp1.name)     # Prints specific attribute

print("-" * 40)


# ---------------- With __str__() ----------------

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee(Name={self.name}, Salary={self.salary})"


emp2 = Employee("Harsh", 50000)

print("With __str__():")
print(emp2)          # Calls __str__()
print(emp2.name)     # Still prints only the name