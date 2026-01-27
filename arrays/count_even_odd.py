

# Count how many elements are even and odd.


n= int(input("Enter a numbers:"))
arr = []
even = 0
odd = 0
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    arr.append(num)
    if arr[i] % 2 == 0:
        even +=1
    else :
        odd +=1
print("The numbers are:")
for x in arr:
    print(x)

print("Total even =", even)
print("Total even =", odd)