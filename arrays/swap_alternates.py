
# Swap alternate elements (1st ↔ 2nd, 3rd ↔ 4th, etc.).


arr = [1, 2, 3, 4, 5, 6]

print("Original array:", arr)

for i in range(0, len(arr)-1, 2):
    arr[i], arr[i+1] = arr[i+1], arr[i]   

print("After swapping alternates:", arr)