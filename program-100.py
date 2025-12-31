

# Take n elements and print only those greater than a given value k

arr = [ 2,4,6,78,45,34,12,23,34,45]
k = 24
for i in arr:
    if i> k:
        print(i)

  Another method
arr = [ 2,4,6,78,45,34,12,23,34,45]
k = 24

for i in range(len(arr)):    
    if arr[i] > k:
        print(arr[i])
#