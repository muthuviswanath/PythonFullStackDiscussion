

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
    
