

#  Find the smallest and largest digit in a given number.


num = input("Enter a number: ")

small = 9
large = 0

for d in num:
    digit = int(d)

    if digit < small:
        small = digit

    if digit > large:
        large = digit

print("Smallest digit:", small)
print("Largest digit:", large)