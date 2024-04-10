# Cow gives Milk by taking Grass and Water as input
# Identify the Objects present in the requirement
# Create a class for all the objects that are identified
# Create the method inside the respective class based on "REVERSE L" technique
# Verify the output

# Cow, Milk, Grass and Water

class Cow:
    
    def gives(self,grass, water):
        m = Milk()
        print(id(m))
        return m

class Milk:
    pass

class Grass:
    pass

class Water:
    pass

c = Cow()
grass = Grass()
water = Water()
mlk = c.gives(grass,water)
print(id(mlk))


#           Object
#             |
#             |
#             |
#             |
# Output______|Action
