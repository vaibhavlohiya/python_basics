"""
A python program about if/else statements.
"""

is_male = False  # Boolean variables
is_tall = True 

if is_male or is_tall:
    print('You are a male or tall or both')
else:
    print('You are neither male nor tall')

is_male = False  # Boolean variables
is_tall = False 

if is_male and is_tall:
    print('You are a tall male')
else:
    print('You are neither male nor tall')

is_male = True # Boolean variables
is_tall = False 

if is_male and is_tall:
    print('You are a tall male')
elif is_male and not is_tall:
    print('You are a short male')
else:
    print('You are neither male nor tall')

is_male = False # Boolean variables
is_tall = True 

if is_male and is_tall:
    print('You are a tall male')
elif is_male and not is_tall:
    print('You are a short male')
elif not is_male and is_tall:
    print('You are a not male but are tall')
else:
    print('You are neither male nor tall')

# Comparison statements (for example: >, <, >=, <=, ==, !=)

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(5, 9, 7))








