
# Write a program to demonstrate a login-required decorator in Python.

def login_required(func):
    def wrapper():
        print(f"Checking if us logged in..")
        func()
    return wrapper

@login_required
def view_profile():
    print("Ravi profile opened")

view_profile()