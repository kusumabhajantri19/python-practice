
# Swap two specific characters in a string

word = "khushi"
result = ""

for ch in word:
    if ch == "k":
        result += "i"
    elif ch == "i":
        result += "k"
    else:
        result += ch

print(result)