class Student:
    # Instance Variables (Object Level Variables):
    # The value of the instance variable can vary for different objects that are created out of same class
    # Where to create Instance variables:
    
    # 1. Inside the constructor using self keyword:
    
    # def __init__(self):
    #   self.age = 10
    
    # 2. Inside the method using self keyword
    
    # def my_method(self):
    #   self.name = "Vignesh"
    
    # 3: Outside the class using the reference variable
    # s.designation = "CEO"
    # print(s.designation)
    
    # Static Variables (Class Level Variables)
    # If the value of the variable is not affected by any number of object or the value remains the constant for all the objects
    # Only one copy of static variable is present for n number of objects
    
    # Where and how to declare the static variable:
    
    # Inside the constructor using the class name
    # Inside an instance method using class name
    # Inside a classmethod using class name or cls variable
    # Inside a static method using class name
    
    
    
    # Local Variables (Method Level Variables)
    def __init__(self):
        self.age = 20
    
    def my_method(self):
        self.name = "Vignesh"
    

s = Student()
print(s.age)
s.my_method()
print(s.name)

s.designation = "CEO"
print(s.designation)

g = Student()
g.age = 45
print(g.age)