
# Print sum of first n natural numbers recursively.

def sum_natural(n):
    if n == 0:          
        return 0
    return n + sum_natural(n - 1)
    print(sum_natural(n))


n = int(input("Enter n: "))
print(sum_natural(n))