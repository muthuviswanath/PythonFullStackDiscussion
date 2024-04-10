class Even:
    val = 100
    
    def display(self):
        print (self.val)

print(Even.val)
e = Even() # this calls the default constructor
e.display()

class Odd:
    
    def __init__(self):
        self.val = 1000
    
    def show(self):
        print (self.val)

o = Odd() # this calls the non-parameterized constructor that is created by the developer
o.show()

class Prime:
    count = 0
    def __init__(self, num):
        for i in range(1,num+1):
            if num % i == 0:
                self.count += 1
    
    def checkPrime(self):
        if self.count == 2:
            print("Given number is Prime number")
        else:
            print("Given number is not Prime number")

p = Prime(97) # this calls the parameterized constructor that is created by the developer
p.checkPrime()

class Box:
    
    def __init__(self, length=10, width =20):
        print(f"Area: {length * width}")
    
b = Box()
b = Box(100,100)

class Vignesh:
    
    def __init__(self):
        self.age = 23
        self.name = "Vignesh"
        self.occupation = "CEO"
    
    def display(self):
        print(f"{self.name} who is {self.age} years old is working as {self.occupation}")

v = Vignesh()
v.display()
