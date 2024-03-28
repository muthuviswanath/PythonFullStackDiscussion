class Employee:
    
    Emp_Name = ""
    Emp_Id = 0
    Designation = ""
    Employment_Type =""
    Salary = 0
    Bonus = 0
    
    def get_user_input(self):
        self.Emp_Name = input("Enter the employee name: ")
        self.Emp_Id = int(input("Enter the employee Id: "))
        self.Designation = input("Enter the employee Designation: ")
        self.Employment_Type = input("Enter the employment type: ")
        self.Salary = int(input("Enter the salary: "))
    
    def give_bonus(self):
        if self.Employment_Type == "Permanent":
            self.Bonus = 5000
    
    def print_net_salary(self):
        print(f"Net Salary (salary + bonus): {self.Salary + self.Bonus}")

emp = Employee()
emp.get_user_input()
emp.give_bonus()
emp.print_net_salary()
