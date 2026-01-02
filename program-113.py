

# Rotate an array by one position to the left.

arr = [1, 2, 3, 4, 5]

print("Original array:", arr)

first = arr[0]   

for i in range(len(arr)-1):
    arr[i] = arr[i+1]   

arr[-1] = first   

print("Rotated array:", arr)