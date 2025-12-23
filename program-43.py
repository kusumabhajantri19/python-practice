
# Take a year and print the corresponding century (e.g., “19th century”, “20th century”)


year = int(input("Enter a year: "))
century = (year + 99) // 100
print(f"{century} century")