# if,elif,else,nested-if

#simple if:

# num = int(input("Enter a number"))
# if num >= 18:
#     print("Eligible to vote")
# else:
#     print("Not Eligible to vote")

# 0 - 5 : free
# 6 - 14 : 1/2
# 15 - 59:general
# >60: senior citizen
fare = 100
age = int(input("Enter the passenger Age: "))
if 0 < age <= 5:
    print("Free ticket")
elif age>=6 and age <=14:
    print("Half ticket")
elif age>=15 and age <=59:
    print("Full ticket")
else:
    fare = fare * 0.6
    print(fare)