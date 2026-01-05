
words = input("Enter words separated by space: ")

print("Before split:", words)
print("After split:", words.split())

for w in words.split():
    print(w)
