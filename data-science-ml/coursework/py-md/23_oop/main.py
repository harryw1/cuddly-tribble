"""Module provides classes to represent students and grades as objects.

It demonstrates the use of classes, objects, and methods in Python.

"""

class Student:
    """Represents a student with their grades and attendance."""

    def __init__(self, name, year):
        """Initialize a Student object."""
        self.name = name
        self.year = year
        self.grades = []
        self.attendance = {}

    def add_grade(self, grade):
        """Add a grade to the student's record."""
        if isinstance(grade, Grade):
            self.grades.append(grade)
        else:
            return # Do nothing if the grade is not a Grade object

    def get_average(self):
        """Calculate the average grade of the student."""
        if not self.grades:  # Handle the case where there are no grades
            return 0.0  # Or some other appropriate default value

        total = 0
        for grade in self.grades:
            total += grade.score  # Access the score attribute of the Grade object

        return total / len(self.grades)


class Grade:
    """Represents a grade with a score and passing status."""
    
    def __init__(self, score):
        """Initialize a Grade object."""
        self.score = score
        self.minimum_passing = 65

    def is_passing(self):
        """Check if the grade is passing."""
        if self.score >= self.minimum_passing:
            return "Passing"
        else:
            return "Failing"


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)


pieter.add_grade(Grade(100))
pieter.add_grade(Grade(50))
print(pieter.get_average())