class Person:
    def __init__(self, name_para, age_para):
        self.name = name_para
        self.age = age_para
    
    def __str__(self):
        return f"Name: {self.name} and age: {self.age}"
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
class Student(Person):

    major = ''
    studentID = ''

    def showInfo(self):
        print(f"A student name: {self.name} with ID: {self.studentID}  is study in major of:{self.major}")

costStudent = Student('David', '22')
costStudent.major= 'Computer Science'
costStudent.studentID = '603656'

print(costStudent.greet())
costStudent.showInfo()