import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print('I will sleep')
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print('Cast out...')
            self.alive = False

        elif self.gladness <= 0:
            print('Depression...')
            self.alive = False

        elif self.progress > 5:
            print('Passed externally...')
            self.alive=False

    def end_of_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Progress = {round(self.progress,2)}')

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f'{day:=^50}')
        print('1 - to study')
        print('2 - to sleep')
        print('3 - to chill')
        live_cube = (input('Enter your choice:'))
        if live_cube == '1':
            print('You entered 1 variant (study)')
            self.to_study()
        elif live_cube == '2':
            print('You entered 2 variant (sleep)')
            self.to_sleep()
        elif live_cube == '3':
            print('You entered 3 variant (chill)')
            self.to_chill()
        else:
            print('! Not correct choice. U can enter only 1 or 2 or 3 !')
        self.end_of_day()
        self.is_alive()

nick=Student(name='Nick')
for day in range(365):
    if nick.alive==False:
        print('Student lose')
        break
    nick.live(day)






