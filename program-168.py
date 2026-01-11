

sentence = input("Enter a sentence: ")

words = sentence.split()


smallest_word = words[0]

for word in words[1:]:
    if len(word) < len(smallest_word):
        smallest_word = word

print("The smallest word is:", smallest_word)