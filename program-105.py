
5. Check if all elements in an array are unique.


arr = [2, 4, 6, 8, 10, 4]

if len(arr) == len(set(arr)):    
    print("All elements are unique")
else:
    print("Duplicates found")