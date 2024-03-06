from multiprocessing import process
from functools import partial
from time import sleep


class WarehouseManager:
    def __init__(self):
        self.data = {}

    def process_request(self, request):
        product, action = request

        if action == 'receipt':
            if product in self.data:
                self.data[product] += 1
            else:
                self.data[product] = 1
        elif action == 'shipment':
            if product in self.data and self.data[product] > 0:
                self.data[product] -= 1

    def run(self, requests):
        if __name__ == "__main__":
            processes = []
            manager.run(requests)
        for request in requests:
            process = Process(target=self.process_request, args=(request,))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()


requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]
manager = WarehouseManager()
print(manager.data)
