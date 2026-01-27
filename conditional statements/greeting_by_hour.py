


# Print a greeting based on the hour entered by the user (Good morning/afternoon/evening/night).

hours = int(input("Enter a hours(0-24):"))
if hours >=5 and hours <12:
    print("Good morning")
elif hours>= 12 and hours <17:
    print("Good afternoon")
elif hours >=17 and hours <21:
    print("Good evening")
else:
    print("Good night")