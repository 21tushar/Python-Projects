# def outer_func():
#     message = 'Hello'
#
#     def inner_func():
#         print(message)
#
#     return inner_func
#
#
# my_func = outer_func()
# my_func()


def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func


hi_func = outer_func('Hi')
bye_func = outer_func('Bye')

hi_func()
bye_func()
