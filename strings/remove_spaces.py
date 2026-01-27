
# Remove all spaces from a string.

s = "Hello World"
vowels = "aeiouAEIOU"
result = ""

for ch in s:
    if ch not in vowels:
        result += ch

print("String without vowels:", result)