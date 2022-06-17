"""
A python program about try and except statements
"""
try:
    value = 1/0  # putting an invalid number to catch two different types of errors.
    number = int(input('Enter a integer: '))
    print(number)
except ZeroDivisionError as err:
    # print('Divided by zero')
    print(err)  # we can simply printg out the error and move on, this will not lead to termination of the code.
except ValueError:
    print('Invalid number')
