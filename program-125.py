

# Check if the array is sorted in descending order.

arr = [5, 4, 3, 2, 1]

if arr == sorted(arr):
    print("Ascending order")
elif arr == sorted(arr, reverse=True):
    print("Descending order")
else:
    print("Not sorted")