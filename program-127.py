
# Find the second smallest element in an array.

arr = [4, 2, 7, 1, 9, 5]

smallest = min(arr)
arr.remove(smallest)
second_smallest = min(arr)

print("Second smallest element:", second_smallest)