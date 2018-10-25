# Function argument unpacking

def foo(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {
    'x': 1, 
    'y': 0, 
    'z': 1
}

foo(*tuple_vec) # 1, 0, 1

foo(**dict_vec) # 1, 0, 1
