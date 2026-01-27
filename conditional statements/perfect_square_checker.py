
# Check whether a number is a perfect square (without using the square root function)

num = int(input("Enter a number: "))


root = int(num ** 0.5)

if root * root == num:
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not a perfect square")