# # List creation with default elements
# colors = ["Violet","Indigo","Blue","Green","Yellow","Orange","Red"]



# # # Accessing the elements
# #     #printing all the elements
# # print(colors)
# #     # To access a specific element:
# # print(colors[4])

# # # Slicing the list
# # # ------------------------------------------------------------------------------------------------
# # # Prints the elements from the index value 2 till end of list
# # print(colors[2:])
# # # Prints the elements from the index value 2 till the range mentioned-1
# # print(colors[2:5])
# # # Prints the elements from the start till the 6th element
# # print(colors[:6])
# # # Prints empty list if the range mentioned in the slicing operation is not proper
# # print(colors[5:2])
# # # slicing using the negative index value
# # print(colors[-5:-1])
# # # Prints empty list if the range mentioned in the slicing operation is not proper
# # print(colors[-1:-5])
# # # prints the 
# # print(colors[:-5])
# # print(colors[-5:])
# # # print the list in reverse order
# # print(colors[::-1])

# # # Reassigning the values inside the list
# # # ------------------------------------------------------------------------------------------------

# # my_numbers = [10,20,30,50,60,80,90,100]
# # print(my_numbers)

# # my_numbers[5] = 1000
# # print(my_numbers)

# # # Deleting the elements
# # # ------------------------------------------------------------------------------------------------
# # del my_numbers[5]
# # print(my_numbers)

# # #Deleting more than one element
# # del my_numbers[5:]
# # print(my_numbers)

# # # Multidimensional list
# # list = [1,2,[23,34,45,56],4,5,6]

# # # Retrieve the element called (5)
# # print(f"Expected Element: {list[4]}")
# # print(f"Expected Element: {list[-2]}")
# # print(f"Expected Element: {list[2]}")
# # # Accessing the element inside the nested list:
# # print(f"Expected Element: {list[2][2]}")

# # # Concatenation of lists
# # my_list_1 = [1,2,3,4,5]
# # my_list_2 = [10,20,30,40,50]
# # final_list = my_list_1 + my_list_2
# # print(final_list)
# # Operations on lists
# my_list_1 = [1,2,3,4,5]
# my_list_2 = [1.5,20,30,40,50,"Welcome",True,45+7j]
# ops_list = my_list_1 * 2
# print(ops_list)
# # ops_list = my_list_1 * my_list_2[0]
# # ops_list = my_list_1 * 2
# ops_list = my_list_1 + my_list_2
# print(ops_list)

# # Iterations on lists

# for i in range(0,8):
#     print(f"Element at index value {i}: {my_list_2[i]}")
    
# for i in my_list_2:
#     print(f"Element present are: {i}")

# for i in range(0,len(my_list_2)):
#     print(f"Element at index value {i}: {my_list_2[i]}")

# I have a list of fruits:
fruits = ["Mango","JackFruit","Banana","Apple","Orange"]
# If the fruit name is "Banana" then print true else print false
# # Empty list creation
# food= []
# for i in range(0, len(fruits)):
#     if (fruits[i] == "Banana"):
#         food.append(fruits[i])


# print(fruits)
# print(food)

# for i in fruits:
#     if i == "Banana":
#         print("True")
#     else:
#         print("False")
food = []
for i in fruits:
    if i == "Banana":
        food.append(i)
print(food)
# # List Comprehension
# Syntax:
# newlist = [expression for item in anotherlist if condition]
foods = [i for i in fruits if i != "Banana"]
print(foods)

#  new list = [2,4,6,8,10,12]
new_list = [2*i for i in range(1,7)]
print(new_list)

given_numbers = [1,2,3,4,5,6,7,8,9,10]
odd_list = []
for i in given_numbers:
    if i%2 != 0:
        odd_list.append(i)
print(odd_list)

odd_num_list = [i for i in given_numbers if i%2 != 0]
print(f"Odd number list using list comprehension: {odd_num_list}")
# # Built-in Functions
# # Built-in Methods

