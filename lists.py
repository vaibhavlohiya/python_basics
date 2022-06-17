"""
A python program about lists.
"""

friends = ['Abhinav', 'Ekansh', 'Yatharth', 'Nitin', 'Vikas', 'Yatharth']

print(friends[-2])
print(friends[1:])
print(friends[1:3])

friends[1] = 'Ketki' # to change the value of the elements in the list.

# functions 

lucky_numbers = [3, 7, 11, 17, 99, 69]

# friends.extend(lucky_numbers) # extend function 
print(friends)

friends.append('Saumya') # append function 
print(friends)

friends.insert(2, 'Kavana') # insert function 
print(friends)

friends.remove('Nitin') # remove function 
print(friends)

friends.pop() # pop's one element out of the list
print(friends)

print(friends.index('Kavana')) # to check the index of an element

print(friends.count('Yatharth')) # to count the occurence of a certain element.

friends.sort() # to sort the list on alphabatical or increasing order.
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse() # to reverse the list
print(lucky_numbers)

friends_2 = friends.copy()  # to copy a list
print(friends_2)

friends.clear() # clear function (erases everything)
print(friends)