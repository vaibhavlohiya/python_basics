"""
A python program for object functions.
"""
from classes_and_objects import student

stud_1 = student('Oscar', 'Business', 3.2, True)
stud_2 = student('Phyllis', 'Accounting', 4.3, False)

print(stud_2.on_honor_roll())