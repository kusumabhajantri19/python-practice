
#Write a program to demonstrate local and global variables in Python.

def func():
    x = "khushi"
    print("Hello World")
    print(y)       #Global variable prints
    print(x)

y = "hi"
print(x)
func()     #local variable prints
