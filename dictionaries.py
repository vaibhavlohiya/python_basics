"""
A python program to make dictionaries.
"""

monconversion = {
    'Jan' : 'January',
    'Feb' : 'Febuary',
    'Mar' : 'March',
    'Apr' : 'April',
    'Jun' : 'June',
    'Jul' : 'July',
    'Aug' : 'August',
    'Sep' : 'September',
    'Oct' : 'October',
    'Nov' : 'November',
    'Dec' : 'December'
}

print(monconversion['Feb'])

print(monconversion.get('Apr')) # we can pass a default value in get function when a certain key is not found in the dictionary.

print(monconversion.get('Cuv', 'Not a valid key '))

weekconversion = {
    1 : 'Monday',
    2 : 'Tuesday',
    3 : 'Wednesday',
    4 : 'Thursday',
    5 : 'Friday',
    6 : 'Saturday',
    7 : 'Sunday'
}

print(weekconversion[3])
