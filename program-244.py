
#using error exception handling

a = int(input("a:"))
b = int(input("b:"))

try:
    print(a/b)
except Exception as e:
    print(f" Error :{e}")
    # b = int(input("b:"))
    # print(a/b)
else:
    print("No Error")
finally:
    print("program ended! do not care error")