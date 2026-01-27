
#count howmany times a given character appears in a string.

s = input("Enter a string: ")
ch = input("Enter a character to count: ")

count = 0

for c in s:
    if c == ch:
        count += 1

print(f"The character '{ch}' appears {count} times.")