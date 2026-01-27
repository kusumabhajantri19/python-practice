

# Check if the input entered by the user is a letter, a digit, or neither.

ch = input("enter a character/digit/word: ")
if 'a' <= ch <= 'z' or 'A'<= ch <= 'Z':
    print(f"{ch} is a letter")
elif '0' <= ch <= '999':  #its a unicode value so in''like binary values it take
    print(f"{ch} is a digit")
else:
    print(f"{ch} is neither a letter or digit")