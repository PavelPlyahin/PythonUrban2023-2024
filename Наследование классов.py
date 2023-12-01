class Car:
    price = 1000000

    def __init__(self,name):
        self.name = name

    def horse_powers(self):
        return 100
class Nissan(Car):
    price = 800000

    def __init__(self):
        self.name = Nissan

    def horse_powers(self):
        return 150

class Kia(Car):
    price = 700000

    def __init__(self):
        self.name = Kia
    def horse_powers(self):
        return 180




