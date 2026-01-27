

#Write a Python program with a function that takes a string as input and prints the number of vowels in it.

vowels =  "aeiouAEIOU"
def string(n):
    count = 0
    for item in n:
        if item in vowels:
            count +=1

    print(count)