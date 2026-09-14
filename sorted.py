students = [
    {"name": "Asha", "department": "CSE", "marks": 85},
    {"name": "Rahul", "department": "IT", "marks": 76},
    {"name": "Meera", "department": "CSE", "marks": 90},
    {"name": "John", "department": "ECE", "marks": 82},
    {"name": "Sara", "department": "IT", "marks": 88},
    {"name": "Ravi", "department": "ECE", "marks": 79}
]

# Sort by department first, then by marks in descending order
students.sort(key=lambda student: (student["department"], -student["marks"]))

print("Students sorted by Department and Marks:")
for student in students:
    print(f"Name: {student['name']}, Department: {student['department']}, Marks: {student['marks']}")
