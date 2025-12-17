

ch = input("Enter a character: ")

if 'a' <= ch <= 'm' or 'A' <= ch <= 'M':
    print("Lies in first half of alphabet")
elif 'n' <= ch <= 'z' or 'N' <= ch <= 'Z':
    print("Lies in second half of alphabet")
else:
    print("Not an alphabet letter")