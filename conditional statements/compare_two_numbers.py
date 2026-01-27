
# Check the temperature entered by the user and print "cold", "heat", or "normal" based on a reference value.


temperature = int(input ("enter temperature: "))
temp = 270
if temp > temperature:
    print("cold")
elif temp < temperature:
    print("heat")
else:
    print("normal")