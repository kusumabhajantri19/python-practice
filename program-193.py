
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