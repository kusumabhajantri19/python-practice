

# Check if a lowercase character entered by the user lies in the alphabet ranges 'a-m' or 'n-z'.

ch = input("Enter a character:")
if 'a' <= ch <= 'm' or 'n' <= ch <= 'z':
    print("Lies")
else:
    print("not lies")