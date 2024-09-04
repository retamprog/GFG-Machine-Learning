# here we are going to discuss some special python functions
# zip, lambda, filter,map

# zip
list1 = ['retam', 'archita', 'shanu']
list2 = [20, 21, 22]
print(list(zip(list1, list2)))
print('-' * 50)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix)
print(list(zip(*matrix)))
print([list(row) for row in zip(matrix)])
print([list(row) for row in zip(*matrix)])
print([list(row) for row in zip(*[list(row) for row in zip(*matrix)])])
print('-' * 50)
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
# scalar product of the two lists and their sum
print(sum([i * j for i, j in zip(lst1, lst2)]))
print("-" * 50)
lst = [x for x in range(10)]


def is_odd(n):
    return not n % 2 == 0


# filter
print(list(filter(is_odd, lst)))

# lambda
add_num = lambda x, y: x + y
print(add_num(5, 10))

num = [x for x in range(8)]

print(list(filter(lambda x: x % 2 != 0, num)))
print("-" * 50)


# map
def cube(x):
    return x ** 3


print(list(map(cube, num)))
print('-'*50)
print(ord(' '))
print(chr(90))
for x in range(33,200):
    print(chr(x))