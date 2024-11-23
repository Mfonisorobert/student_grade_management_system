# utils.py

from grades import calculate_course_average

def display_all_averages():
    """Displays the average grades for all courses."""
    print("\nCourse Averages:")
    all_courses = set()
    for grades in display_all_students.values():
        all_courses.update(grades.keys())

    for course in all_courses:
        avg = calculate_course_average(course)
        print(f"{course}: {avg:.2f}" if avg is not None else f"{course}: No grades yet.")

def display_all_students():
    """Displays all student grades."""
    print("\nAll Student Grades:")
    for student, grades in student.items():
        print(f"{student}: {grades}")
