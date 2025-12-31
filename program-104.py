
# Last occurrence

n = int(input("Enter a number: "))
arr = [2,4,34,23,34,45,56,4,2,13,24,45,56,67]

print(arr)

last_index = -1   

for i in range(len(arr)):
    if arr[i] == n:
        last_index = i    

if last_index == -1:
    print("Number not found")
else:
    print("Last occurrence index =", last_index)