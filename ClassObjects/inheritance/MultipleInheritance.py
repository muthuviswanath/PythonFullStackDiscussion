class Horse:
    tail = True

    def produce_Kids(self):
        print("It is a mammal")

class Bird:
    has_wings = True

    def lay_Eggs(self):
        print("It is not a mammal")

class Unicorn(Horse, Bird):
    pass

u = Unicorn()
print(f"Unicorn has wings: {u.has_wings}")
print(f"Unicorn has tail: {u.tail}")
u.produce_Kids()
u.lay_Eggs()