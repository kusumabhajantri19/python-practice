
##Bubble Sort

arr = [2, 6, 1, 3, 7]
print("Original array:", arr)

# Outer loop: repeat passes
for j in range(len(arr)-1):
    # Inner loop: compare adjacent elements
    for i in range(0, len(arr)-1-j):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            pass  # optional, can also remove this line

print("Sorted array:", arr)