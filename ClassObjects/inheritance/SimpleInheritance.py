class Vehicle:
    Make= "Make"
    Manf_Year="Year"
    Color="Color"
    Model="Model"

    def Steer(self):
        print("Steer Left or Steer Right")
    def Ignition(self):
        print("Ignition On/Off")
    def Drive(self):
        print("Drive in forward direction")
    def Reverse(self):
        print("Drive in reverse direction")
    def Stop(self):
        print("Halt the vehicle")

    def __str__(self):
        return "Welcome"


class Car(Vehicle):
    
    def __init__(self):
        self.Make = "Ford"
        self.Manf_Year = 2017
        self.Color = "White"
        self.Model = "Eco Sport"
        
    def Steer(self):
        print("Power Steer Left or Power Steer Right")
    

ecosport = Car()
ecosport.Ignition()
print(ecosport.Model)
ecosport.Steer()
ecosport.Drive()