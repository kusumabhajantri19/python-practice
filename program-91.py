
#input n and take n integers into an array; print them.

n = int(input("Enter how many numbers: "))

arr = []   

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    arr.append(num)

print("The numbers are:")
for x in arr:
    print(x)