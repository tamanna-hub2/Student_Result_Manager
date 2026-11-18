class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.marks = {}


class Course:
    def __init__(self, course_code, title, credit):
        self.course_code = course_code
        self.title = title
        self.credit = credit


class StudentResultManager:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def show_menu(self):
        print("\n===== Student Result Manager =====")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enter Marks")
        print("4. Show Result")
        print("5. Exit")

    def add_student(self):
        student_id = input("Enter Student ID: ").strip()

        if not student_id:
            print("Student ID cannot be empty!")
            return

        if student_id in self.students:
            print("Student ID already exists!")
            return

        name = input("Enter Student Name: ").strip()

        if not name:
            print("Student name cannot be empty!")
            return

        self.students[student_id] = Student(student_id, name)

        print("Student added successfully!")

    def add_course(self):
        course_code = input("Enter Course Code: ").strip()

        if not course_code:
            print("Course Code cannot be empty!")
            return

        if course_code in self.courses:
            print("Course Code already exists!")
            return

        title = input("Enter Course Title: ").strip()

        if not title:
            print("Course Title cannot be empty!")
            return

        try:
            credit = float(input("Enter Course Credit: "))

            if credit <= 0:
                print("Credit must be greater than 0!")
                return

        except ValueError:
            print("Invalid credit! Please enter a number.")
            return

        self.courses[course_code] = Course(
            course_code, title, credit
        )

        print("Course added successfully!")

    def enter_marks(self):
        student_id = input("Enter Student ID: ")

        if student_id not in self.students:
            print("Student not found!")
            return

        course_code = input("Enter Course Code: ")

        if course_code not in self.courses:
            print("Course not found!")
            return

        try:
            marks = float(input("Enter Marks (0-100): "))

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100!")
                return

        except ValueError:
            print("Invalid marks! Please enter a number.")
            return

        self.students[student_id].marks[course_code] = marks

        print("Marks added successfully!")
    def calculate_grade(self, marks):
        if marks >= 80:
            return "A+", 4.00
        elif marks >= 75:
            return "A", 3.75
        elif marks >= 70:
            return "A-", 3.50
        elif marks >= 65:
            return "B+", 3.25
        elif marks >= 60:
            return "B", 3.00
        elif marks >= 55:
            return "B-", 2.75
        elif marks >= 50:
            return "C+", 2.50
        elif marks >= 45:
            return "C", 2.25
        elif marks >= 40:
            return "D", 2.00
        else:
            return "F", 0.00
    def show_result(self):
        student_id = input("Enter Student ID: ").strip()

        if student_id not in self.students:
            print("Student not found!")
            return

        student = self.students[student_id]

        print("\n===== Student Result Sheet =====")
        print("Student ID:", student.student_id)
        print("Student Name:", student.name)

        total_points = 0
        total_credits = 0

        for course_code, marks in student.marks.items():
            course = self.courses[course_code]
            grade, point = self.calculate_grade(marks)

            print("\nCourse Code:", course.course_code)
            print("Course Title:", course.title)
            print("Marks:", marks)
            print("Grade:", grade)
            print("Grade Point:", point)

            total_points += point * course.credit
            total_credits += course.credit

        if total_credits > 0:
            cgpa = total_points / total_credits
            print("\nCGPA:", round(cgpa, 2))
        else:
            print("\nNo marks available!")
def main():
    manager = StudentResultManager()

    while True:
        manager.show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_student()

        elif choice == "2":
            manager.add_course()

        elif choice == "3":
            manager.enter_marks()

        elif choice == "4":
            manager.show_result()

        elif choice == "5":
            print("Thank you for using Student Result Manager!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()