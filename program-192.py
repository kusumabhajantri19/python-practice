
vowels = "aeiouAEIOU"

def count_vowels(n):
    count = 0
    for item in n:
        if item in vowels:
            count += 1
    print("Vowel count:", count)

ch = input("Enter a name: ")
count_vowels(ch)
