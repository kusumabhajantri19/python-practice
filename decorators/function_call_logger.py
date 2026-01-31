

#Write a program to log function calls using a decorator in Python.

def login_function_call(func):
    def wrapper():
        print(f"function called {func.__name__}..")
        func()
    return wrapper

@login_function_call
def add():
    print("Ravi profile opened")

add()