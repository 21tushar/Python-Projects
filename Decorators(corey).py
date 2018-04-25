# def outer_func():
#     message = 'Hi'
#
#     def inner_func():
#         print(message)
#
#     return inner_func
#
#
# my_func = outer_func()
# my_func()
# my_func()


# def outer_func(msg):
#     message = msg
#
#     def inner_func():
#         print(message)
#
#     return inner_func
#
#
# hi_func = outer_func('Hi')
# hello_func = outer_func('Hello')
#
# hi_func()
# hello_func()


# def decorator_function(original_function):
#     def wrapper_function():
#         return original_function()
#
#     return wrapper_function
#
#
# def display():
#     print('display function ran')
#
#
# decorated_display = decorator_function(display)
# decorated_display()


# def decorator_function(original_function):
#     def wrapper_function():
#         print('wrapper executed this before {}'.format(original_function.__name__))
#         return original_function()
#
#     return wrapper_function
#
#
# @decorator_function
# def display():
#     print('display function ran')
#
#
# display()


# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print('wrapper executed this before {}'.format(original_function.__name__))
#         return original_function(*args, **kwargs)
#
#     return wrapper_function
#
#
# @decorator_function
# def display():
#     print('display function ran')
#
#
# @decorator_function
# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name, age))
#
#
# display_info('John', 26)
# display()


# class decorator_class(object):
#
#     def __init__(self, original_function):
#         self.original_function = original_function
#
#     def __call__(self, *args, **kwargs):
#         print('call method executed this before {}'.format(self.original_function.__name__))
#         return self.original_function(*args, **kwargs)
#
#
# @decorator_class
# def display():
#     print('display function ran')
#
#
# @decorator_class
# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name, age))
#
#
# display_info('John', 27)
# display()


# def my_timer(original_function):
#     import time
#
#     def wrapper_function(*args, **kwargs):
#         t1 = time.time()
#         result = original_function(*args, **kwargs)
#         t2 = time.time() - t1
#         print('{} ran in: {} sec'.format(original_function.__name__, t2))
#         return result
#
#     return wrapper_function
#
#
# @my_timer
# def display():
#     print('display function ran')
#
#
# @my_timer
# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name, age))
#
#
# display_info('John', 34)
# display()
