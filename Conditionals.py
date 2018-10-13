# if conditional
a = 1
b = 2
if b > a:
  print("b is greater than a") # b is greater than a
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
  
# if else short hand 
a = 1
b = 2
c = 3
print("hello conditionals!") if a < b and c > a else print('nothing') # hello conditionals!


# Loops
i = 0
while i < 6:
  i += 1 
  if i == 3:
    continue
  print(i)
  

# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
    



    
