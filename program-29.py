
 nums = ["zero","one","two","three","four","five","six","seven","eight","nine"]
#
digit = int(input("Enter a day number (0-9): "))

if 0 <= digit <= 9:
    print(nums[digit])
else:
    print("Invalid  number")