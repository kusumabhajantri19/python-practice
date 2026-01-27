
# Find the sum of all factors of a number.

num = int(input("Enter a number: "))
total = 0
print("Factors are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
        total +=i
print("total sum :",total)