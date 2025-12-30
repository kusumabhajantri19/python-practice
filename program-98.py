
# Find the index of the maximum element.


n= int(input("Enter a numbers:"))
arr = []

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    arr.append(num)
maximum = max(arr)
maximum_index = arr.index(maximum)  

print("The numbers are:")
for x in arr:
    print(x)
print("Maximum value =", maximum)
print("Index of  max value  =", maximum_index )