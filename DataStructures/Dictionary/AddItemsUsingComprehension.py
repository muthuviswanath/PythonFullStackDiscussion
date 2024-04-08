n = int(input("Enter the number of records to be added to the database: "))
user_database = {input(f"Enter the id of {i+1} User: "):input(f"Enter the name of {i+1} User: ") for i in range(n)}
print(user_database)