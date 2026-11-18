import os
from graphviz import Digraph

# Graphviz executable path
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"

uml = Digraph("Student_Result_Manager")

# Diagram settings
uml.attr(
    rankdir="TB",
    label="Student Result Manager - UML Class Diagram",
    labelloc="t",
    fontsize="20",
    fontname="Arial",
    nodesep="0.8",
    ranksep="1.0",
    splines="ortho"
)

uml.attr(
    "node",
    shape="record",
    style="filled",
    fillcolor="lightblue",
    fontname="Arial",
    fontsize="10",
    margin="0.15"
)

# Student Class
uml.node(
    "Student",
    """{
    Student
    |
    + student_id
    + name
    + marks
    |
    + _init_(student_id, name)
    }"""
)

# Course Class
uml.node(
    "Course",
    """{
    Course
    |
    + course_code
    + title
    + credit
    |
    + _init_(course_code, title, credit)
    }"""
)

# StudentResultManager Class
uml.node(
    "Manager",
    """{
    StudentResultManager
    |
    + students
    + courses
    |
    + _init_()
    + show_menu()
    + add_student()
    + add_course()
    + enter_marks()
    + calculate_grade(marks)
    + show_result()
    }""",
    fillcolor="lightyellow"
)

# Keep Student and Course on the same level
with uml.subgraph() as s:
    s.attr(rank="same")
    s.node("Student")
    s.node("Course")

# Relationships
uml.edge(
    "Manager", "Student",
    label=" manages students ",
    arrowhead="vee"
)

uml.edge(
    "Manager", "Course",
    label=" manages courses ",
    arrowhead="vee"
)

# Student marks are stored using course codes
uml.edge(
    "Student", "Course",
    label=" marks stored by course_code ",
    style="dashed",
    arrowhead="vee"
)

# Generate PNG
uml.render(
    "Student_Result_Manager_UML",
    format="png",
    cleanup=True
)

print("UML Diagram generated successfully!")