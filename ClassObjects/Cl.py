# class class_name:
#       property_declaration and assignment
#       method_declaration

# create a new object:
# variable_name(reference_variable) = class_name()


# reference_variable.variable_name
# reference_variable.method_name(argument)

class Bike:
    Model = "MR250"
    Transmission = "5 Gear"
    Fuel = "Petrol"
    Make = "BMW"
    
    def start_engine(self, ignition):
        if ignition == "On":
            print(f"Your {self.Model} {self.Make} bike has started")
        else:
            print("First turn on the Ignition")

# Create the object
bmw_racer = Bike()
print(f"Model: {bmw_racer.Model}")
print(f"Transmission: {bmw_racer.Transmission}")
print(f"Fuel: {bmw_racer.Fuel}")
print(f"Make: {bmw_racer.Make}")
bmw_racer.start_engine("Off")

# Create an Employee class that has the following properties:
# Name, Designation, Salary, DepartmentName