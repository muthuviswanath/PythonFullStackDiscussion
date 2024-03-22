rows = 6
cols = 6
for i in range(1,rows):
    for j in range(1,cols):
        print("*", end=" ")
    print()

# * 
# * *
# * * *
# * * * *
# * * * * *


rows = 6
cols = 6
for i in range(1,rows):             #i [1,2,3,4,5]
    for j in range(1,i+1):          #j [1]
        print("*", end=" ")
    print()

# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

rows = 6
cols = 6
for i in range(1,rows):             #i [1,2,3,4,5]
    for j in range(1,i+1):          #j [1]
        print(j, end=" ")
    print()
    
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

rows = 6
cols = 6
k = 1
for i in range(1,rows):             #i [1,2,3,4,5]
    for j in range(1,i+1):          #j [1]
        print(k, end=" ")
        k += 1
    print()

# 1 
# 2 3
# 4 5 6
# 7 8 9 1
# 2 3 4 5 6

# a 
# b b
# c c c
# d d d d
# e e e e e

rows = 6
cols = 6
k = 97
for i in range(1,rows):             #i [1,2,3,4,5]
    for j in range(1,i+1):          #j [1]
        print(chr(k), end=" ")
    k += 1    
    print()


# a 
# a b
# a b c
# a b c d
# a b c d e

# a 
# b c
# d e f
# g h i j
# k l m n o

# 1                     1
# 1 2 1                 3
# 1 2 3 2 1             5
# 1 2 3 4 3 2 1         7
# 1 2 3 4 5 4 3 2 1     9

odd = 1                         # odd : 3
for i in range (1,6):           # i : 2 ->[2,3,4,5]
    k = 0                       # k : 0
    for j in range(1,odd+1):    # j [1,2,3]
        if(j <= i):             # j <= i -> 3 <= 2 -> False
            k += 1              # k : 2  
        else:
            k -= 1              # k : 2 - 1 = 1
        print(k, end=" ")       # 1 
    print()                     # 1 2 1
    odd += 2

rows = 6
for i in range (1,rows+1):
    for j in range(1,i-1):
        print(j, end =" ")
    for j in range(i-1,0,-1):
        print(j, end =" ")
    print()


#     1                     
#    121                 
#   12321             
#  1234321         
# 123454321     

odd = 1                         # odd : 3
space = 4
for i in range (1,6):           # i : 2 ->[2,3,4,5]
    k = 0   
    # to print space
    for s in range(1,space+1):
        print(" ",end="")
        # k : 0
    for j in range(1,odd+1):    # j [1,2,3]
        if(j <= i):             # j <= i -> 3 <= 2 -> False
            k += 1              # k : 2  
        else:
            k -= 1              # k : 2 - 1 = 1
        print(k, end="")       # 1 
    print()                     # 1 2 1
    odd += 2
    space -= 1