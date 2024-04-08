My_Car = {
    "Brand":"Ford",
    "Variant":"Eco Sport",
    "Model":2024,
    "Transmission":"Automatic",
    "Fuel Type" : "Petrol"
}

for k in My_Car:
    print(f"{k} | {My_Car[k]}")

for val in My_Car.values():
    print(f"Values: {val}")
    
for k in My_Car.keys():
    print(f"Keys: {k}")

for k,v in My_Car.items():
    print(f"{k} | {v}")