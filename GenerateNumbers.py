# Given 4 digits 1,2,3 and 4 generate unique 3 digit numbers as follows
# 123   213  312    412
# 124   214  314    413
# 132   231  321    421
# 134   234  324    423
# 142   241  341    431
# 143   243  342    432

count = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and i!=k and j!=k:
                print(i,j,k)
                count +=1

print(f"Total number of unique value: {count}")