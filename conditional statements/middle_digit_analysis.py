


# Determine whether the middle digit of a 3-digit number is the largest, smallest, or neither.

num = int(input("Enter a 3-digit number: "))

hundreds = num // 100
tens = (num // 10) % 10
units = num % 10


if tens > hundreds and tens > units:
    print("Middle digit is the largest")
elif tens < hundreds and tens < units:
    print("Middle digit is the smallest")
else:
    print("Middle digit is neither largest nor smallest")