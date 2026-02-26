
##Quick Sort

def quicksort(arr):
    if len(arr) <= 1:              # base condition
        return arr

    p = arr[-1]                    # choose last element as pivot
    left = []
    right = []

    for i in range(len(arr) - 1):  # loop except pivot
        if arr[i] < p:             # elements smaller → left
            left.append(arr[i])
        else:                      # elements larger/equal → right
            right.append(arr[i])

    # Recursively sort left and right, then combine
    return quicksort(left) + [p] + quicksort(right)


arr = [4, 6, 3, 1, 2]
sorted_arr = quicksort(arr)
print(sorted_arr)