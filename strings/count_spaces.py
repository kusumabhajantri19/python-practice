

# Count how many spaces are in a sentence

sentence = input("Enter a sentence: ")

space_count = 0

for ch in sentence:
    if ch == " ":
        space_count += 1

print("Number of spaces:", space_count)
