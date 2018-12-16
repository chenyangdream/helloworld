def create_teacher(name):
    print('name = %s' % name)
    return Teacher(name, region)

def create_student(name):
    return Student(name)

def is_a_teacher(name):
    return name in teachers
