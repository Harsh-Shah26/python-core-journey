# Q1
# Print the length of the string.

text = "Python Programming"
print(len(text))


# Q2
# Print only the first character.
text = "Python"
print(text[0])


# Q3
# Print the last character using negative indexing.
text = "Backend"
print(text[-1])


# Q4
# Print only "Programming" using slicing.
text = "Python Programming"
print(text[7:])
print(text[-11:]) # also prints programming
print(text[:-3]) #now python starts from 0 to end and remove -3 words


# Q5 Convert the string into uppercase.
text = "django"
print(text.upper())


# Q6 Replace "banana" with "cherry".
fruit = "i love banana"
print(fruit.replace("banana", "cherry"))


# Q7 Count how many times 'a' appears.
fruit = "banana"
print(fruit.count('a'))


# Q8 Check whether the string starts with "Python".
course = "Python Backend"
print(course.startswith("Python")) #case sensitivity matter


# Q9 Split the date using '-'.
date = "26-01-2005"
print(date.split('-'))


# Q10 Print the following using an f-string.
# My name is Harsh.
name = "Harsh"
print(f"my name is {name}")


# Q11
# Print only "gram"
text = "Python Programming"
print(text[10:14])

# Q12
# Replace every 'a' with '@'
fruit = "banana"
print(fruit.replace('a', "@"))

# Q13
# Check whether "Python123" ends with "123"
text = "Python123"
print(text.isalnum())

# Q14
# Print only the second last character
text = "Backend"
print(text[-2])


# Q15
# Count how many times "an" appears
text = "banana"
print(text.count('an'))