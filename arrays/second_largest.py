
# Find the second largest element in an array.


arr = [4, 2, 7, 1, 9, 5]

largest = max(arr)             
arr.remove(largest)            
second_largest = max(arr)      

print("Second largest element:", second_largest)