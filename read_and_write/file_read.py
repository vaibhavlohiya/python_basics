"""
A python program to read data from an external file.
"""

# How to open and close a file

emp_file = open('employees.txt', 'r') # abbriviations read - 'r', write - 'w', append - 'a', read & write - 'r+'

emp_file.close() # to close a file.

# How to read a file 

"""
NOTE: Once the file is opened and read from the user, you cannot access it again through any read functions.
TO do that you have first close and then again open the file.
"""

emp_file = open('employees.txt', 'r')

print(emp_file.readable())  # to check if the file is readable or not, if the mode is 'w' or 'a'. The output is 0.

print(emp_file.read()) # to read the whole file.

print(emp_file.readline()) # to read individual lines, starting with the first line and then the next lines in order
print(emp_file.readline())

print(emp_file.readlines()[3]) # this will read our lines and put them in an array.

for employee in emp_file.readlines():
    print(employee)

emp_file.close()

