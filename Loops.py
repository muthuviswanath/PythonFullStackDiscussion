# while, for
# entry controlled loops


# While Loop Syntax:

# loop variable declaration and initialization
# while (condition) the condition will be around loop variable
#   Statements
#   loop variable increment or decrement (Write a statement that stops the loop after certain execution)


n = 1
while n <= 50:
    print(n)
    n += 1
    
while True:
    n = int(input("Enter a number"))
    if(n == 0):
        break
    else:
        print("Square of the number:",n*n)
    