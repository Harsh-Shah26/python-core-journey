# ============================
# 1. Single Inheritance
# ============================
class Animal:
    def eat(self):
        print("Animal is Eating")

class Dog(Animal):
    def bark(self):
        print("Dog is Barking")

d = Dog()
d.eat()
d.bark()


# ============================
# 2. Multiple Inheritance
# ============================
class Father:
    def money(self):
        print("Father's Money")

class Mother:
    def care(self):
        print("Mother's Care")

class Child(Father, Mother):
    pass

c = Child()
c.money()
c.care()


# ============================
# 3. Multilevel Inheritance
# ============================
class GrandFather:
    def land(self):
        print("Land")

class Father(GrandFather):
    def house(self):
        print("House")

class Son(Father):
    def bike(self):
        print("Bike")

s = Son()
s.land()
s.house()
s.bike()


# ============================
# 4. Hierarchical Inheritance
# ============================
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Bark")

class Cat(Animal):
    def meow(self):
        print("Meow")

d = Dog()
c = Cat()

d.eat()
d.bark()

c.eat()
c.meow()


# ============================
# 5. Hybrid Inheritance
# ============================
class A:
    def showA(self):
        print("A")

class B(A):
    def showB(self):
        print("B")

class C(A):
    def showC(self):
        print("C")

class D(B, C):
    def showD(self):
        print("D")

obj = D()

obj.showA()
obj.showB()
obj.showC()
obj.showD()


# ============================
# Method Overriding
# ============================
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()
d.sound()


# ============================
# super()
# ============================
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Bark")

d = Dog()
d.sound()


# ============================
# Constructor Inheritance
# ============================

class Animal:
    def __init__(self):
        print("Animal Constructor")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog Constructor")

d = Dog()


# ============================
# Parent Constructor Parameters
# ============================

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Tommy", "Labrador")
print(d.name)
print(d.breed)

# ============================
# MRO
# ============================

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

obj = D()
obj.show()
print(D.mro())