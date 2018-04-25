import os

# print(os.getcwd())

os.chdir('/root/Videos')

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)

    f_title, f_course, f_num = f_name.split(' - ')
    f_num = f_num[1:].zfill(2)

    new_file = '{}-{}{}'.format(f_num, f_title, f_ext)

    os.rename(f, new_file)