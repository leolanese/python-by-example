# Python Collections (Arrays)

## There are four 'collection data types' in the Python programming language:
# 1) `List` is a collection which is ordered and changeable. Allows duplicate members.
# 2) `Tuple` is a collection which is ordered and unchangeable. Allows duplicate members.
# 3) `Set` (like JS Objects) is a collection which is unordered and unindexed. No duplicate members.
# 4) `Dictionary` is a collection which is unordered, changeable and indexed. No duplicate members.

## List
```
# list
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
thislist[1] = "blackcurrant"
print(thislist[1])
print(thislist)
```

```
# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
```

```
# check if item exist
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
```

```
# Remove Item list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
```

```
# modifing a list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
```

```
# Checking Items in a List
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
```

```
# Adding Items to the end to a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)    # ['banana', 'orange', 'mango', 'lemon', 'apple']
```

```
# Inserting Items into a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
```

```
# Removing Items from a List
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana']
```

```
# Copying a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
```

---

##  Tuples (immutable)

```
# You cannot change values in a tuple. Tuples are immutable
thistuple = ("apple", "banana", "cherry");
thistuple[1] = "blackcurrant";

print(thistuple); # TypeError: 'tuple' object does not support item assignment
```

```
# It is not possible to remove a single item in a tuple, as preved before
# but it is possible to delete whole the tuple itself using del
fruits = ('banana', 'orange', 'mango', 'lemon');

fruits # ('banana', 'orange', 'mango', 'lemon')

del fruits
```


```
# Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
```

```
# Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
```

```
# Checking an Item in a Tuple
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment
```

---

## Sets (js Objects)

> You cannot access items in a set by referring to an index, since sets are unordered the items has no index.

``` 
# Loop through the set
 thisset = {"apple", "banana", "cherry"}
 for x in thisset:
   print(x)
```

```
# Add an item to a set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
```

```
# Add multiple items to a set
mySet = {"apple", "banana", "cherry"}
mySet.update(["orange"])
print(mySet)
```

```
# Remove Item (if exist)
thisset = {"apple", "banana", "cherry"}
if "banana" in thisset:
  print(thisset)
  thisset.remove("banana") # {'cherry', 'banana', 'apple'}
  print(thisset) # {'cherry', 'apple'}
```  

---

# Dictionary

```
# Change Values 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
```

```
# return values of a dictionary
for x in thisdict.values():
  print(x)
```  

```
# loop through both keys and values
for x, y in thisdict.items():
  print(x, y)
```

```  
# Check if Key Exists. Get value from a key
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print( thisdict.get("model") ) # Mustang
```  
  
```
# delete
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
```
