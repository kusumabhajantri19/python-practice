
#find the elements that are in one array but not in other

arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7]


diff1 = []
for i in arr1:
    if i not in arr2:
        diff1.append(i)

diff2 = []
for i in arr2:
    if i not in arr1:
        diff2.append(i)

print("In arr1 but not in arr2:", diff1)
print("In arr2 but not in arr1:", diff2)