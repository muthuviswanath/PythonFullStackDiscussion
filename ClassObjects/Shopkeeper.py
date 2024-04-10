# Shopkeeper sells Mangoes by taking money as input

# ATM Machine dispense cash by taking card, pin, amount as input

# Conductor Issues ticket by taking destination and money as input

# Vignesh reads NewsPaper

# Shopkeeper, Mangoes, Money

class Shopkeeper:
    
    def sells(self, amount):
        m = Mangoes()
        print(id(m))
        return m
        
class Mangoes:
    pass
class Money:
    pass

s = Shopkeeper()
amt = Money()
mango = s.sells(amt)
print(id(mango))