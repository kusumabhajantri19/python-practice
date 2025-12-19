
hours = int(input("Enter a hours(0-24):"))
minutes = int(input("Enter a minutes(0-59):"))
# if hours >=5 and hours <12:
if 0<= hours < 12:
    print("Am")
elif 12<= hours < 24:
    print("pm")
else:
    print("invalid")