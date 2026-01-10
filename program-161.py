
#Remove consecutive duplicate characters (e.g., “aaabb” → “ab”).

s = input("Enter a string: ")

if not s:  
    result = ""
else:
    result = s[0]  

    for ch in s[1:]:
        if ch != result[-1]:  
            result += ch      

print("String after removing consecutive duplicates:", result)