
#Merge sort

lst = [1,6,8,4,2,9]

# Step 1: Split into two halves
mid = len(lst) // 2
left = lst[:mid]     # left part
right = lst[mid:]    # right part

# Step 2: Sort each half
left = sorted(left)
right = sorted(right)

# Step 3: Merge the two sorted halves
i = j = 0
sorted_list = []

while i < len(left) and j < len(right):
    if left[i] < right[j]:
        sorted_list.append(left[i])
        i += 1
    else:
        sorted_list.append(right[j])
        j += 1

# # Add remaining elements
# sorted_list.extend(left[i:])
sorted_list.extend(right[j:])

print("Previous list:", lst)
print("Sorted list:", sorted_list)
