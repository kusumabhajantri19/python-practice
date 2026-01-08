
#Count how many words end with ‘s’.

sentence = input("Enter a sentence: ")

count = 0
words = sentence.split()  

for word in words:
    if word.endswith('s') or word.endswith('S'):  
        count += 1

print("Number of words ending with 's':", count)