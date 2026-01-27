
#captilize the first letter  of each word

words = ["hello", "world"]
result = ""

for word in words:
    result += word[0].upper() + word[1:].lower() + " "  

print("Before strip:", "'" + result + "'")
result = result.strip()  
print("After strip:", "'" + result + "'")