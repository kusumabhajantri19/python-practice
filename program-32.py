
num = int(input("Enter a 3-digit number: "))


hundreds = num // 100        
tens = (num // 10) % 10      
units = num % 10           
if hundreds != tens and hundreds != units and tens != units:
    print("All digits are distinct")
else:
    print("Digits are not distinct")