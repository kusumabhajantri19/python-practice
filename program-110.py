
# Replace all even numbers with 1 and all odd with 0.

arr = [2, -1, 4, 6, 4, -3, -0, 6, 7]

print("Original array:", arr)

for i in range(len(arr)):
    if arr[i] % 2 == 0:    
        arr[i] = 1
    else:                 
        arr[i] = 0

print("Modified array:", arr)