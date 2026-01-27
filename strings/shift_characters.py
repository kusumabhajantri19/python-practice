
#Shift each character by 1 (e.g., “abc” → “bcd”).

s = input("Enter a string: ")

result = ""
for ch in s:
    result += chr(ord(ch) + 1)  

print("String after shifting each character by 1:", result)
