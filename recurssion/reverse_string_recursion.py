
#Reverse a string using recurssion

def reverse_string(s):
    if len(s) == 0:       
        return ""
    return s[-1] + reverse_string(s[:-1])


s = input("Enter string: ")
print(reverse_string(s))