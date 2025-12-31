

#  Find the sum of even elements only.

arr = [1,23,4,5,4,34,23,12,25,56,57]
total = 0
for i in arr:
    if i % 2 == 0:
     print(i)
    total += i
print("sum of even :",total)