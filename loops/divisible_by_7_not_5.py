
#Count how many numbers between 1–500 are divisible by 7 but not by 5.


count = 0
for i in range(1,501):
    if i % 7 ==0 and i % 5!=0:
        print(i)
        count += 1
print("count of numbers:",count)