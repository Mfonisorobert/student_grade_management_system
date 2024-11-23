# main.py

from student import register_student, add_or_update_grade
from grades import calculate_course_average, get_highest_grade, get_lowest_grade
from utils import display_all_averages, display_all_students

def main():
    print("Welcome to the Student Grade Management System!")
    while True:
        print("\nMenu:")
        print("1. Register Student")
        print("2. Add/Update Grade")
        print("3. Calculate Course Average")
        print("4. Get Highest Grade in a Course")
        print("5. Get Lowest Grade in a Course")
        print("6. Display All Course Averages")
        print("7. Display All Student Grades")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            name = input("Enter student name: ").strip()
            courses = input("Enter courses (comma-separated): ").strip().split(",")
            print(register_student(name, [course.strip() for course in courses]))
        elif choice == "2":
            name = input("Enter student name: ").strip()
            course = input("Enter course: ").strip()
            grade = float(input("Enter grade: ").strip())
            print(add_or_update_grade(name, course, grade))
        elif choice == "3":
            course = input("Enter course: ").strip()
            avg = calculate_course_average(course)
            print(f"Average grade for {course}: {avg:.2f}" if avg is not None else f"No grades found for {course}.")
        elif choice == "4":
            course = input("Enter course: ").strip()
            highest = get_highest_grade(course)
            print(f"Highest in {course}: {highest}" if highest else f"No grades found for {course}.")
        elif choice == "5":
            course = input("Enter course: ").strip()
            lowest = get_lowest_grade(course)
            print(f"Lowest in {course}: {lowest}" if lowest else f"No grades found for {course}.")
        elif choice == "6":
            display_all_averages()
        elif choice == "7":
            display_all_students()
        elif choice == "8":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
