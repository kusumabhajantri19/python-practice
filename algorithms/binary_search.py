
#Binary search

arr = [2, 6, 1, 3, 7, 4, 9, 23, 12, 24]

# Step 1: sort the array
arr = sorted(arr)
print("Sorted array:", arr)

# Step 2: take target input
target = int(input("Enter a target value: "))

# Step 3: initialize pointers
first = 0
last = len(arr) - 1
found = False

# Step 4: binary search loop
while first <= last:
    mid = (first + last) // 2
    if arr[mid] == target:
        print(f"Found at index {mid}")
        found = True
        break
    elif target < arr[mid]:
        last = mid - 1
    else:
        first = mid + 1

# Step 5: if not found
if not found:
    print("Not found")