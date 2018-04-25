student = {'name': 'Prashant', 'age': 23, 'Courses': ['Python','C++','Spoken English']}

student.update({'name': 'Michael', 'age': 27, 'phone': '666-2456478'})

for key, value in student.items():
    print(key, value)


#print(student.get('class', 'Not Found'))