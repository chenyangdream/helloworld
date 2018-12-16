def create_teacher(name, region):
    return Teacher(name, region)

def create_student(name):
    return Student(name)

def is_a_teacher(name):
    return name in teachers
