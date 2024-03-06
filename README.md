# A python-playground

![Python](https://upload.wikimedia.org/wikipedia/commons/0/0a/Python.svg)

##  Refreshing the basics

### Python Command Line

```js
// running Python using Command Line
touch helloworld.py
print("Hello, World!")

python helloworld.py
```

```
// The Python Command Line
python

print("Hello, World!")
exit()
```

### Built-in utility 

| Function          | Description                                                                           | Example                                 |
|-------------------|---------------------------------------------------------------------------------------|-----------------------------------------|
| `help()`          | Provides interactive help and documentation for Python objects and modules            | `help()` or `help(object)`              |
| `dir()`           | Returns a list of names in the current local scope or a list of attributes of an object | `dir()` or `dir(object)`                |
| `type()`          | Returns the type of an object                                                          | `type(42)` -> `<class 'int'>`           |
| `len()`           | Returns the length of an object (such as a string, list, or tuple)                      | `len('hello')` -> `5`                   |
| `print()`         | Prints the specified values to the standard output                                      | `print('Hello, World!')`                |
| `input()`         | Reads a line from the standard input                                                   | `name = input('Enter your name: ')`    |
| `range()`         | Generates a sequence of numbers within a specified range                               | `range(5)` -> `[0, 1, 2, 3, 4]`         |
| `open()`          | Opens a file and returns a file object                                                | `file = open('example.txt', 'r')`     |
| `sum()`           | Returns the sum of elements in an iterable                                            | `sum([1, 2, 3])` -> `6`                  |
| `sorted()`        | Returns a sorted list from the elements of an iterable                                 | `sorted([3, 1, 4, 1, 5, 9, 2])` -> `[1, 1, 2, 3, 4, 5, 9]` |
| `max()`           | Returns the largest item in an iterable or the largest of two or more arguments        | `max(3, 7, 1)` -> `7`                    |
| `min()`           | Returns the smallest item in an iterable or the smallest of two or more arguments      | `min(3, 7, 1)` -> `1`                    |
| `abs()`           | Returns the absolute value of a number                                                | `abs(-5)` -> `5`                        |
| `round()`         | Rounds a floating-point number to the nearest integer                                  | `round(3.14159)` -> `3`                 |
| `input()`         | Reads a line from the standard input                                                   | `name = input('Enter your name: ')`    |
| `exit()`          | Exits the Python interpreter                                                          | `exit()`                                |



### Python Indentation

> In Python, indentation is not just for readability; it is a syntactical element. The level of indentation determines the grouping of statements. Consistent indentation is essential for the code to be valid.

```
if condition:
    # This block is indented
    statement1
    statement2
else:
    # Another indented block
    statement3
    statement4
```

```
# Function to add two numbers
def example_function():
    print("This is indented")
    if True:
        print("This is indented within the if block")
    print("This is back to the outer indentation level")

# Call the function
example_function()
```



### TOPICS

[Learning Path](https://github.com/leolanese/python-playground/tree/master/learning)<br/>
[Library](https://github.com/leolanese/python-playground/tree/master/learning)<br/>
[Tips](https://github.com/leolanese/python-playground/tree/master/tips)<br/>


### Collection Python Playgorund

[Trinket playground](https://trinket.io/python)<br/>
[Programiz playground](https://programiz.pro/ide/python)<br/>
[Online-Python](https://www.online-python.com/)<br/>

---

<h5> { 'Leo Lanese',<br>
       'Building Inspiring Responsive Reactive Solutions',<br>
       'London, UK' }<br>
</h5>
<h5>Portfolio
<a href="http://www.leolanese.com" target="_blank">http://www.leolanese.com</a>
</h5>
<h5>Twitter:
<a href="http://twitter.com/LeoLanese" target="_blank">twitter.com/LeoLanese</a>
</h5>
<h5>Questions / Suggestion / Recommendation ?
<a href="mail:to">developer@leolanese.com</a>
</h5>
<h5>DEV.to:
<a href="http://www.dev.to/leolanese" target="_blank">www.dev.to/leolanese</a>
</h5>
<h5>Blog:
<a href="http://www.leolanese.com/blog" target="_blank">leolanese.com/blog</a>
</h5>
