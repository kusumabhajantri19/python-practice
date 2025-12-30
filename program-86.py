
#Palindrome using recurssion

def reverse_num(n, rev=0):
    if n == 0:
        return rev
    return reverse_num(n // 10, rev * 10 + n % 10)

def is_palindrome(n):
    return n == reverse_num(n)

n = int(input("Enter number: "))
print(is_palindrome(n))
