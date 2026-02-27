
# Find Maximum Element in a List

arr = [4, 7, 1, 9, 3]

max_value = arr[0]   

for num in arr:
    if num > max_value:
        max_value = num

print("Maximum element:", max_value)