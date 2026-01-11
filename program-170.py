
#count how many words contain letter a

sentence = input("Enter a sentence: ")

words = sentence.split()  
count = 0

for word in words:
    if 'a' in word or 'A' in word:  
        count += 1

print("Number of words containing letter 'a':", count)