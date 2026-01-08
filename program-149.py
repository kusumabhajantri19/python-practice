
# Reverse a string without using built-in reverse.

n = input("Enter a string: ")

rev = ""

for ch in n:
    rev = ch + rev      

print("Reversed string:", rev)