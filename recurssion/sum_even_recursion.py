

# Sum of Even using recurssion

def sum_even(n):
    if n == 0:             
        return 0
    if n % 2 == 0:
        return n + sum_even(n - 1)
    else:
        return sum_even(n - 1)

n = int(input())
print(sum_even(n))