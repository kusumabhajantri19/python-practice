
# print multiple values of ASCII values


values = input("Enter ASCII values separated by space: ")

for v in values.split():
    print(v, "=", chr(int(v)))
