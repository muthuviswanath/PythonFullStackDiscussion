# # abs() - returns the absolute value of the given number Ex: abs(10) -> 10 abs(-10) -> 10
# print(abs(-10))
# # all() - returns true if the given iterable contains all elements as True else returns false
# l = [1,True," ",None]
# print(all(l))
# # any() - returns true if the given iterable contains at least one element as True else returns false
# print(any(l))
# # ascii() - returns the ascii representation of the given value
# print(ascii('அ'))
# # bin() - converts the given integer value to a binary representation
# print(bin(10))
# # bool() - converts the given value to a boolean
# print(bool(0))
# # callable() - returns true if the given expression is a callable object else returns false
# print(callable(10))
# print(callable(list))
# # chr() - converts the given integer value to a character
# print(chr(100))
# compile() - Compiles the given expressionx
exec(compile('a=10\nb=20\nprint(a+b)','','exec'))
# exec() - executes the compiled python expression
# complex() - it converts a number into a complex number (5+3j)
print(complex(3))
print(complex(10.4))
# dict() - it creates a python dictionary
# dir() - it returns all the attributes of the object
class Test:
    result = "Pass"
t =Test()
print(dir(t))
# enumerate() - it returns all the attributes of the enumeration
for i in enumerate(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']):
    print(i)

# eval() - it evaluates the expression that is represented as String
x = 10
print(eval('x+20'))
# float() - converts the given value into a float

print(float(10))
# format() - It is used to format the given string
print("My age is {0}".format(x))
# help() - it returns the help string
# print(help())
# id() - it returns the object's identifier
a = 34
b = 56
print(id(a))
print(id(b))
# input() - it is used to get the input string from the user
# int() - it is used to convert the given value to integer
# isinstance() - it returns Tru if the given value is an instance else return false
# len() - it returns the length of the iteratble object
l = ['food','travel','movies','games']
print(len(l))