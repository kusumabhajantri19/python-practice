


# Check if a password entered by the user is at least 8 characters long and contains at least one digit.

password = input("Enter a password: ")

if len(password) >= 8 and (
    '0' in password or '1' in password or '2' in password or '3' in password or
    '4' in password or '5' in password or '6' in password or '7' in password or
    '8' in password or '9' in password
):
    print("Correct password")
else:
    print("Incorrect password")