
#Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the
#origin

x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

if x == 0 and y == 0:
    print("The point is at the Origin")
elif y == 0:
    print("The point lies on the X-axis")
elif x == 0:
    print("The point lies on the Y-axis")
else:
    print("The point is not on any axis")