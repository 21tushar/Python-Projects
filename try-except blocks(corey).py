# try:
#     f = open('data.txt')
#     var = bad_var
# except FileNotFoundError:
#     print('This file does not exist')
# except Exception:
#     print('Sorry, something went wrong')


# try:
#     f = open('data.txt')
#     var = bad_var
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)


# try:
#     f = open('data.txt')
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print(f.read())
#     f.close()


try:
    f = open('data.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Executing Finally...')