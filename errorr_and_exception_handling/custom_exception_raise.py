

#Raising Custom Exceptions in Python

try:
    boy = input("Who do you friend..")
    if boy.lower() != "khushi":
        raise Exception("You can only friend khushi.select her!")
except Exception as e:
    print(f"Error:{e}")
else:
    print("yes . khushi is ready")