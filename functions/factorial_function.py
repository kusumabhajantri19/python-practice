

#Write a Python program with a function that takes a number as input and prints its factorial.

def cal_fact(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    print(fact)
cal_fact(5)