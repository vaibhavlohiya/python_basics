"""
A python program to make a calculator
"""

num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
op = input('Enter the operator: ')

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1*num2)
elif op == '/':
    print(num1/num2)
else:
    print('The operation is invalid')