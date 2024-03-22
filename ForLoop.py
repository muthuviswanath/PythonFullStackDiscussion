# Range Function
# It will generate a range of values between lower_limit and higher_limit - 1
# range(higher_limit) default lower_limit is 0 and default step is 1
# range(lower_limit, higher_limit)default step is 1
# range(lower_limit,higher_limit,step)
# range(higher_limit,lower_limit,step_reverse)

for i in range(3,10,2):
    print (i)
    
for i in range(10,3,-2):
    print(i)
    
for i in range(3,10,-2):
    print(i)
    
name = "Vignesh"
for i in name:
    print(i)
    
colors = ["red", "green", "blue"]
for i in range(0,3):
    print(colors[i])

colors = ["red", "green", "blue"]
for i in colors:
    print(i)
    

adjectives = ["red", "big", "sour", "sweet", "tasty"]
fruits=["apple", "banana", "mango", "orange", "peech"]
for ad in adjectives:
    for fr in fruits:
        print(f"{ad} {fr}")
        # print(ad,fr)
        # print("{0}{1}".format(ad,fr))
    
for i in range(1,4):            # i:1
    for j in range(1,4):        # j:2
        print(i,j)              