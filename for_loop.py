"""
A python program on for loop and it's functionalities.
"""

# Printing out letters using for loop.

for letter in 'Vaibhav Lohiya':
    print(letter)

# Printing out elements from a list.

friends = ['Abhinav', 'Ekansh', 'Yatharth']

for friend in friends:
    print(friend)

# Printing out numbers using range.

for index in range(20):
    print(index)

for index in range(5, 10):
    print(index)

for index in range(len(friends)):
    print(friends[index])

# Building an exponent function using for loop

def power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result *= base_num
    return result

print(power(2, 3))