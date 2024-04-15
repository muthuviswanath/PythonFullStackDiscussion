from random import randint

# Create a class Called as Ludo
# Create a method that takes a number as input and it should display the message as follows:
# If the number is 1 then the message should be: You moved one step forward
# If the number is 2 then the message should be: You moved two step forward
# If the number is 3 then the message should be: You moved three step forward
# If the number is 4 then the message should be: You moved four step forward
# If the number is 5 then the message should be: You moved five step forward
# If the number is 6 then the message should be: You moved six step forward

# Create a class called as PUBG
# Inside the PUB class create a method called as provideWeapons that takes a number as input and display the following
# If the number is 1: 
#                   Create Object of Knife and print ("Stab the enemy with the knife")
# If the number is 2: 
#                   Create Object of Grenade and print ("Remove the pin and throw the grenade")
# If the number is 3: 
#                   Create Object of Gun and print ("Open Fire")

class PUBG:
    def provideWeapons(self,num):
        if num ==1:
            k = Knife()
            k.action()
        elif num == 2:
            g = Grenade()
            g.action()
        else:
            gun = Gun()
            gun.action()

class Knife:
    def action(self):
        print("Stab the enemy with the knife")

class Grenade:
    def action(self):
        print("Remove the pin and throw the grenade")
    
class Gun:
    def action(self):
        print("Open Fire")


#SOLID Principles
# S - Single Responsibility Principle (SRP) - A class should have its own responsibility for performing actions. It should be
#                                             responsible for all other actions.
# O - Open-Closed Principle(OCP) - A class should be open for scalability purpose but should be closed for any modifications
# L - Liskov's Substitution Principle (LSP) - If Beta is subclass of Alpha we should be able to replace Beta with Alpha without altering
#                                              or changing the behavior of Alpha 
# I - Interface Segregation Prinicple (ISP) - If there is a large interface, then they should be divided into sub interfaces so that
#                                              it will be easy for the classes to implement them separately
# D - Dependency Inversion Principle (DIP) - It is decoupling of the software modules such that the modules are not depedent wherein 
#                                            the highlevel modules are dependent on low level modules rather both are dependent on abstraction