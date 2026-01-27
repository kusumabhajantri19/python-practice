
# Count how many numbers are divisible by 3 and 5 both.

arr = [1, 15, 30, 45, 22, 60, 75, 10, 90, 100]
count = 0

for num in arr:
    if num % 3 == 0 and num % 5 == 0:
        count += 1

print("Count of numbers divisible by both 3 and 5 =", count)