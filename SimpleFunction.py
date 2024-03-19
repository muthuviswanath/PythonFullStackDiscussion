"""
    Function Syntax:
    
    def <function_name>(param1,param2,.....param_n):
        statement
        return statement - optional
        
    Ways to write a function:
    
    1. A function that takes an input and returns nothing
    2. A function that takes no input and returns nothing
    3. A function that takes no input but returns something
    4. A function that takes an input and returns something
    
"""

def execute(a,b):
    print(a+b)

execute(10,20)

def display():
    print("Hello")
    
display()

def generateInteger():
    return 4

my_value = generateInteger()
print(my_value)

def prod(a,b):
    return a*b

product = prod(10,20)
print(product)