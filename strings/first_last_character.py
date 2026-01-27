


# Print the first and last character of a string

n = input("Enter a name: ")

for i in range(len(n)):
    if i == 0:
        print("First character:", n[i])
    if i == len(n) - 1:
        print("Last character:", n[i])