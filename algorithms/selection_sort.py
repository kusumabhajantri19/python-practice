
##Sekection Sort

arr = [7, 4, 9, 2]

for i in range(len(arr)-1):          # Step 1: outer loop
    min_index = i                    # assume current position is minimum
    for j in range(i+1, len(arr)):   # Step 2: find minimum in unsorted part
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]  # Step 3: swap

print("Sorted array:", arr)