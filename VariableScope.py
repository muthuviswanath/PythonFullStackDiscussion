#   Local,Global,Built-In,Enclosed
# If the varaible name of the global variable and the local variable are same, then to access the 
# global variable from the local scope, we need to redeclare the global varaible using the keyword global

a = 30 #global scope
def func():
    global a
    print(a)
    a = 10 # local scope
    print(a)

func()