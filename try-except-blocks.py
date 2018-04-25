try:
    a = open('examplefile,txt')
except FileNotFoundError:
    print('this code is incorrect')