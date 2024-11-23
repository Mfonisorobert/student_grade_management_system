# grades.py

from student import students

def calculate_course_average(course):
    """Calculates the average grade for a specific course."""
    total, count = 0, 0
    for grades in students.values():
        if course in grades:
            total += grades[course]
            count += 1
    return total / count if count > 0 else None

def get_highest_grade(course):
    """Returns the highest grade for a course."""
    highest_student, highest_grade = None, float('-inf')
    for student, grades in students.items():
        if course in grades and grades[course] > highest_grade:
            highest_grade = grades[course]
            highest_student = student
    return highest_student, course, highest_grade if highest_student else None

def get_lowest_grade(course):
    """Returns the lowest grade for a course."""
    lowest_student, lowest_grade = None, float('inf')
    for student, grades in students.items():
        if course in grades and grades[course] < lowest_grade:
            lowest_grade = grades[course]
            lowest_student = student
    return lowest_student, course, lowest_grade if lowest_student else None
