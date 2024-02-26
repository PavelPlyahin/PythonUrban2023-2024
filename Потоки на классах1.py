# Напишите программу с использованием механизмов многопоточности,
# которая создает два потока-рыцаря.
#
# Каждый рыцарь должен иметь имя (name) и умение(skill). Умение рыцаря определяет,
# сколько времени потребуется рыцарю, чтобы выполнить свою защитную миссию для королевства.
# Враги будут нападать в количестве 100 человек. Каждый день рыцарь может ослабить вражеское войско на skill-человек.
# Если у рыцаря skill равен 20, то защищать крепость он будет 5 дней (5 секунд в программе).
# Чем выше умение, тем быстрее рыцарь защитит королевство.
#
# В классе наследника (Knight), переопределите метод run,
# именно там будет заложена основная логика работы потоков.
# Используйте функцию sleep из модуля time для задержки времени

from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, skill, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill

    def fight(self, enemy):
        return min(enemy, self.skill)

    def run(self):
        enemies = 100
        days = 5
        day_count = 0
        for _ in range(days):
            while enemies != 0:
                enemy_weakened = self.fight(enemies)
                print(f'{self.name}, сражается {day_count + 1} день(дня), осталось {enemies} войнов')
                enemies -= enemy_weakened
                day_count += 1
                days -= 1
                sleep(1)

        print(f'{self.name} победил спустя {day_count} дней(дня)!')


knight1 = Knight("Sir Lancelot", 25) # Низкий уровень умения
knight2 = Knight("Sir Galahad", 40) # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()

print('Рыцари победили всех воинов')
