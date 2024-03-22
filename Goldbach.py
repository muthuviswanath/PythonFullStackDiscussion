# Express the given number as sum of two prime numbers if it is possible

# Given number: 10
# Output:
# 10 = 3 + 7
# 10 = 5 + 5
# 10 = 7 + 3

# Create a function that takes a number as input and return the Boolean value True if it is a prime number
# else it returns False if it is not a prime number

def isPrime(num): 
    factor = 0 # factor: 1
    for i in range(1,num+1): #i[1,2,3,4,5,6,7,8]
        if num % i == 0:
            factor += 1
    if factor == 2:
        return True
    else:
        return False

n = int(input("Enter a number to express it as sum of two prime numnbers: "))
for i in range(1, n+1): # [1,2,3,4,5,6,7,8,9,10]
    if isPrime(i) and isPrime(n-i):     # i: 1
        #True and True = True
        print (f"{n} = {i} + {n-i}")