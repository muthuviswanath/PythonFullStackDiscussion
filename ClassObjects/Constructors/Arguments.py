def calc():
    print ("Hi")

calc()

# default argument
def calc_default(a=10,b=20):
    print(a*b)

calc_default()
calc_default(100,100)

# keyword arguments
def calc_keyword(a,b):
    print(a*b)

calc_keyword(10,30)


#arbitrary arguments
def greet_everyone(*names):
    for name in names:
        print(f"Hello! {name}")

greet_everyone('Vignesh','Muthu','Roopa')
