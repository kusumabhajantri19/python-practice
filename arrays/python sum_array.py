
# Find the sum of all elements in an array.


n= int(input("Enter a numbers:"))
arr = []
total = 0
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    arr.append(num)
    total += arr[i]
print("The numbers are:")
for x in arr:
    print(x)

print("Sum =", total)