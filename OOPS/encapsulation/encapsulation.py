# Encapsulation: Data Hiding and Controlled Access

class Employee:

    def __init__(self):
        self.__salary = 50000

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid Salary")

    def get_salary(self):
        return self.__salary


emp = Employee()

print(emp.get_salary())

emp.set_salary(80000) 
print(emp.get_salary())

emp.set_salary(-10000) # suppsoe someone do this 
print(emp.get_salary())