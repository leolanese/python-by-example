# Python Scalar & Collection Data-Types

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


## "Collections" data-types (Arrays)
- List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
- Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
- Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
- Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.

| Data Type   | Description                                      | Example                                        |
|-------------|--------------------------------------------------|------------------------------------------------|
| `list`      | Ordered, 'mutable' sequence of elements            | `[1, 2, 3]`, `['a', 'b']`                      |
| `tuple`     | Ordered, 'immutable' sequence of elements          | `(1, 2, 3)`, `('a', 'b')`                      |
| `set`       | Unordered collection of unique elements          | `{1, 2, 3}`, `{'a', 'b'}`                      |
| `dict`      | Key-value pairs mapping                          | `{'name': 'John', 'age': 25}`                  |

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



