nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# I want 'n' for each 'n' in nums

# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

# my_list = [n for n in nums]
# print(my_list)


# I want 'n*n' for each 'n' in nums

# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)

# my_list = [n*n for n in nums]
# print(my_list)


# Using Map + Lambda

# my_list = list((map(lambda n: n*n, nums)))
# print(my_list)


# I want 'n' for each 'n' in nums if 'n' is even

# my_list = []
# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)
# print(my_list)

# my_list = [n for n in nums if n%2 == 0]
# print(my_list)


# Using Filter + Lambda

# my_list = list(filter(lambda n: n%2 == 0, nums))
# print(my_list)


# I want (letter, num) for each letter in 'abcd' and each num in '0123'

# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))
# print(my_list)

# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list)


# Dictionary Comprehension
names = ['Andy', 'Hamilton', 'Karl', 'Sarah']
heros = ['Superman', 'Spiderman', 'Batman', 'WonderWoman']

# I want dict{'name': 'hero'} for each name, hero in zip(names, heros)

# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print(my_dict)

# my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Karl'}
# print(my_dict)

# print(dict(zip(names, heros)))


# Set Comprehension
nums = [1, 4, 2, 3, 1, 4, 5, 7, 6, 7]

# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)

# my_set = {n for n in nums}
# print(my_set)


# Generator Expressions

# I want to yield 'n*n' for each 'n' in nums

# def gen_func(nums):
#     result = []
#     for n in nums:
#         result.append(n*n)
#     return result
#
#
# my_gen = gen_func([1, 2, 3, 4, 5, 6])
# print(my_gen)


# def gen_func(nums):
#     for n in nums:
#         yield n*n
#
#
# my_gen = gen_func([1, 2, 3, 4, 5, 6])
#
# for i in my_gen:
#     print(i)


my_gen = (n*n for n in [1, 2, 3, 4, 5, 6])

for i in my_gen:
    print(i)