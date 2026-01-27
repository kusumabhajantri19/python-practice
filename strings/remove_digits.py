
#Print the string after removing all digits.

s = input("Enter a string: ")

result = ""

for ch in s:
    if not ch.isdigit():  
        result += ch

print("String without digits:", result)
