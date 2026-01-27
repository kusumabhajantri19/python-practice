
# Input an element x — check if it exists in the array.

n = int(input("Enter an element: "))
arr = [2,4,34,23,34,45,56,4,2,13,24,45,56,67]

print(arr)

for i in arr:
    if i == n:
        print("exist")
        break
else:

    print("Not exist")