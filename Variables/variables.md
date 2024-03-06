# Creating Variables

> Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.

> Python variables are case-sensitive

## Python is `dynamically typed` but `strongly typed`

```js
x = 5  # x is an integer

x = "Hello"  # x is now a string

print(x); # Hello

print(type(x)); # <class 'str'>
```

```
x, y, z = "Leo", "Tom", "Sam";

print(x, y, z); # Leo, Tom, Sam
```

```
# when you want to access a value from a dictionary using its key, you need to use the key as a string inside square brackets.
people = [{
   'firstname': 'John',
   'lastname': 'Doe',
   'country': 'USA',
   'city': 'New York',
   'age': 30,
   'skills': ['Java', 'C#', 'SQL']
}]

print(people[0]['firstname'])
```


---

## Unpacking 

> Process of extracting elements from an iterable (like a tuple, list, or dictionary) and assigning them to individual variables.

# Unpacking a Tuple:
```
coordinates = (10, 20);
x, y = coordinates;

x # 10
y # 20
coordinates # (10, 20)
```

# Unpacking a list
```
numbers = [1, 2, 3];
a, b, c = numbers;

numbers # [1, 2, 3]
a # 1
b # 2
c # 3
```

# Unpacking a dictionary
```
person = {"name": "Alice", "age": 30};
name, age = person.values();

print("name:", name, "age:", age) # name: Alice age: 30
```

# Unpacking with meaningful variable names
```
point = (5, 10);
x_coordinate, y_coordinate = point;

print("x_coordinate:", x_coordinate) # x_coordinate: 5
print("y_coordinate:", y_coordinate) # y_coordinate: 10
```

---

# Global Variables

> Attempting to access the local variable outside the function will result in an error

> `global_var` is a global variable that can be accessed both inside and outside the function.

```
# Global variable
global_var = 10

def modify_global():
    # Function block
    # Accessing and modifying the global variable within the function
    global global_var
    global_var += 5
    print("Inside modify_global function - Global variable:", global_var)

def use_local():
    # Function block
    # Local variable
    local_var = 5
    # Accessing the local variable
    print("Inside use_local function - Local variable:", local_var)

# Accessing the global variable before calling the function
print("Before calling functions - Global variable:", global_var)

# Calling the function that modifies the global variable
modify_global()

# Accessing the global variable after calling the function
print("After calling modify_global function - Global variable:", global_var)

# Calling the function that uses a local variable
use_local()
```






