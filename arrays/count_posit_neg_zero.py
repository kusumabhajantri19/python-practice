
# Count how many elements are positive, negative, or zero.

n = int(input("Enter how many numbers: "))
arr = []

positive = 0
negative = 0
zero = 0

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    arr.append(num)

    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("The numbers are:")
for x in arr:
    print(x)

print("Positive count =", positive)
print("Negative count =", negative)
print("Zero count =", zero)