"""
NOTE: This is a testing script for the class student in the classes and objects file.
"""

from classes_and_objects import student

stud_1 = student('Jim', 'Physics', 4.0, False)

print(stud_1.name)
print(stud_1.gpa)

stud_2 = student('Pam', 'Art', 3.6, True)

print(stud_2.is_on_probation)
print(stud_2.major)

