from school_schedule.student import Student
import pytest

def test_valid_student_initialization():
    # Arrange
    name = "yajuan"
    grade = "junior"
    classes = ["math", "art"]
    # Act

    yajuan = Student(name, grade, classes)


    # Assert
    assert yajuan.grade == "junior"
    assert "math" in yajuan.classes

def test_valid_student_initialization_with_empty_classes():
    #Arrange
    name = "yajuan"
    grade = "senior"
    classes = []

    #Act
    yajuan = Student(name, grade, classes)

    #assert 
    yajuan.get_num_classes() == 0



def test_invalid_student_initialization():
    # Arrange
    name = "yajuan"
    grade = "junior"


    with pytest.raises(TypeError):
        yajuan = Student(name, grade)


def test_add_valid_class():
    #Arrange
    class_name = "physics"
    name = "yajuan"
    grade = "junior"
    classes = ["math", "art"]

    yajuan = Student(name, grade, classes)

    #Act
    yajuan.add_class(class_name)

    #Assert
    assert yajuan.get_num_classes() == 3
    assert "physics" in yajuan.classes



def test_duplicate_class():
    #Arrange
    name = "yajuan"
    grade = "junior"
    classes = ["math", "physics", "art"]

    class_name = "art"

    #Act
    yajuan = Student(name, grade, classes)
    yajuan.add_class(class_name)

    #Assert
    assert yajuan.get_num_classes() == 4

    # The result should be pass here, but we can consider to check the duplicate class from add_class method



def test_valid_summary():
    #Arrange
    name = "yajuan"
    grade = "senior"
    classes = ["art", "music", "microeconomy"]

    summary = "yajuan is a senior enrolled in 3 classes"
    #Act
    yajuan = Student(name, grade, classes)

    #Assert

    assert yajuan.summary() == summary


