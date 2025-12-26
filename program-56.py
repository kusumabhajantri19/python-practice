

#  Check if a number is a palindrome.

num = input("Enter a number: ")

rev = ""
for digit in num:
    rev = digit + rev     

if num == rev:
    print("Palindrome")
else:
    print("Not a palindrome")