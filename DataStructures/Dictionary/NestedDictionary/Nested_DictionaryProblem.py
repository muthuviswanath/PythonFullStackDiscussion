Employee = {"Muthu":{"Designation": "Manager", "Salary":45678},
            "Vignesh":{"Designation": "Manager", "Salary":456378},
            "Roopa":{"Designation": "Developer", "Salary":25678}}

# Display the complete dictionary entries of the manager who is getting highest salary
# EXpected Output:
# Vignesh:{"Designation": "Manager", "Salary":456378}

max = 0
print(f"Original Dictionary: \n")
for key,val in Employee.items():
    print(f"Key: {key} | Value: {val}")
    if val["Salary"] > max:
        max = val["Salary"]

print(f"Maximum Salary: {max}")

for key,val in Employee.items():
    if val["Designation"] == "Manager" and val["Salary"] == max:
        print(f"{key} | {val}")

# print(f"The Manager with Higher Salary:")
# print(f"{result}")