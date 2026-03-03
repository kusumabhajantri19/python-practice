

#Student Information Function Example

def student_info(name, age=18, *marks, **details):
    print("Name:", name)
    print("Age:", age)
    
    print("Marks (args):", marks)
    
    if marks:
        print("Total Marks:", sum(marks))
    
    print("Other Details (kwargs):")
    for key, value in details.items():
        print(key, ":", value)


# Function Call
student_info(
    "Kusuma",
    22,
    85, 90, 88,
    city="Bangalore",
    course="Python"
)