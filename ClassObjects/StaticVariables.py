class Mouse:
    
    owner = "Pillayaar"
    
    def __init__(self):
        Mouse.name = "Moonjoor"
    
    def mymeth(self):
        Mouse.legs = 4
        
    @classmethod
    def classmeth(cls):
        cls.tail = "Long Tail"
    
    @staticmethod
    def statmeth():
        Mouse.actions = "Steal food"

m = Mouse()
m.mymeth()
print(m.legs)


e = Mouse()
print(e.legs)


m.classmeth()
print(e.tail)

m.statmeth()
print(e.actions)
print(e.owner)
print(m.owner)