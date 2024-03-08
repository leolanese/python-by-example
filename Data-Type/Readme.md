# Scalar & Collection Data-Types

> Keep in mind that Python is dynamically typed, meaning you don't need to declare the data type explicitly

## "Scalar" data-types

| Data Type   | Description                                     | Example               |
|-------------|-------------------------------------------------|-----------------------|
| `int`       | Integer numbers                                 | `42`, `-10`, `0`      |
| `float`     | Floating-point numbers                          | `3.14`, `-0.001`, `2.0`|
| `complex`   | Complex numbers                                 | `1 + 2j`, `3 - 4j`     |
| `str`       | String (text)                                   | `'Hello'`, `"Python"`  |
| `bool`      | Boolean (True or False)                         | `True`, `False`        |
| `None`      | Represents the absence of a value (null)        | `None`                |

---

## "Collections" data-types (Arrays)
```
`List`: Ordered, changeable, allows duplicates.
`Tuple`: Ordered, unchangeable (immutable), allows duplicates.
`Set`: Unordered, unindexed, unmodifiable, no duplicates.
`Dictionary`: Unordered, changeable, indexed, no duplicates.
```

| Data Structure | Ordered? | Modifiable? | Indexed? | Allows Duplicates? | Example |
|----------------|----------|-------------|----------|---------------------|---------|
| List           | Yes      | Yes         | Yes      | Yes                 | `my_list = [1, 2, 3, 1]` |
| Tuple          | Yes      | No          | Yes      | Yes                 | `my_tuple = (1, 2, 3, 1)` |
| Set            | No       | Yes         | No       | No                  | `my_set = {1, 2, 3}` |
| Dictionary     | No       | Yes         | Yes      | No                  | `my_dict = {'key1': 'value1', 'key2': 'value2'}` |

---

## list (mutable)

> lst = list[]

Lists are mutable, meaning you can modify their elements after the list is created.
You can add, remove, or change elements in a list.

```
# Create a List = List (fruits = ['banana', 'orange', 'mango', 'lemon']):
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'apple'
```

## Tuples (immutable)

> lst = list()

Tuples are immutable, meaning once a tuple is created, you cannot add, remove, or modify its elements.
You can't change the values of elements or add/remove elements from a tuple.

```
# Create a Tuple = tTuple (fruits = ('banana', 'orange', 'mango', 'lemon')):
fruits = ('banana', 'orange', 'mango', 'lemon')
# error
# fruits[0] = 'apple'
```

---



