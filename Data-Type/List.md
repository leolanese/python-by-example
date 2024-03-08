# Lists

```
# Create a list of squares for even numbers from 0 to 9
squares = [x**2 for x in range(10) if x % 2 == 0]

print(squares)  # Output: [0, 4, 16, 36, 64]
```


```
# Create a matrix using nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[1][1])  # Output: 5
```

```
# Concatenate lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]

# Repeat elements in a list
repeated_list = list1 * 3
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

```
# Append and remove elements
fruits = ['apple', 'banana', 'orange']
fruits.append('grape')
print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape']

fruits.remove('banana')
print(fruits)  # Output: ['apple', 'orange', 'grape']
```

```
# Extract a sublist using slicing
numbers = [1, 2, 3, 4, 5]
sublist = numbers[1:4]
print(sublist)  # Output: [2, 3, 4]
```

