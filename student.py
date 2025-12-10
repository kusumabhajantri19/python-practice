import random
correct_name = "Kusuma"
correct_pin = "1234"
name = input("Enter your name: ")
if name != correct_name:
    print("Invalid Username!")
    exit()
print("Welcome to SBI ATM, priyanka!")
pin = input("Enter your PIN: ")
if pin != correct_pin:
    print("Invalid PIN!")
    exit()
otp = random.randint(1000, 9999)
print(f"Your OTP is: {otp}")
entered_otp = input("Enter the OTP: ")
if entered_otp != str(otp):
    print("Invalid OTP!")
    exit()


balance = 10000
withdraw = int(input("Enter amount to withdraw: "))

if withdraw > balance:
    print("Insufficient balance!")
    exit()

balance -= withdraw
print("Please collect your cash: withdraw")
print(f"Your new balance is: ₹{balance}")
