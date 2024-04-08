Employee = {"Muthu":{"Designation": "Manager", "Salary":45678},
            "Vignesh":{"Designation": "Manager", "Salary":456378},
            "Roopa":{"Designation": "Developer", "Salary":25678}}

# Display the complete dictionary entries of the manager who is getting highest salary
# EXpected Output:
# Vignesh:{"Designation": "Manager", "Salary":456378}


Emp_list = {}
n = int(input("Enter the number of Employees to be added: "))
for i in range(n):
    emp_no = int(input("Enter the employee number: "))
    Emp_list[emp_no] = {}
    Name = input("Enter the Employee Name: ")
    Email = input("Enter the Employee Email: ")
    Phone = input("Enter the Employee Phone: ")
    Emp_list[emp_no]["Name"] = Name
    Emp_list[emp_no]["Email"] = Email
    Emp_list[emp_no]["Phone"] = Phone
print("List of Employees")
print(Emp_list)    
    
