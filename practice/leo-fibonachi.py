# Using looping technique
def fibL(n):
    a = 0
    b = 1
    for i in range(1,n+1):
            c = a + b
            print b
            a = b
            b = c
# x = int(raw_input('which fibonacci do you want? '))
# fibL(x)  # 15 -> 610


# Using recursion
def fibR(n):
   if n == 1:
      return 1
   elif n == 0:   
      return 0            
   else:                      
      return fibR(n-1) + fibR(n-2)  
x = int(raw_input('which fibonacci do you want? '))
print fibR(x) # 15 -> 610
