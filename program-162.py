
# Swap case: uppercase → lowercase and lowercase → uppercase.

s = input("Enter a string: ")

result = ""
for ch in s:
    if ch.isupper():
        result += ch.lower()   
    elif ch.islower():
        result += ch.upper()   
    else:
        result += ch           

print("String after swapping case:", result)