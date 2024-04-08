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
