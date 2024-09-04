# list comprehension in python

names = ['Retam', 'Archita', 'Tim', 'Ankita', 'Ron']
# using list comprehension to create a new list from the existing one

new_list = [x for x in names if 'i' in x]
print(new_list)
# the syntax of list comprehension
# new_list=[expression for item in iterable if condition ==True]

newlist = [x for x in range(10) if x > 5]
print(newlist)
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate
# before it ends up like a list item in the new list:
nameU = [x.upper() for x in names if 'a' in x]
print(nameU)

