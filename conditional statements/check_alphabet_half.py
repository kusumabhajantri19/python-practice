


# Determine if a character entered by the user lies in the first half, second half of the alphabet, or is not a letter.

ch = input("Enter a character: ")

if 'a' <= ch <= 'm' or 'A' <= ch <= 'M':
    print("Lies in first half of alphabet")
elif 'n' <= ch <= 'z' or 'N' <= ch <= 'Z':
    print("Lies in second half of alphabet")
else:
    print("Not an alphabet letter")