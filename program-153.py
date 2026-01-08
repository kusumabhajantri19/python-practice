

#Print the middle character(s) of a string.

s = input("Enter a string: ")

length = len(s)
mid = length // 2  

if length % 2 == 0:
    print("Middle characters:", s[mid-1:mid+1])
else:
    print("Middle character:", s[mid])