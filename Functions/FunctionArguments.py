def sum(a,b): # here a and b are called as parameters
    return a+b

# Keyword Arguments
result = sum(10,20) # 10 and 20 are values that are passed to the function's parameter and it is called as argument
print(result)

# Default Arguments:
# It is possible to provide user-defined values while calling the function.
def mul(a=5,b=2): # when declaring the function if the parameters are assigned a value, then they are called as Default Arguments
    print(a*b)

mul()
mul(10,10)

# Arbitrary Arguments:
# For a given parameter, it is possible to provide more than one values

def greetings(*names):
    for n in names:
        print (f"Hello {n}!")


greetings('Vignesh','Muthu','Vasu','Raju')
