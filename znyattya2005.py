'''class Student:
    print('Hi')
    def __init__(self):
        self.height=160
        print("I am alive")
        # print(self)

first_student=Student()
print(first_student.height)'''

'''class Pupil:
    def __init__(self, height=160):
        self.height=height

nick=Pupil()
kate=Pupil(height=170)
print(nick.height)
print(kate.height)'''
class Student:
    amount_of_students=0
    def __init__(self, height=172):
        self.height=height
        Student.amount_of_students +=1

nick=Student()
print(nick.height)
print(nick.amount_of_students)
kate=Student(height=170)
print(kate.height)
print(kate.amount_of_students)