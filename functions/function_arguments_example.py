
#Write a program to demonstrate function arguments in Python.

def marriage(boy,girl):      #parameters
    print(f"Boy is {boy}")
    print(f"Girl is {girl}")
    print(f"{boy} married {girl}")

marriage("khushi","jiya")       #positional arguments
marriage("hi","hell")
marriage(boy="hi", girl="hrt")   #keywoed arguments