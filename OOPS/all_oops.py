
# class Student:
#     name = "mohit kumar"
#     age = 22
    
# s1 = Student()
# print(s1.age)
# print(s1.name)


# class Student:
#     def __init__(self,name,age):
#         self.fname = name
#         self.age = age 
#         print("created")
    
# s1 = Student("mohit", 22)
# print(s1.fname)
# print(s1.age)



# class Car:
#     car_company = "TATA"
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#         print("created")
        
# s1 = Car("Nexon","red")
# print(s1.name, s1.color)

# s1.car_company = 'SUZUKi'                                                   # i know sirf ese hi kr rha hu . 
# s2 = Car("Safari", "Blue")
# print(s2.name, s2.color)

# print(Car.car_company)
# print(s1.car_company)
# print(s2.car_company)  


# class Student:
#     @staticmethod
#     def college():
#         print("iit bombay")

# Student.college()




#INHERITANCE(SINGLE level)
# class Animal:
#     def eat(self):
#         print("animal is eating")

# class Dog(Animal):
#     def speak(self):
#         print("Dog is barking")

# d = Dog()
# d.eat() #parent method
# d.speak() #Child Method


#Multiple Inheritance (One Child → Multiple Parents)
# class Father:
#     def money(self):
#         print("Father money haha!")
    
# class Mother:
#     def care(self):
#         print("Mothers care hahaha!")

# class Child(Father,Mother):
#     pass

# c = Child()
# c.money()
# c.care()

# Father      Mother
#       \    /
#       Child


# Multilevel Inheritance ⭐
# Grandparent → Parent → Child

# class GrandFather:
#     def land(self):
#         print("Land")
    
# class Father(GrandFather):
#     def house(self):
#         print("House")

# class Son(Father):
#     def bike(self):
#         print("Bike")

# s = Son()
# s.land()
# s.house()
# s.bike()

# Diagram

# GrandFather
#       │
#   Father
#       │
#      Son



# Hierarchical Inheritance ⭐
# One Parent → Multiple Children

# class Animal:
#     def eat(self):
#         print("Eating")

# class Dog(Animal):
#     def bark(self):
#         print("bark")

# class Cat(Animal):
#     def meow(self):
#         print("meow")
    
# d = Dog()
# c = Cat()

# d.eat()
# d.bark()

# c.eat()
# c.meow()

# Diagram

#         Animal
#         /    \
#       Dog    Cat


# 5. Hybrid Inheritance ⭐
# Combination of two or more inheritance types.

# class A:

#     def showA(self):
#         print("A")

# class B(A):

#     def showB(self):
#         print("B")

# class C(A):

#     def showC(self):
#         print("C")

# class D(B, C):

#     def showD(self):
#         print("D")

# obj = D()

# obj.showA()
# obj.showB()
# obj.showC()
# obj.showD()  


#METHOD OVERRIDING
 
# class Animal:

#     def sound(self):
#         print("Animal Sound")

# class Dog(Animal):

#     def sound(self):
#         print("Bark")

# d = Dog()
# d.sound()


# Constructor Inheritance (__init__)

# class Animal:
#     def __init__(self):
#         print("animal Constructor")
    
# class Dog(Animal):
#     pass

# d = Dog()


#ENCAPSULATION 
# class Employee:

#     def __init__(self):
#         self.__salary = 50000

#     def set_salary(self, salary):

#         if salary > 0:
#             self.__salary = salary
#         else:
#             print("Invalid Salary")

#     def get_salary(self):
#         return self.__salary


# e1 = Employee()

# print(e1.get_salary())

# e1.set_salary(70000)

# print(e1.get_salary())


#POLYMORPHISM
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")


class Cat(Animal):
    def sound(self):
        print("Meow")

d = Dog()
c = Cat()

d.sound()
c.sound()



