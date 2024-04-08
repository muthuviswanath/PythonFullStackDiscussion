# How to define a dictionary

# Empty Dictionary
my_dictionary = {}
# Dictionary with hard coded values
mi_players = {45:"Rohit Sharma",91:"Hardik Pandya",63:"SK Yadav",93:"Bumrah"}

# Dictionary with values that are got from the user. Single value
k = int(input("Enter a player jersy number: "))
v = input("Enter the player name: ")
my_dictionary[k] = v
print(my_dictionary)

# Dictionary with values that are got from the user. Multiple values
user_dictionary = {}
n = int(input("Enter the total number of users to be added: "))
for i in range(n):
    u_id = int(input("Enter the user id: "))
    u_name = input("Enter the user name: ")
    user_dictionary[u_id] = u_name
print(user_dictionary)

# Dictionary with values that are got from the user. Multiple values
employee_dictionary = {}
n = int(input("Enter the total number of users to be added: "))
for i in range(n):
    u_id = 1000 + i + 1
    u_name = input("Enter the employee name: ")
    employee_dictionary[u_id] = u_name
print(employee_dictionary)


