
#Iterate through a tuple, print each element, and stop when a number divisible by 6 is found

tuple = (2,56,36,3,5,-1)

for i in tuple:
    print(i)
    if i % 6 == 0:
        print(i)
        break
    else:
        print("no in divisible 6")