
# Find the minimum element in an array.

n= int(input("Enter a numbers:"))
arr = []

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    arr.append(num)
minimum = min(arr)

print("The numbers are:")
for x in arr:
    print(x)

print("Total min =", minimum)