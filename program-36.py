

# Check if a number is a multiple of 7 or ends with 7.

num = int(input("Enter an integer: "))

if num % 7 == 0 or num % 10 == 7:
    print("The number is either a multiple of 7 or ends with 7")
else:
    print("The number is neither a multiple of 7 nor ends with 7")