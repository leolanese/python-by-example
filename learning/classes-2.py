class myClass(): # create a class
  def foo1(self): # create a function in the class
    print ("myClass foo1")
    
  def foo2(self, someString):
    print ("myClass foo2: " + someString)
    
class anotherClass(myClass): # create a another class
  def foo2(self): # create a function in the other class
    print ("anotherClass foo2")
    
  def foo1(self):
    myClass.foo1(self);
    print ("anotherClass foo1")
      
def main():
  c = myClass()
  c.foo1()
  c.foo2("This is a string")
  c2 = anotherClass()
  c2.foo1()
  
if __name__ == "__main__": # When the Python interpreter reads a source file, it executes all of the code found in it
  main()
