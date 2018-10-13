# merging 2 objects
x = {'a':1, 'b': 2}
y = {'c':3, 'd': 4}
z = {**x, **y}
print(z) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
