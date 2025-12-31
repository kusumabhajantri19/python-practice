
# Count how many times a given element appears.

n = int(input("Enter an element: "))
arr = [2,4,34,23,34,45,56,4,2,13,24,45,56,67]
count = 0

print(arr)

for i in arr:
    if i == n:
        count += 1
print(f"Appears  {count} time")