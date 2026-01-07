
# count the number of digits ,letters, and special characters in a string.
#Another method

s = input("Enter a string: ")

digits = 0
letters = 0
special = 0

for ch in s:
    if '0' <= ch <= '9':         
        digits += 1
    elif 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':  
        letters += 1
    else:                           
        special += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special characters:", special)