# Polymorphism: One Interface, Many Forms


# Method Overriding
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

print("-" * 40)


# Built-in Polymorphism
print(len("Harsh"))
print(len([1, 2, 3, 4]))
print(len((10, 20)))

print("-" * 40)


# Method Overloading Like Behavior using Default Argument
class Calculator:

    def add(self, a, b, c=0):
        print(a + b + c)

calc = Calculator()
calc.add(10, 20)
calc.add(10, 20, 30)

print("-" * 40)


# Duck Typing
class Car:

    def start(self):
        print("Car Started")

class Bike:

    def start(self):
        print("Bike Started")

def start_vehicle(vehicle):
    vehicle.start()

car = Car()
bike = Bike()

start_vehicle(car)
start_vehicle(bike)

print("-" * 40)

# Operator Overloading
print(10 + 20)
print("Hello " + "World")
print([1, 2] + [3, 4])