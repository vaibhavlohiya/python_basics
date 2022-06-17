"""
A python program about 2-D lists and nested for loops.
"""

number_grid = [   # two dimentional list.
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print('row 2 column 1: ', number_grid[2][1])

# Nested for loop 

for row in number_grid:
    for column in row:
        print(column)

# Making a translator

"""
Monkey Language : Every vowel in a sentence becomes m.

dog --> dmg
cat --> cmt

"""
def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if letter.isupper():
                translation += 'M'
            else:
                translation += 'm'
        else: 
            translation += letter
    return translation

sen = input('Enter a sentence: ')

print(translate(sen))

