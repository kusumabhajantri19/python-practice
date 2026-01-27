
# Print only even numbers from 1 to n recursively.

def print_even(n):
    if n == 0:
        return 

    print_even(n - 1)  

    if n % 2 == 0:
        print(n)    

n = int(input("Enter a number: "))
print_even(n)   