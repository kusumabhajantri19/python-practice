

#Write a Python program with a function that takes a string as input, counts the number of digits, sums them, and prints the total length of the string.

vowels =  "aeiouAEIOU"
def string(n):
    count = 0
    total = 0
    for item in n:
        if item.isdigit():
            count +=1
            total += int(item)
    print("total length:",len(n))
    print("total digits:",count)
    print("sum of digits:",total)


ch = input("Enter a name:")
string(ch)