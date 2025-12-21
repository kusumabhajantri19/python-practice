
#Take two angles of a triangle and compute the third angle

angle1 = float(input("Enter the first angle (in degrees): "))
angle2 = float(input("Enter the second angle (in degrees): "))


angle3 = 180 - (angle1 + angle2)

if angle3 > 0:
    print(f"The third angle is: {angle3} degrees")
else:
    print("Invalid angles! The sum of the first two angles must be less than 180.")