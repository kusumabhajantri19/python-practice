

#  Compare two arrays — check if they are equal (same elements & order).

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5]

if len(arr1) != len(arr2):
    print("Not Equal")
else:
    equal = True

    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            equal = False
            break

    if equal:
        print("Both arrays are Equal")
    else:
        print("Not Equal")