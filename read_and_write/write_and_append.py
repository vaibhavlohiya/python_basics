"""
A python program to write and append in file.
"""

emp_file = open('employees.txt', 'a') # this is to append in the file employees.txt

emp_file.write('Andy - Idiot') # write a new entry in an existing file.

# emp_file.close()

"""
NOTE: If you run the program more than once it will append the new entry again into the file.
"""

# to avoid the above issue

emp_file.write('\nKelly - Customer Service') # to write on to the next line (use escape character - '\n')

# TO write in a new file. (You can also overwrite a file, this will delete the previous entries of the file.)

emp_file = open('employees_1.txt', 'w') # this will make a whole new file 

emp_file.write('Karen - Salesperson')

emp_file.close()
