#using Decorator

 def welcome(func):
    def wrapper():
        print("Namaskar")
        func()
    return wrapper

@welcome
def intro():
    print("I am Khushi from Karnataka.")

intro()