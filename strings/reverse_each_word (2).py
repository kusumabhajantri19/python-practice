
# Reverse each word in a sentence

s = input("Enter a sentence: ")

words = s.split()
result = ""

for w in words:
    result += w[::-1] + " "

print(result)
