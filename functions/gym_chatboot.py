


#gym chatboot

def calculate_bmi(height,weight):
    bmi = round(weight/(height**2),2)
    return bmi
print ("Welcome to  Gym Chatbox")
while True:
    user_input = input("you:")
    if user_input.lower() == "bmi":
        w = float(input(" enter weight in kg:"))
        h = float(input("Enter height in meter:"))
        result = calculate_bmi(h,w)
        print("chatbox:your bmi is",result)
        if result > 18:
            calories = 2200
            plan = "- Breakfast: Oats with milk, nuts, and fruits\n"
            print(f"you are in over weight {result}")
            print(f"your calories is {calories}")
            print(f"you need to prefer {plan}")

        elif result < 18:
            calories = 2000
            plan = "- Breakfast: Oats with milk, nuts, and fruits\n"