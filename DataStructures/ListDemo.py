# # # List creation with default elements
# # colors = ["Violet","Indigo","Blue","Green","Yellow","Orange","Red"]



# # # # Accessing the elements
# # #     #printing all the elements
# # # print(colors)
# # #     # To access a specific element:
# # # print(colors[4])

# # # # Slicing the list
# # # # ------------------------------------------------------------------------------------------------
# # # # Prints the elements from the index value 2 till end of list
# # # print(colors[2:])
# # # # Prints the elements from the index value 2 till the range mentioned-1
# # # print(colors[2:5])
# # # # Prints the elements from the start till the 6th element
# # # print(colors[:6])
# # # # Prints empty list if the range mentioned in the slicing operation is not proper
# # # print(colors[5:2])
# # # # slicing using the negative index value
# # # print(colors[-5:-1])
# # # # Prints empty list if the range mentioned in the slicing operation is not proper
# # # print(colors[-1:-5])
# # # # prints the 
# # # print(colors[:-5])
# # # print(colors[-5:])
# # # # print the list in reverse order
# # # print(colors[::-1])

# # # # Reassigning the values inside the list
# # # # ------------------------------------------------------------------------------------------------

# # # my_numbers = [10,20,30,50,60,80,90,100]
# # # print(my_numbers)

# # # my_numbers[5] = 1000
# # # print(my_numbers)

# # # # Deleting the elements
# # # # ------------------------------------------------------------------------------------------------
# # # del my_numbers[5]
# # # print(my_numbers)

# # # #Deleting more than one element
# # # del my_numbers[5:]
# # # print(my_numbers)

# # # # Multidimensional list
# # # list = [1,2,[23,34,45,56],4,5,6]

# # # # Retrieve the element called (5)
# # # print(f"Expected Element: {list[4]}")
# # # print(f"Expected Element: {list[-2]}")
# # # print(f"Expected Element: {list[2]}")
# # # # Accessing the element inside the nested list:
# # # print(f"Expected Element: {list[2][2]}")

# # # # Concatenation of lists
# # # my_list_1 = [1,2,3,4,5]
# # # my_list_2 = [10,20,30,40,50]
# # # final_list = my_list_1 + my_list_2
# # # print(final_list)
# # # Operations on lists
# # my_list_1 = [1,2,3,4,5]
# # my_list_2 = [1.5,20,30,40,50,"Welcome",True,45+7j]
# # ops_list = my_list_1 * 2
# # print(ops_list)
# # # ops_list = my_list_1 * my_list_2[0]
# # # ops_list = my_list_1 * 2
# # ops_list = my_list_1 + my_list_2
# # print(ops_list)

# # # Iterations on lists

# # for i in range(0,8):
# #     print(f"Element at index value {i}: {my_list_2[i]}")
    
# # for i in my_list_2:
# #     print(f"Element present are: {i}")

# # for i in range(0,len(my_list_2)):
# #     print(f"Element at index value {i}: {my_list_2[i]}")

# # I have a list of fruits:
# fruits = ["Mango","JackFruit","Banana","Apple","Orange"]
# # If the fruit name is "Banana" then print true else print false
# # # Empty list creation
# # food= []
# # for i in range(0, len(fruits)):
# #     if (fruits[i] == "Banana"):
# #         food.append(fruits[i])


# # print(fruits)
# # print(food)

# # for i in fruits:
# #     if i == "Banana":
# #         print("True")
# #     else:
# #         print("False")
# food = []
# for i in fruits:
#     if i == "Banana":
#         food.append(i)
# print(food)
# # # List Comprehension
# # Syntax:
# # newlist = [expression for item in anotherlist if condition]
# foods = [i for i in fruits if i != "Banana"]
# print(foods)

# #  new list = [2,4,6,8,10,12]
# new_list = [2*i for i in range(1,7)]
# print(new_list)

# given_numbers = [1,2,3,4,5,6,7,8,9,10]
# odd_list = []
# for i in given_numbers:
#     if i%2 != 0:
#         odd_list.append(i)
# print(odd_list)

# odd_num_list = [i for i in given_numbers if i%2 != 0]
# print(f"Odd number list using list comprehension: {odd_num_list}")
# # Built-in Functions

# len - returns the number of items in the list
m_list = [1,23,346,467,689,78,456,34,23,46,58,6,45]
print(len(m_list))

# max
print(max(m_list))
#min
print(min(m_list))
#sum
print(sum(m_list))

#sorted - this will not affect the existing list
print(sorted(m_list))

#sorting in descending order
m = sorted(m_list)
print(m[::-1])

name = "Vigneshwaran"
c_name = list(name)
print(c_name)


# my_id = 123123
# c_id = list(my_id)
# print(c_id)



# # Built-in Methods

c = []
print(c)
c.append(10)
print(c)
c.append(20)
print(c)

c.insert(1,99)
print(c)

c.remove(99)
print(c)

#pop - removes the element specified in the pop method
print(m_list.pop())

print(m_list.index(346))

dummy_list = [12,34,45,56,67,12,34,12,34,12,12,12]
print(dummy_list.count(12))

# sort method alters the list completely
dummy_list.sort()
print(dummy_list)


print(dummy_list)

dummy_list.reverse()
print(dummy_list)

# To reverse using slice operation
# print(dummy_list[::-1])