

#  Finding Index of minimum value of array

n= int(input("Enter a numbers:"))
arr = []

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    arr.append(num)
minimum = min(arr)
minimum_index = arr.index(minimum)

print("The numbers are:")
for x in arr:
    print(x)
print("Maximum value =", minimum)
print("Index of  max value  =", minimum_index )