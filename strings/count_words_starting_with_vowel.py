
#Print how many words start with a vowel in a sentence.

sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
count = 0

words = sentence.split()  

for word in words:
    if word[0] in vowels:  
        count += 1

print("Number of words starting with a vowel:", count)