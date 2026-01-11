
#Count how many words have even length.

sentence = input("Enter a sentence: ")

words = sentence.split()  
count = 0

for word in words:
    if len(word) % 2 == 0:
        count += 1

print("Number of words with even length:", count)