# Lists

| Method                  | Description                                    |
|-------------------------|------------------------------------------------|
| `append(x)`             | Adds element `x` to the end of the list        |
| `extend(iterable)`      | Appends elements of `iterable` to the list     |
| `insert(i, x)`          | Inserts element `x` at index `i` in the list   |
| `remove(x)`             | Removes the first occurrence of element `x`    |
| `pop([i])`              | Removes and returns the element at index `i`   |
| `clear()`               | Removes all elements from the list             |
| `index(x[, start[, end]])` | Returns the index of the first occurrence of element `x` |
| `count(x)`              | Returns the number of occurrences of element `x` |
| `sort(key=None, reverse=False)` | Sorts the list in ascending or descending order |
| `reverse()`             | Reverses the order of the elements in the list |
| `copy()`                | Returns a shallow copy of the list             |


## Mixed Data Type List within the same structure
```
mixed_list = ["apple", 3.14, True, [10, 20, 30]]
print(mixed_list) # ['apple', 3.14, True, [10, 20, 30]]
```

## Create a list of squares for even numbers from 0 to 9
```
squares = [x**2 for x in range(10) if x % 2 == 0]

print(squares)  # Output: [0, 4, 16, 36, 64]
```

## Create a matrix using nested lists
```
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[1][1])  # Output: 5
```

## Concatenate lists
```
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]

# Repeat elements in a list
repeated_list = list1 * 3
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

## Handle elements: append, remove, sort, reverse
```
fruits = ['apple', 'banana', 'orange']
fruits.append('grape')

print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape']

fruits.remove('banana')
print(fruits)  # Output: ['apple', 'orange', 'grape']

fruits = ["apple", "banana", "orange", "cherry", "grape"]

# Add an element to the end
fruits.append("mango")

# Remove the first occurrence of an element
fruits.remove("banana")

# Sort the list in ascending order
fruits.sort()

# Reverse the order of elements in-place
fruits.reverse()

print(fruits)
```


## Extend
```
groceries = ["bread", "milk", "cheese"]
snacks = ["chips", "candy", "popcorn"]

groceries.extend(snacks)
print(groceries)  # Output: ['bread', 'milk', 'cheese', 'chips', 'candy', 'popcorn']
```

## insert
```
groceries.insert(0, "bread")
print(groceries)  # Output: ['bread', 'milk', 'cheese', 'chips', 'candy', 'popcorn']
```

## pop
```
snack = groceries.pop()
print(groceries)  # Output: ['bread', 'milk', 'chips', 'candy']
print(snack)  # Output: 'popcorn'
```

## index
```
snacks = ["chips", "candy"]
chip_index = snacks.index("chips")
print(f"Chips are at index {chip_index}")  # Output: Chips are at index 0
```


## count
```
snacks = ["chips", "candy"]
candy_count = snacks.count("candy")
print(f"There are {candy_count} candy in the list")  # Output: There are 1 candy in the list
```


## sort
```
snacks = ["chips", "candy"]
snacks.sort()
print(snacks)  # Output: ['candy', 'chips']
```


## Extract a sublist using slicing
```
numbers = [1, 2, 3, 4, 5]
sublist = numbers[1:4]
print(sublist)  # Output: [2, 3, 4]
```


## List Comprehensions (Concise List Creation)
```
squares = [x**2 for x in range(1, 6)]  
words = [word.upper() for word in "hello world".split()]  

print(squares) # Creates a list of squares from 1 to 5
print(words) # Uppercases each word
```

## Nested Lists (Hierarchical Data Structures)
```
inventory = [
    ["Shirt", "M", 10, 19.99],
    ["Jeans", "L", 5, 39.95],
    ["Hat", "S", 8, 14.99],
]
print(inventory)

# Accessing specific items within the nested structure
first_item_name = inventory[0][0]
first_item_price = inventory[0][3]

print(f"First item name: {first_item_name}")
print(f"First item price: ${first_item_price:.2f}")
```

## List Slicing (Extracting Specific Subsequences)
```
numbers = [1, 2, 3, 4, 5, 6, 7]

# Get a sublist from index 2 (inclusive) to 5 (exclusive)
sliced_list = numbers[2:5]

# Get a copy of the list from the beginning to the fourth element (not inclusive)
copied_list = numbers[:4]

# Get a reversed sublist from index 1 (inclusive) to the end
reversed_slice = numbers[1:][::-1]

print(sliced_list)
print(copied_list)
print(reversed_slice)
```

## Lists Looping
```
# for loop
numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for num in numbers:
    squared_numbers.append(num * num)
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

# List Looping comprehension
```
squared_numbers = [num * num for num in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

## List looping with Filtering
```
even_numbers = [num for num in range(1, 11) if num % 2 == 0]
print(even_numbers) # [2, 4, 6, 8, 10]
```

# List looping with Modification
```
sentence = "Hello world, hi there!?";
uppercase_words = [word.upper() for word in sentence.split()];
print(uppercase_words) # ['HELLO', 'WORLD,', 'HI', 'THERE!?']
```
