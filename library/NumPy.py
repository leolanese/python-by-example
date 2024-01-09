# Finding the Sum of numbers Using Loops: 0.14 Seconds
import time 
start = time.time()
# iterative sum
total = 0
# iterating through 1.5 Million numbers
for item in range(0, 1500000):
    total = total + item
print('sum is:' + str(total))
end = time.time()
print(end - start)
# 1124999250000
# 0.14 Seconds


# Finding the Sum of numbers Using Vectorization: 0.14 Seconds
import numpy as np
start = time.time()
# vectorized sum - using numpy for vectorization
# np.arange create the sequence of numbers from 0 to 1499999
print(np.sum(np.arange(1500000)))
end = time.time()
print(end - start)

# 1124999250000
# 0.008 Seconds
