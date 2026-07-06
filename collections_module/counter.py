from collections import Counter

fruits = ["apple", "banana", "apple", "mango", "banana", "apple"]

count = Counter(fruits)
print(count)


print(count.most_common())
print(count.most_common(2))


text = "python django python flask django"
print(Counter(text.split()))



fruits = ["apple", "banana", "mango"]

count = Counter()
for fruit in fruits:
    count.update(fruit)

print(count)