
# // Decorator with arguments

def welcome(func):
    def wrapper(name):
        print("Namaskar")
        func(name)
    return wrapper

@welcome
def intro(name):
    print(f"I am {name} from Karnataka.")

intro("khushi")