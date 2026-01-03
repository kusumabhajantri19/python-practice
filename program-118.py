
# Compare two arrays — check if they contain the same elements (ignore order).

arr1 = [2,3,4,2,3,6,7,8,9,5]
arr2 = [2,4,3,5,7,8,9,3,2,6]


arr1_sorted = sorted(arr1)
arr2_sorted = sorted(arr2)


if arr1_sorted == arr2_sorted:
    print("Both arrays have the same elements (order ignored)")
else:
    print("Arrays are NOT equal")