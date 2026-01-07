
s = input("Enter a string: ")

digits = 0
letters = 0
special = 0

for ch in s:
    ascii_value = ord(ch)  

    if 48 <= ascii_value <= 57:  
        digits += 1
    elif (65 <= ascii_value <= 90) or (97 <= ascii_value <= 122): 
        letters += 1
    else:
        special += 1  

print("Letters:", letters)
print("Digits:", digits)
print("Special characters:", special)