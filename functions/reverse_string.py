

 #Write a Python program with a function that takes a string as input and returns the reversed string.

def reverse_string(s):
    return s[::-1]

name = input("Enter a string: ")
print("Reversed:", reverse_string(name))
