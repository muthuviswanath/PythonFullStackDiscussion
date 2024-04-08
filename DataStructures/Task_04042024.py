# List Operations:
# 1. Create a numerical List
# 2. Display the second largest element of the list
my_list = [12,23,12,45,67,67,3,5,2,2,89,89,89,54]
first_max = max(my_list)    # first_max = 89
second_max = min(my_list)   # second_max = 67                        
for element in my_list:     # element = 54
    if element > second_max and element != first_max:
        second_max =  element
print(f"Second Maximum: {second_max}")
# 3. Display the second smallest element of the list
my_list = [12,23,12,45,67,67,3,5,2,2,89,89,89,54]
first_max = max(my_list)    # first_max = 89
second_max = min(my_list)   # second_max = 67                        
for element in my_list:     # element = 54
    if element < first_max and element != second_max:
        first_max =  element
print(f"Second Minumum: {first_max}")
# 4. Split the given list into two lists by taking the number of elements to be present in the first list
# 5. Exit

