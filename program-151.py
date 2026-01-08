

#. Print the second half of the string in reverse.


s = input("Enter a string: ")

half = len(s) // 2
second_half = s[half:]      
rev = second_half[::-1]     

print("Second half reversed:", rev)