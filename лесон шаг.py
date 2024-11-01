"""клас - це користувацький тип даних
"""
"""
class Student:
    def __init__(self): # конструтор класу - метод(функція), яка викликається автоматично при створені змінної(об'єкта)
        self.height = 160
        print("hello! I am a student at IT Step Academy")
        print("i am alive")


class Student2:
    def __init__(self, height = 170): # параметр за замовчуванням
        self.height = height
        
        print("I am Student PRO")

def Foo():
    print("Hello world")

def BrushTeeth(count_of_repeats = 2):
    for i in range(0, count_of_repeats):
        print("Піти до ванної")
        print("Взяти щітку")
        print("і тд")


Oleg = Student()
#Олег - тепер студент
print(Oleg.height)

kate = Student2(height=180)
print(kate.height)

Semen = Student2()
print(Semen.height)


BrushTeeth(5)
"""

"""
class Student:
    amount_of_student = 0
    def __init__(self, height = 160):
        Student.amount_of_student += 1
        self.height = height
    def grow(self, height_changer = 1):
        self.height += height_changer
    def getHeight(self):
        return self.height
    def __del__(self):
        print("Treining is over. I am now an expert")


Vitaliy = Student(180)
print(Vitaliy.height)
Vitaliy.grow(10)
print(Vitaliy.getHeight())

Kseniya = Student()

print(f"count of students: {Student.amount_of_student}")
"""


import random

class Student:
    def __init__(self, name):
        Student.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = 10

    def ToStudy(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5

    def ToSleep(self):
        print("I will sleep")
        self.gladness += 3

    def toChill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def IsAlive(self):
        if self.progress < -0.5:
            print("Cash out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False
    def endOfDay(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {self.progress}")
