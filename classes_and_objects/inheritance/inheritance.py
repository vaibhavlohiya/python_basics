"""
A python program about inheritance.
"""

from chef import Chef
from chinese_chef import chinese_chef

myChef = Chef()
myChef.make_chicken()

myChineseChef = chinese_chef()
myChineseChef.make_salad()   # This particular function is inherited from the class Chef.
myChineseChef.make_fried_rice()