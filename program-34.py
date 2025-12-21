

num = int(input("Enter a 4-digit number: "))


if 1000 <= num <= 9999:
    first_digit = num // 1000
    last_digit = num % 10

    if first_digit == last_digit:
        print("First and last digits are equal")
    else:
        print("First and last digits are not equal")
else:
    print("Invalid input! Enter a 4-digit number.")