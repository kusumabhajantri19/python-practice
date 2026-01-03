

#find common elements between two array

arr1 = [1, 2, 2, 3, 4, 5]
arr2 = [2, 2, 4, 6]

common = []  

for i in arr1:        
    if i in arr2:     
        if i not in common:  
            common.append(i)

print("Common elements:", common)