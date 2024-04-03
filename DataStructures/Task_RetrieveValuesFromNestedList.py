# Multidimensional list
lst = [1,2,[23,34,45,56],4,5,6]

# Retrieve the element called (5)
print(f"Expected Element: {lst[4]}")
print(f"Expected Element: {lst[-2]}")
print(f"Expected Element: {lst[2]}")
# Accessing the element inside the nested list:
print(f"Expected Element: {lst[2][2]}")

#Task:
#--------------------------------------------------------
employee = ["Vignesh",["Department",["Sales","Marketing"],"Payroll"],"Muthu"]

# Retrieve the following values from the nested list
# Marketing
print(employee[1][1][1])
# Payroll
print(employee[1][2])
