import datetime
print("Hi khushi!")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))


a = datetime.date(year, month, day)
print(f"today is {a:%A} {datetime.date.today()}.Good evening!")
print("Let’s check your health profile."
      "Please tell me your height (in cm). ")
height = int(input("Enter height:"))
print(f"your height is {height}cm")
print(" Great! Now your weight (in kg)? ")
weight = int(input("Enter weight:"))
print(f"your weight is {weight}kg")
import datetime
B_year = int(input("Enter birth year: "))
B_month = int(input("Enter birth month: "))
B_day = int(input("Enter birth day: "))
dob = datetime.date(B_year, B_month, B_day)
today = datetime.date.today()
age = today.year - dob.year
if (today.month, today.day) < (dob.month, dob.day):
    age -= 1
print(f" Thanks! You are {age} years old")
print("Calculating your BMI...")
height_m = height / 100

# calculate BMI
BMI = weight / (height_m ** 2)

print(f"Your BMI is {BMI:.1f}")
if BMI < 18.5:
      print("Which means you are in Underweight.")
elif 18 <= BMI <=24.9:
     print(" which means You are in normal weight.")
elif 25<= BMI <29.9 :
     print(" Which means You are in Overweight.")
else:
    print("Which means you are in Obese.")
    print("Based on your BMI and goal, here’s your personalized plan:  ")


if BMI < 18.5:
    calories = 2200
    plan = "- Breakfast: Oats with milk, nuts, and fruits\n" \
           "- Lunch: Rice/chapati, dal, vegetables, lean protein\n" \
           "- Snacks: Smoothie, yogurt, dry fruits\n" \
           "- Dinner: Rice with curry or pasta with vegetables"
elif 18.5 <= BMI <= 24.9:
    calories = 2000
    plan = ("- Breakfast: Eggs or oats with fruits"
           "- Lunch: Chapati/rice, dal, vegetables, protein"
           "- Snacks: Fruits, yogurt, nuts"
           "- Dinner: Light meal – soup, salad, grilled vegetables"
)
elif 25 <= BMI < 29.9:
    calories = 1800
    plan = ("- Breakfast: Oats with fruits, boiled eggs"
           "- Lunch: 2 chapatis, vegetables, dal, salad"
           "- Snacks: Green tea, fruits"
           "- Dinner: Soup and grilled vegetables"
            )
else:
    calories = 1500
    plan = ("- Breakfast: Smoothie with greens"
           "- Lunch: Brown rice/chapati, dal, vegetables"
           "- Snacks: Nuts in small portions, fruits"
           "- Dinner: Salad, soup, grilled paneer or fish"
            )


water_liters = calories / 1000


print(f"Recommended water intake: {water_liters:.1f} liters per day")


print("Exercise Recommendations:"
      "Moderate cardio 30-40min.")
print("Motivational Tip!  "
      "Keep going! Healthy choices today = stronger tomorrow.")
print("Would you like to save this plan or update your details?")












