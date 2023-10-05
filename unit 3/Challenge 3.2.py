class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __repr__(self):
        return f"Student(name='{self.name}', roll_number='{self.roll_number}', cgpa={self.cgpa})"

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

students = [
    Student("Alice", "101", 3.8),
    Student("Bob", "102", 3.6),
    Student("Charlie", "103", 3.9),
    Student("David", "104", 3.7),
]

sorted_students = sort_students(students)

print("Sorted Students (by CGPA):")
for student in sorted_students:
    print(student)
