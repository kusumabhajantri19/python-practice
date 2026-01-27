
# Count how many characters (excluding spaces) are in the string.

n = input("Enter a string: ")

count = 0
for ch in n:
    if ch != " ":      
        count += 1

print("Count:", count)