#!/usr/bin/pyenv

class Teacher(object):

    def __init__(self, name):
        self.name = name

    def print(self):
        print("I am a Teacher.Name is %s" % self.name)
        
class MiddleSchoolTeacher(object):
    def __init__(self, name):
        self.name = name

    def print(self):
        print("I am a Middle School Teacher.Name is %s" % self.name)

class HighSchoolTeacher(object):
    def __init__(self, name):
        self.name = name

    def print(self):
        print("I am a High School Teacher.Name is %s" % self.name)
