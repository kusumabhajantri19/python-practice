
#Product of number using recurssion

def product_digits(n):
    if n < 10:          
        return n
    return (n % 10) * product_digits(n // 10)

n = int(input("Enter number: "))
print(product_digits(n))