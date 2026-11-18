import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout
from main import StudentResultManager, Student, Course


class TestStudentResultManager(unittest.TestCase):

    def setUp(self):
        self.manager = StudentResultManager()

    # Test 1: Add Student
    def test_add_student(self):
        with patch("builtins.input", side_effect=["020", "Megha"]):
            self.manager.add_student()

        self.assertIn("020", self.manager.students)

    # Test 2: Duplicate Student ID
    def test_duplicate_student(self):
        with patch("builtins.input", side_effect=["020", "Megha"]):
            self.manager.add_student()

        with patch("builtins.input", side_effect=["020"]):
            self.manager.add_student()

        self.assertEqual(len(self.manager.students), 1)

    # Test 3: Add Course
    def test_add_course(self):
        with patch(
            "builtins.input",
            side_effect=["CSE433", "Data Science", "3"]
        ):
            self.manager.add_course()

        self.assertIn("CSE433", self.manager.courses)

    # Test 4: Calculate Grade
    def test_calculate_grade(self):
        grade, point = self.manager.calculate_grade(85)

        self.assertEqual(grade, "A+")
        self.assertEqual(point, 4.00)

    # Test 5: Enter Marks
    def test_enter_marks(self):
        self.manager.students["020"] = Student("020", "Megha")
        self.manager.courses["CSE433"] = Course(
            "CSE433", "Data Science", 3
        )

        with patch(
            "builtins.input",
            side_effect=["020", "CSE433", "85"]
        ):
            self.manager.enter_marks()

        self.assertEqual(
            self.manager.students["020"].marks["CSE433"], 85
        )

    # Test 6: Reject Marks Above 100
    def test_marks_above_100(self):
        self.manager.students["020"] = Student("020", "Megha")
        self.manager.courses["CSE433"] = Course(
            "CSE433", "Data Science", 3
        )

        with patch(
            "builtins.input",
            side_effect=["020", "CSE433", "105"]
        ):
            self.manager.enter_marks()

        self.assertNotIn(
            "CSE433", self.manager.students["020"].marks
        )

    # Test 7: Reject Negative Marks
    def test_negative_marks(self):
        self.manager.students["020"] = Student("020", "Megha")
        self.manager.courses["CSE433"] = Course(
            "CSE433", "Data Science", 3
        )

        with patch(
            "builtins.input",
            side_effect=["020", "CSE433", "-5"]
        ):
            self.manager.enter_marks()

        self.assertNotIn(
            "CSE433", self.manager.students["020"].marks
        )


# Test 8: Grade Scale Range Testing
    def test_grade_scale_ranges(self):
        grade_ranges = [
            (100, "A+", 4.00),
            (80, "A+", 4.00),
            (79, "A", 3.75),
            (75, "A", 3.75),
            (74, "A-", 3.50),
            (70, "A-", 3.50),
            (69, "B+", 3.25),
            (65, "B+", 3.25),
            (64, "B", 3.00),
            (60, "B", 3.00),
            (59, "B-", 2.75),
            (55, "B-", 2.75),
            (54, "C+", 2.50),
            (50, "C+", 2.50),
            (49, "C", 2.25),
            (45, "C", 2.25),
            (44, "D", 2.00),
            (40, "D", 2.00),
            (39, "F", 0.00),
            (0, "F", 0.00)
        ]

        for marks, expected_grade, expected_point in grade_ranges:
            with self.subTest(marks=marks):
                grade, point = self.manager.calculate_grade(marks)

                self.assertEqual(grade, expected_grade)
                self.assertEqual(point, expected_point)

    # Test 9: Weighted CGPA Testing
    def test_cgpa_calculation(self):
        self.manager.students["020"] = Student("020", "Megha")

        self.manager.courses["CSE433"] = Course(
            "CSE433", "Data Science", 3
        )
        self.manager.courses["CSE434"] = Course(
            "CSE434", "Programming", 1
        )

        self.manager.students["020"].marks = {
            "CSE433": 85,
            "CSE434": 75
        }

        output = StringIO()

        with patch("builtins.input", return_value="020"):
            with redirect_stdout(output):
                self.manager.show_result()
        self.assertIn("CGPA: 3.94", output.getvalue())
    # Test 10: Show Result Sheet Testing
    def test_show_result_sheet(self):
        self.manager.students["020"] = Student("020", "Megha")

        self.manager.courses["CSE433"] = Course(
            "CSE433", "Data Science", 3
        )

        self.manager.students["020"].marks = {
            "CSE433": 85
        }

        output = StringIO()

        with patch("builtins.input", return_value="020"):
            with redirect_stdout(output):
                self.manager.show_result()

        result = output.getvalue()

        self.assertIn("Megha", result)
        self.assertIn("CSE433", result)
        self.assertIn("Data Science", result)
        self.assertIn("85", result)
        self.assertIn("A+", result)
        self.assertIn("4.0", result)
        self.assertIn("CGPA", result)
if __name__ == "__main__":
    unittest.main()