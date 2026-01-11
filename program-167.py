
#smallest value

sentence = input("Enter a sentence: ")

words = sentence.split()  
smallest_word = ""

for word in words:
    if len(word) < len(smallest_word):
        longest_word = word

print("The smallest word is:", smallest_word)