"""
NOTE: This is a class that is inheriting functions from chef class.
"""
from chef import Chef

class chinese_chef(Chef):

    def make_special_dish(self):  # Just like this we can overwrite inherited functions from Chef class.
        print('The Chef makes orange chicken')

    def make_fried_rice(self):
        print('The Chef makes fried rice')
