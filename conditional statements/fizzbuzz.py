


# Print "Fizz" if a number is divisible by 3, "Buzz" if divisible by 5, "FizzBuzz" if divisible by both, else "Invalid".

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print("Invalid")