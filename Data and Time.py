"""Задание:

Создайте класс SuperDate, наследованный от класса datetime модуля datetime, объекты которого будут дополнительно обладать следующими методами:

1. get_season - должен возвращать сезон года (Summer, Autumn, Winter, Spring)
2. get_time_of_day - должен возвращать  время суток
(Morning: 6-12; Day: 12-18, Evening: 18-0, Night: 0-6) (последнее число не включено в промежуток)
"""

import datetime


class SuperDate(datetime.datetime):

    def get_season(self):
        if self.month in [1, 2, 12]:
            return 'Winter'
        elif self.month in [3, 4, 5]:
            return 'Spring'
        elif self.month in [6, 7, 8]:
            return 'Summer'
        else:
            return 'Autumn'

    def get_time_of_day(self):
        if 6 <= self.hour < 12:
            return 'Morning'
        elif 12 <= self.hour < 18:
            return 'Day'
        elif 18 <= self.hour < 24:
            return 'Evening'
        else:
            return 'Night'


a = SuperDate(2024, 4, 7, 19)
print(a.get_season())
print(a.get_time_of_day())
