
students = [
    {"name": "ji", "marks": 17},
    {"name": "jiya", "marks": 56}
]
marks = [17,56]
# marks.sort()
# students.sort(reverse= True)
students.sort(key=lambda x: x["marks"], reverse=True)
print(students)