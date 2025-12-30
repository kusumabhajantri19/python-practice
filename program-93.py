
# Find the average of array elements.

n= int(input("Enter a numbers:"))
arr = []
avg = 0
total = 0
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    arr.append(num)
    total += arr[i]
avg = total / n

print("The numbers are:")
for x in arr:
    print(x)

print("Total avg  =", avg)