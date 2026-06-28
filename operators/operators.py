#arithmetic Operators

a = 10
b = 3

print("Addition:", a+b)             #13
print("Subtraction:", a-b)          #7
print("Multiplication:", a*b)       #30
print("Division:", a/b)             #3.333333333
print("Floor Division:", a//b)      #3
print("Modulus", a%b)               #1
print("Power:", a ** b)             #1000


# 2. Comparison Operators
a = 10
b = 5

print("Equal:", a == b)                 # False
print("Not Equal:", a != b)             # True
print("Greater Than:", a > b)           # True
print("Less Than:", a < b)              # False
print("Greater Than or Equal:", a >= b) # True
print("Less Than or Equal:", a <= b)    # False



#3. logical Operators
num1 = True    
num2 = True

print("Logical AND:", num1 and num2) # only return true when both true
print("Logical OR:", num1 or num2) #if any 1 condition true then returns true
print("Logical NOT", not num2) #reversex    


#assignment operator 
a = 10

a += 5
print("+= :", a)      # 15

a -= 3
print("-= :", a)      # 12

a *= 2
print("*= :", a)      # 24

a /= 4
print("/= :", a)      # 6.0

a //= 2
print("//= :", a)     # 3.0

a %= 2
print("%= :", a)      # 1.0

a **= 3
print("**= :", a)     # 1.0