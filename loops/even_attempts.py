

#Write a Python program that prints all even attempt numbers from 1 to 100 using a while loop and continue

i = 1
while i <= 100:
    if i % 2 == 0:
        print(f"attempt {i}")
    i += 1
