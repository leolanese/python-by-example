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
`List`: Ordered, changeable, allows duplicates (mutable)
`Tuple`: Ordered, unchangeable (immutable), allows duplicates
`Set`: Unordered, unindexed, unmodifiable, no duplicates allow
`Dictionary`: Unordered, changeable, indexed, no duplicates allow
```

| Data Structure | Ordered? | Modifiable? | Indexed? | Allows Duplicates? | Example |
|----------------|----------|-------------|----------|---------------------|---------|
| List           | Yes      | Yes         | Yes      | Yes                 | `my_list = [1, 2, 3, 1]` |
| Tuple          | Yes      | No          | Yes      | Yes                 | `my_tuple = (1, 2, 3, 1)` |
| Set            | No       | Yes         | No       | No                  | `my_set = {1, 2, 3}` |
| Dictionary     | No       | Yes         | Yes      | No                  | `my_dict = {'key1': 'value1', 'key2': 'value2'}` |


## list (Ordered, changeable, allows duplicates)

> lst = list[]

Lists are mutable, meaning you can modify their elements after the list is created.
You can add, remove, or change elements in a list.

```
my_list = [3, 1, 2, 3]

print(my_list)  # Output: [3, 1, 2, 3]
```

## Tuples (Ordered, unchangeable (immutable), allows duplicates)

> lst = list()

Tuples are immutable, meaning once a tuple is created, you cannot add, remove, or modify its elements.
You can't change the values of elements or add/remove elements from a tuple.

```
my_tuple = (3, 1, 2, 3)

print(my_tuple)  # Output: (3, 1, 2, 3)
```

## Set (Unordered, unindexed, unmodifiable, no duplicates allow)

```
my_set = {3, 1, 2, 3}

print(my_set)  # Output: {1, 2, 3}
```

## Dictionary (Unordered, changeable, indexed, no duplicates allow)

```
my_dict = {'apple': 3, 'banana': 2, 'orange': 1, 'apple': 4}

print(my_dict)  # Output: {'apple': 4, 'banana': 2, 'orange': 1}
```
