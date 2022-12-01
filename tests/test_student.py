from school_schedule.student import Student
from school_schedule.cohort import Cohort
from school_schedule.comparison import get_student_with_more_classes
'''
class Student():
    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade
        self.classes = classes

    def add_class(self, class_name):
        self.classes.append(class_name)

    def get_num_classes(self):
        return len(self.classes)

    def summary(self):
        return f"{self.name} is a {self.grade} enrolled in {self.get_num_classes()} classes"

nominal cases:
1- assessing the three attributes
2- assessing classes is a list
3- assert len(self.classes) is +1 after applying add_class()
4- assert new_class is in 

edge cases:
1- assert a typeerror is raised when missing an argument
2- assert an empty class classto add_class
'''
def test_check_for_validity_of_istances_of_attributes():
#Arrange
    claire = Student( 
            "Claire", 
            "freshman", 
            [ 
                "Algebra", 
                "Writing", 
                "Contemporary World Issues", 
                "Gym", 
                "Earth Science" 
            ]
        )
    samara = Student(
            "Samara", 
            "junior", 
            [ 
                "Pre-Calc", 
                "English III", 
                "World History", 
                "Gym", 
                "Chemistry", 
                "Music Composition" 
            ]
        )
# Act
    #new_student1 = Student(claire)
    #new_student2 = Student(samara)
#Assert
    assert samara.name == "Samara"
    assert samara.grade == "junior"
    assert len(samara.classes) == 6
    assert "Chemistry" in samara.classes

def test_add_class_to_add_valid_class_with_classname():
    #Arrange 
    samara = Student(
            "Samara", 
            "junior", 
            [ 
                "Pre-Calc", 
                "English III", 
                "World History", 
                "Gym", 
                "Chemistry", 
                "Music Composition" 
            ]
        )
    class_name = "Algorithm Practice"
    #Act
    
    samara.add_class(class_name)
    #Assert
    assert samara.classes == [ 
                "Pre-Calc", 
                "English III", 
                "World History", 
                "Gym", 
                "Chemistry", 
                "Music Composition",
                "Algorithm Practice"
            ]
    assert len(samara.classes) == 7

def test_check_get_correct_num_classes():
    # Arrange
    claire = Student( 
            "Claire", 
            "freshman", 
            [ 
                "Algebra", 
                "Writing", 
                "Contemporary World Issues", 
                "Gym", 
                "Earth Science" 
            ]
        )   
    #Act
    #new_student = Student(claire)

    #Assert
    assert claire.get_num_classes() == 5
def test_to_check_summary_method_returns_correct_summary():
    #Arrange
    claire = Student( 
            "Claire", 
            "freshman", 
            [ 
                "Algebra", 
                "Writing", 
                "Contemporary World Issues", 
                "Gym", 
                "Earth Science" 
            ]
        )
    #Act
    #new_student = Student(claire)
    new_student_summary = claire.summary()
    #
    assert new_student_summary == "Claire is a freshman enrolled in 5 classes"

def test_to_add_empty_class_name():
    #Arrange
    sylvia = Student( 
            "Sylvia", 
            "senior", 
            [ 
                "Calc I", 
                "Spanish Literature", 
                "Biology", 
                "Gym"
            ]
        )
    class_name = ""
    #Act
    #new_student = Student(sylvia)
    sylvia.add_class(class_name)

    #Assert
    assert len(sylvia.classes) == 4
def test_to_check_get_student_with_more_classes():
    #Arrange 
    sylvia = Student( 
            "Sylvia", 
            "senior", 
            [ 
                "Calc I", 
                "Spanish Literature", 
                "Biology", 
                "Gym"
            ]
        )
    claire = Student( 
            "Claire", 
            "freshman", 
            [ 
                "Algebra", 
                "Writing", 
                "Contemporary World Issues", 
                "Gym", 
                "Earth Science" 
            ]
        )   
    #Act
    #new_student1 = Student(claire)
    #new_student2 = Student(sylvia)
    student_with_more_classes = get_student_with_more_classes(sylvia,claire)

    #Assert
    assert student_with_more_classes == claire

# new comment
    