
#Linear search

arr = [2,3,5,4,6,8,7]
target = int(input("Enter a target value:"))
for i in arr:
    if i==target:
       print(i)
       break
else:
    print("Not found")