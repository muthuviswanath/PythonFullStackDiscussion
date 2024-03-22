# generate odd numbers from 1 to 20
# Check and tell whether the number entered by the user is a prime number or not

# a number which can be completely divided by 1 and itself is called a prime number
# there must be only 2 factors : 1 and the number

num = int(input("Enter a number to check whether it is prime or not"))

factor = 0
for i in range(1,num+1):
    if num % i == 0:
        factor += 1
if factor == 2:
    print("The given number ", num, " is prime")
else:
    print("The given number ", num, " is not prime")
