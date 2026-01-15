
vowels =  "aeiouAEIOU"
def string(n):
    count = 0
    for item in n:
        if item in vowels:
            count +=1

    print(count)