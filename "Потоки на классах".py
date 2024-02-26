from threading import *
import time


class Knight(Thread):

    def __init__(self, name, skills, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skills = skills

    def run(self):
        enemies = 100
        days = enemies // self.skills
        for day in range(1, days + 1):
            enemies -= self.skills
            print(f'{self.name} защищается уже {day} день(дня); (осталось {enemies} врагов)')
            time.sleep(1)
        print(f'{self.name} отбился от врагов', end='\n')


ghoust1 = Knight(name='Berserk', skills=80)
ghoust2 = Knight(name='knight Leon', skills=20)
ghoust1.start()
ghoust2.start()

ghoust1.join()
ghoust2.join()


print('Бойцы отваивались')
