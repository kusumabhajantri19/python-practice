

#Replace all vowels with "*"

s = input("Enter a string: ")

vowels = "aeiouAEIOU"
result = ""

for ch in s:
    if ch in vowels:
        result += "*"  
    else:
        result += ch  

print("String with vowels replaced:", result)