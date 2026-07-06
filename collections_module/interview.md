# Collections Module in Python

## What is Collections Module?

The `collections` module provides specialized container data types that extend the functionality of Python's built-in data structures like list, tuple, dictionary, and set.

It makes code cleaner, faster, and more efficient.

Import

```python
from collections import *
```

---

# 1. namedtuple

## Definition

`namedtuple` creates a tuple with named fields instead of index positions.

Example

```python
Student = namedtuple("Student", ["name", "age"])
```

Advantages

- More readable than tuple
- Immutable
- Faster than dictionary
- Less memory than dictionary

---

# 2. deque

## Definition

deque (Double Ended Queue) allows fast insertion and deletion from both the left and right ends.

Common Methods

```python
append()

appendleft()

pop()

popleft()
```

Advantages

- Fast insertion at beginning
- Fast deletion at beginning
- Better than list for queue operations

---

# 3. Counter

## Definition

Counter is a dictionary subclass used to count the frequency of elements.

Example

```python
Counter(["apple","banana","apple"])
```

Common Method

```python
most_common()
```

Advantages

- Frequency counting
- Cleaner than manual dictionary counting

---

# 4. defaultdict

## Definition

defaultdict is a dictionary subclass that automatically provides a default value for missing keys instead of raising a KeyError.

Common Default Factories

```python
defaultdict(int)

defaultdict(list)

defaultdict(set)

defaultdict(str)
```

Advantages

- No KeyError
- Cleaner code
- No manual initialization

---

# 5. OrderedDict

## Definition

OrderedDict is a dictionary subclass that preserves insertion order and provides additional methods.

Common Method

```python
move_to_end()
```

Important

Python 3.7+ normal dictionaries also preserve insertion order.

OrderedDict is mainly used for extra methods.

---

# 6. ChainMap

## Definition

ChainMap groups multiple dictionaries into a single view without merging them.

Example

```python
ChainMap(dict1, dict2)
```

Advantages

- Multiple dictionaries
- No copying
- Easy configuration management

---

# Interview Questions

## 1. What is the Collections module?

Answer:

Collections is a built-in Python module that provides specialized container data types like namedtuple, deque, Counter, defaultdict, OrderedDict, and ChainMap.

---

## 2. What is namedtuple?

Answer:

namedtuple creates tuple subclasses with named fields, making code more readable while keeping tuples immutable.

---

## 3. Difference between tuple and namedtuple?

Answer:

tuple

- Access by index

namedtuple

- Access by field name

---

## 4. What is deque?

Answer:

deque (Double Ended Queue) allows efficient insertion and deletion from both ends.

---

## 5. Why use deque instead of list?

Answer:

Because inserting or deleting at the beginning of a list is slow, while deque performs these operations efficiently.

---

## 6. What is Counter?

Answer:

Counter is a dictionary subclass used to count the frequency of hashable objects.

---

## 7. What does most_common() do?

Answer:

Returns the elements sorted by frequency in descending order.

---

## 8. What is defaultdict?

Answer:

defaultdict automatically returns a default value when a key is missing instead of raising KeyError.

---

## 9. Why use defaultdict?

Answer:

It avoids KeyError and removes the need to initialize keys manually.

---

## 10. What is OrderedDict?

Answer:

OrderedDict is a dictionary subclass that preserves insertion order and provides additional methods like move_to_end().

---

## 11. Is OrderedDict still useful in Python 3.7+?

Answer:

Yes, but mostly for methods like move_to_end() because normal dictionaries already preserve insertion order.

---

## 12. What is ChainMap?

Answer:

ChainMap combines multiple dictionaries into a single view without merging them.

---

## 13. Difference between OrderedDict and ChainMap?

Answer:

OrderedDict

- Ordered dictionary
- Maintains insertion order

ChainMap

- Combines multiple dictionaries
- Creates a single view

---

# Summary

| Class | Purpose |
|--------|---------|
| namedtuple | Tuple with named fields |
| deque | Fast insert/delete from both ends |
| Counter | Count frequency |
| defaultdict | Default values for missing keys |
| OrderedDict | Ordered dictionary with extra methods |
| ChainMap | Combine multiple dictionaries |

---

# Memory Tricks ⭐

```
namedtuple

Tuple

↓

Named Fields

-----------------------

deque

Left ⇄ Right

Fast Insert/Delete

-----------------------

Counter

List/String

↓

Frequency Count

-----------------------

defaultdict

Missing Key

↓

Default Value

-----------------------

OrderedDict

Dictionary

↓

Maintains Order

+ move_to_end()

-----------------------

ChainMap

Dict1

+

Dict2

+

Dict3

↓

Single View
```

---

# Key Interview Points

- namedtuple is immutable.
- deque is best for queue operations.
- Counter counts frequency.
- defaultdict avoids KeyError.
- OrderedDict provides move_to_end().
- Python 3.7+ dictionaries preserve insertion order.
- ChainMap combines multiple dictionaries without merging.