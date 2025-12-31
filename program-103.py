
 # Find the first occurrence of a given number.
 
n = int(input("Enter a number: "))
arr = [2,4,34,23,34,45,56,4,2,13,24,45,56,67]

print(arr)

for i in range(len(arr)):     
    if arr[i] == n:           
        print("First occurrence index =", i)
        break                 
else:
    print("Number not found")