# classes are defined by def
def main():


#  __init__() Function
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# The __init__() function is called automatically every time the class is being used to create a new object.

# self parameter is a reference to the class itself
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter 
of any function in the class:

class Person:
  def __init__(self, name, age):
    self.name = name 
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# Modify Object Properties
p1.age = 40

# Delete Object Properties
del p1.age



# Use special methods to compare objects to each other
class Employee():
    def __init__(self, fname, lname, level, yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrsService

    # implement comparison functions by emp level
    def __ge__(self, other):
        if self.level == other.level:
            return self.seniority >= other.seniority
        return self.level >= other.level

    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority
        return self.level > other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority
        return self.level < other.level

    def __le__(self, other):
        if self.level == other.level:
            return self.seniority <= other.seniority
        return self.level <= other.level

    def __eq__(self, other):
        return self.level == other.level

def main():
    # define some employees
    dept = []
    dept.append(Employee("Tim", "Sims", 5, 9))
    dept.append(Employee("John", "Doe", 4, 12))
    dept.append(Employee("Jane", "Smith", 6, 6))
    dept.append(Employee("Rebecca", "Robinson", 5, 13))
    dept.append(Employee("Tyler", "Durden", 5, 12))

    # Who's more senior?
    print(bool(dept[0] > dept[2]))
    print(bool(dept[4] < dept[3]))

    # sort the items
    emps = sorted(dept)
    for emp in emps:
        print(emp.lname)


if __name__ == "__main__":
    main()
