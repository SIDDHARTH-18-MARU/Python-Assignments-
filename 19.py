students = {
    "John": {"age": 20, "courses": ["Math", "Science"], "CGPA": 3.8},
    "Alice": {"age": 22, "courses": ["English", "History"], "CGPA": 3.9},
    "Bob": {"age": 21, "courses": ["Physics", "Chemistry"], "CGPA": 3.6}
    }
students.update({"Wednesday":{"age": 23, "courses": ["Biology", "Psychology"], "CGPA": 4.0}})
print("Updated List: ",students)
for student in students:
    students[student]["CGPA"] += 0.1
print("Updated List: ",students)


#REDO