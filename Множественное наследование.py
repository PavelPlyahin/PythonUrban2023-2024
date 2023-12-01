class Vehicle:
    vehicle_type = "none"


class Car(Vehicle):
    price = 1000000

    def horse_powers(self):
        return 150

class Nissan(Car,Vehicle):
    price = 700000
    vehicle_type = "Nissan"

    def horse_powers(self):
        return 180
automobile1 = Nissan()

print(automobile1.vehicle_type, automobile1.price, automobile1.horse_powers())
