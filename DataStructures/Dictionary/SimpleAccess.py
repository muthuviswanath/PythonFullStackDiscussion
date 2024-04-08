My_Car = {
    "Brand":"Ford",
    "Variant":"Eco Sport",
    "Model":2024,
    "Transmission":"Automatic",
    "Fuel Type" : "Petrol"
}

print(My_Car["Transmission"])
print(My_Car.get("Transmission"))

My_Car.update({"Model":2019})
print(My_Car.get("Model"))

print(My_Car)
del My_Car["Model"]
print(My_Car)

My_Car.pop("Transmission")
print(My_Car)

My_Car.popitem()
print(My_Car)