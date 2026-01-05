

# Count how many words are in a sentence.

sentence = input("Enter a sentence: ")

count = 1
for ch in sentence:
    if ch == " ":
        count += 1

print("Word count:", count)