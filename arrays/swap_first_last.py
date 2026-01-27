
# Swap the first and last elements of the array.

arr = [2, -1, 4, 6, 4, -3, -0, 6, 7]
print("Original array:", arr)


temp = arr[0]
arr[0] = arr[-1]
arr[-1] = temp

print("Array after swapping:", arr)