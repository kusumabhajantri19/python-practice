
#using tuple

tuple = (2,56,36,3,5,-1)

for i in tuple:
    print(i)
    if i % 6 == 0:
        print(i)
        break
    else:
        print("no in divisible 6")