"""
A python program about functions.
"""

def hello():            # always name a function in lowercase.
    print('Hello User')

print('Top')
hello()
print('Bottom')

# function with parameters

def hello(name, age):
    print('Hello ' + name + '! You are ' + str(age))

hello('Mike', 42)
hello('Steve', 14)

# using a return statement

def cube(value):
    return value*value*value

print(cube(33))