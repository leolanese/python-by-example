# How to sort a Python dict by value
# (== get a representation sorted by value)

# 1
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
sorted(xs.items(), key=lambda x: x[1]) # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# 2
Weight_details = {
    'Sam':45, 
    'Irum':67,
    'Dolly':80, 
    'Bela':20
    }
 
sorted_weight = sorted(Weight_details.items(), key=lambda x:x[1])
print(sorted_weight)

# 3: using sort & Lambda Function
import operator
sorted(xs.items(), key=operator.itemgetter(1)) # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# 3: using sort & Lambda Function & reverse
import operator
sorted(xs.items(), key=operator.itemgetter(1), reverse=True) # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
