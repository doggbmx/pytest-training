import pytest
from source.school import Classroom, TooManyStudents, Teacher, Student

@pytest.fixture
def empty_classroom():
    return Classroom(Teacher("Snake"), [], "Stealth 101")

@pytest.fixture
def full_classroom():
    students = [Student(f"Student{i}") for i in range(10)]
    return Classroom(Teacher("Ocelot"), students, "Combat Training")

def test_add_student(empty_classroom):
    student = Student("Raiden")
    empty_classroom.add_student(student)
    assert len(empty_classroom.students) == 1

def test_add_student_raises_exception(full_classroom):
    with pytest.raises(TooManyStudents):
        full_classroom.add_student(Student("Meryl"))

def test_remove_student(full_classroom):
    full_students = [student.name for student in full_classroom.students]
    print("Full students:", full_students)
    student_name = "Student3"
    full_classroom.remove_student(student_name)
    remaining_students = [student.name for student in full_classroom.students]
    print("Remaining students:", remaining_students)
    assert all(student.name != student_name for student in full_classroom.students)


def test_change_teacher(empty_classroom):
    new_teacher = Teacher("Liquid Snake")
    empty_classroom.change_teacher(new_teacher)
    assert empty_classroom.teacher.name == "Liquid Snake"

@pytest.mark.parametrize("num_students", [8, 9, 10])
def test_add_student_parametrize(empty_classroom, num_students):
    for i in range(num_students):
        student = Student(f"Student{i}")
        empty_classroom.add_student(student)
    assert len(empty_classroom.students) == num_students
