def addition(a,b):
    print(f"Sum of {a} and {b}: {a+b}")

def subtraction(a,b):
    print(f"Difference of {a} and {b}: {abs(a-b)}")

def multiplication(a,b):
    print(f"Product of {a} and {b}: {a*b}")

def division(a,b):
    print(f"Quotient of {a} and {b}: {a/b}")
    
def modulous(a,b):
    print(f"Remainder of {a} and {b}: {a%b}")
    
def floordivision(a,b):
    print(f"Quotient of {a} and {b}: {a//b}")
    
def exponentiation(a,b):
    print(f"Exponentiation of {a} and {b}: {a**b}")

num1 = int(input("Enter a value for First Number"))
num2 = int(input("Enter a value for Second Number"))
    
while True:
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. FloorDivision\n\
7. Exponentiation\n8. Exit\n")
    choice = int(input("Enter your choice [1-8]: "))
    if choice == 1:
        addition(num1, num2)
        
    elif choice == 2:
        subtraction(num1, num2)
    
    elif choice == 3:
        multiplication(num1, num2)
    
    elif choice == 4:
        division(num1, num2)
    
    elif choice == 5:
        modulous(num1, num2)
    
    elif choice == 6:
        floordivision(num1, num2)
    
    elif choice == 7:
        exponentiation(num1, num2)
    
    elif choice == 8:
        print("Thanks for using our program")
        break
    else:
        print("Invalid Choice")
        
    