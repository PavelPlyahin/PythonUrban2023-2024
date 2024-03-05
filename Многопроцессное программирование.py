import multiprocessing as mp
from functools import partial
from time import sleep

class WarehouseManager():
    manager = WarehouseManager
    def __init__(self):
        self.data = {key: 0 for key in ['product1', 'product2', 'product3']}


    def add_to_data(self, data, product, quantity):
        if product not in data:
            data[product] = quantity
        else:
            data[product] += quantity

    def remove_from_data(self, data, product, quantity):
        new_quantity = data.get(product, 0) - quantity
        if new_quantity < 0:
            raise ValueError("Negative quantity not allowed.")
        if new_quantity > 0:
            data[product] = new_quantity
        elif product in data:
            del data[product]

    def process_receipt(self, product, quantity):
        self.add_to_data(self.data, product, quantity)
        return f"Received {quantity} units of {product}"

    def process_shipment(self, product, quantity):
        self.remove_from_data(self.product, quantity)

requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]

# Запускаем обработку запросов
manager.run(requests)

# Выводим обновленные данные о складских запасах
print(manager.data)