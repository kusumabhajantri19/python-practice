
# Decorator for logging

def logger(func):
    def wrapper():
        print(f"Function '{func.__name__} 'function being called..")
        func()
    return wrapper

@logger
def geet():
    print("Namaskar")

geet()