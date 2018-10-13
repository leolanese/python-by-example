# Splitting Strings

# Avoid this:
str.split('a,b,c', ',') # ['a', 'b', 'c']

# Do this instead:
'a,b,c'.split(',') # ['a', 'b', 'c']

# Splitting Without Parameters
'test me here'.split() # ['test', 'me', 'here']

#############################################################################################
# Concatenating and Joining Strings
## REMEMBER: strings are immutable!

'a' + 'b' + 'c' # 'abc'

str = 'Hi'
str + ' there'
print(str) # 'Hi' because strings are immutable!

str2 = ', world'
str + str2 


# Concatenating With .Join()
strings = ['a', 'b', 'c']
','.join(strings)
'a,b,c'

'b'.join(['a'])  # 'a' # because strings are immutable!
