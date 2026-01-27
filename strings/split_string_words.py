

# Write a program to split a string into words and print each word separately.

words = input("Enter words separated by space: ")

print("Before split:", words)
print("After split:", words.split())

for w in words.split():
    print(w)
