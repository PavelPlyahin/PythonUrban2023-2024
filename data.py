"""Задание:

Создайте класс SuperDate, наследованный от класса datetime модуля datetime,
объекты которого будут дополнительно обладать следующими методами:

1. get_season - должен возвращать сезон года (Summer, Autumn, Winter, Spring)
2. get_time_of_day - должен возвращать  время суток
(Morning: 6-12; Day: 12-18, Evening: 18-0, Night: 0-6) (последнее число не включено в промежуток)
import datetime. """

import datetime

class SuperDate(datetime.datetime):

    def get_season(self):
        seasons = {'Зима': (12, 1, 2), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8),'Осень': (9, 10, 11)}

        for season, period in seasons.items():
            if period.count(self.month):
                return season

    def get_time_of_day(self):
        day_time = {'Утро': range(6, 12), 'День': range(12, 18), 'Вечер': range(18, 24), 'Ночь': range(0, 6)}

        for times, period in day_time.items():
            if period.count(self.hour):
                return times


date = SuperDate(2024, 8, 20, 18, 30)
print(f'Время года: {date.get_season()}')
print(f'Время суток: {date.get_time_of_day()}')
