# Python Strings

> Strings are Arrays

> Square brackets can be used to access elements of the string.

## Most common string methods

| Method                    | Description                                                             | Example                               |
|---------------------------|-------------------------------------------------------------------------|---------------------------------------|
| `capitalize()`            | Returns a copy of the string with its first character capitalized        | `'hello'.capitalize()` -> `'Hello'`    |
| `casefold()`              | Returns a casefolded version of the string (suitable for case-insensitive comparisons) | `'Hello'.casefold()` -> `'hello'`   |
| `center(width, fillchar)` | Returns a centered string within a specified width, padded with a fill character | `'hello'.center(10, '-')` -> `'--hello--'` |
| `count(substring)`        | Returns the number of occurrences of a substring in the string           | `'hello'.count('l')` -> `2`          |
| `endswith(suffix)`        | Returns `True` if the string ends with the specified suffix              | `'hello'.endswith('lo')` -> `True`   |
| `startswith(prefix)`      | Returns `True` if the string starts with the specified prefix            | `'hello'.startswith('he')` -> `True` |
| `find(substring)`         | Returns the lowest index of a substring, or -1 if not found              | `'hello'.find('l')` -> `2`           |
| `index(substring)`        | Similar to `find()`, but raises an exception if the substring is not found | `'hello'.index('l')` -> `2`        |
| `isalnum()`               | Returns `True` if all characters in the string are alphanumeric         | `'hello123'.isalnum()` -> `True`     |
| `isalpha()`               | Returns `True` if all characters in the string are alphabetic           | `'hello'.isalpha()` -> `True`        |
| `isdigit()`               | Returns `True` if all characters in the string are digits               | `'123'.isdigit()` -> `True`          |
| `islower()`               | Returns `True` if all alphabetic characters in the string are lowercase | `'hello'.islower()` -> `True`        |
| `isupper()`               | Returns `True` if all alphabetic characters in the string are uppercase | `'HELLO'.isupper()` -> `True`        |
| `lower()`                 | Returns a lowercase version of the string                               | `'HELLO'.lower()` -> `'hello'`       |
| `upper()`                 | Returns an uppercase version of the string                               | `'hello'.upper()` -> `'HELLO'`       |
| `strip()`                 | Removes leading and trailing whitespace                                 | `'  hello  '.strip()` -> `'hello'`   |
| `replace(old, new)`       | Replaces occurrences of a substring with another substring              | `'hello'.replace('l', 'X')` -> `'heXXo'` |
| `split(separator)`        | Splits the string into a list of substrings based on a separator        | `'hello world'.split(' ')` -> `['hello', 'world']` |
| `join(iterable)`          | Joins the elements of an iterable into a single string using the string as a separator | `'-'.join(['hello', 'world'])` -> `'hello-world'` |
| `len()`                   | Returns the length of the string                                        | `len('hello')` -> `5`                 |

```
a = 'Hello, World!'

a[0] # 'H'
a[1] # 'e'
```

```
for x in "Leo":
  print(x)

L
e
o
```

## String Length

```
a = "Hello, World!"

len(a) # 13
```

## Check String (is / not)

```
txt = "The would is out there. Follow the tracks.";

"the" in txt # true
```

```
txt = 'The would is out there. Follow the tracks';

if "the" in txt:
  print("Yes, 'the' is there") # Yes, 'the' is there
```

## Slice String

```
b = "Hello, World!"

print(b[:5]) # Hello
```

```
b = "Hello, World!"

print(b[7:]) # World!
```

## Remove elements

```
# Remove front and back Whitespace
a = " Hello, World! "

print(a.strip()) # returns "Hello, World!" ' 
```

```
# Split String
a = "Hello, World!"

print(a.split(",")) # ['Hello', ' World!']
```

```
# Replace String
a = "Hello, World!"

print(a.replace("H", "J")) # Jello, World!
```

## Format Strings

```
name = 'Leo';
age = 40;
txt = "My name is {}, and I am {}";

print(txt.format(name, age)) # My name is Leo, and I am 40
```

