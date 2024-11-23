# student.py

students = {}  # Dictionary to store student data {student_name: {course: grade}}

def register_student(student_name, courses):
    """Registers a student and initializes their grades."""
    if student_name in students:
        return f"Student {student_name} is already registered."
    students[student_name] = {course: 0 for course in courses}
    return f"Student {student_name} registered successfully."

def add_or_update_grade(student_name, course, grade):
    """Adds or updates the grade for a specific student and course."""
    if student_name not in students:
        return f"Student {student_name} not found."
    if course not in students[student_name]:
        return f"Course {course} not found for {student_name}."
    students[student_name][course] = grade
    return f"Updated {student_name}'s grade for {course} to {grade}."
