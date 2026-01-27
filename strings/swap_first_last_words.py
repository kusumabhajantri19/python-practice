
#Swap first and last words in a sentence.

sentence = input("Enter a sentence: ")

words = sentence.split()  

if len(words) >= 2:
    words[0], words[-1] = words[-1], words[0]  

swapped_sentence = " ".join(words)
print("Sentence after swapping first and last words:", swapped_sentence)