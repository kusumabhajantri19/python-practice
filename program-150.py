
# Reverse each word in a sentence.


n = input("Enter a string: ")

rev = ""
words = n.split()

for word in words:
    rev = word + rev     

print("Reversed word:", rev)