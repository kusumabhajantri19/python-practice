
 # print vowels in name

name = input("Enter your name: ")
vowels = "aeiouAEIOU"

for ch in name:
    if ch in vowels:
        print(ch)