# Normal Approach
# square_numbers = [1,4,9,16,25]
numbers = [1,2,3,4,5]
square_numbers = []
for element in numbers:
    square_numbers.append(element ** 2)
print (square_numbers)


# List Comprehension:
# new_list = [expression(element) for element in old_list if condition]

# expression: Represents the operation that needs to be performed on each and every element within a list
# element: It is variable that represents the value that is taken from the list
# condition: It is a condition that decides whether the element should be addd to the new list or not

sq = [element ** 2 for element in numbers]
print(sq)


list = []
for i in range(11):
    if i % 2 == 0:
        list.append(i)

print(list)

lst = [i for i in range (11) if i%2 == 0]
print(lst)


[
    [0,1,2],
    [0,1,2],
    [0,1,2]
]

matrix = []
for i in range(1):
    matrix.append([])
    for j in range(1):
        matrix[i].append([])
        for k in range (3):
            matrix[i][j].append(k)

print(matrix)


vignesh_matrix = [[j for j in range(3)] for i in range(3)]
print(vignesh_matrix)

