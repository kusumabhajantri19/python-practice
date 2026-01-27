
# Print the reverse of a given number

num = input("Enter a number: ")

rev = ""
for digit in num:
    rev = digit + rev

print("Reversed number:", rev)