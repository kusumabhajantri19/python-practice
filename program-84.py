

#count the number of digits in a number recursively

def count_digits(n):
    if n == 0:               
        return 0
    return 1 + count_digits(n // 10)

n = int(input("Enter number: "))
print(count_digits(n))