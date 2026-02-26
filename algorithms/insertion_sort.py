
#Insertion sort

arr = [5, 2, 4, 6, 1]

for i in range(1, len(arr)):
    key = arr[i]           # element to insert
    j = i - 1              # index of previous element

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]   # shift right
        j -= 1

    arr[j + 1] = key       # insert key

print(arr)