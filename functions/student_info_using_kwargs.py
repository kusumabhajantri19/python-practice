

#Write a function to display student details using keyword variable-length arguments.

def student_info(**details):
    for key,value in details.items():
        print(f"{key}: {value}")

student_info(name="khushi" , age=22, course="python")