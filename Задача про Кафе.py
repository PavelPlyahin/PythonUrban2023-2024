from time import sleep
from threading import Thread
import threading
import queue


class Table:

    def __init__(self, id):
        self.id = id
        self.is_busy = False


class Cafe:

    def __init__(self, queue, tables):
        self.queue = queue
        self.tables = tables

    def customer_arrival(self):

        for customer_num in range(1, 21):
            print(f'посетитель номер {customer_num} прибыл')
            self.serve_customer(customer_num)
            sleep(2)

    def serve_customer(self, customer_num):

        flag = False
        for table in self.tables:
            if not table.is_busy:
                some_customer = Customer(customer_num, self, table)
                table.is_busy = True
                some_customer.start()
                flag = True
                break
        if not flag:
            self.queue.put(customer_num)
            print(f'посетитель  {customer_num} ожидает свободный стол')


class Customer(Thread):

    def __init__(self, id, cafe, table, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id
        self.cafe = cafe
        self.table = table

    def run(self):
        self.table.is_busy = True
        print(f'посетитель номер {self.id} сед за стол {self.table.id}. (Начало обслуживания)')
        sleep(5)
        print(f'Посетитель номер {self.id}  покушал и ушел. (Конец обслуживания)')
        self.table.is_busy = False
        if self.cafe.queue.qsize() > 0:
            self.cafe.serve_customer(self.cafe.queue.get())


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)

tables = [table1, table2, table3]
queue = queue.Queue()
queue.qsize()
cafe = Cafe(queue, tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
customer_arrival_thread.join()