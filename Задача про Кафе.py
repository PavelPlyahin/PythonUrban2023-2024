# Задание:
# Моделирование работы сети кафе с несколькими столиками и потоком посетителей, прибывающих для заказа пищи и уходящих
# после завершения приема.
#
# Есть сеть кафе с несколькими столиками. Посетители приходят, заказывают еду, занимают столик,
# употребляют еду и уходят. Если столик свободен, новый посетитель принимается к обслуживанию,
# иначе он становится в очередь на ожидание.
#
# Создайте 3 класса:
# Table - класс для столов, который будет содержать следующие атрибуты: number(int) - номер стола, is_busy(bool) -
# занят стол или нет.
#
# Cafe - класс для симуляции процессов в кафе. Должен содержать следующие атрибуты и методы:
# Атрибуты queue - очередь посетителей (создаётся внутри init), tables список столов (поступает из вне).
# Метод customer_arrival(self) - моделирует приход посетителя(каждую секунду).
# Метод serve_customer(self, customer) - моделирует обслуживание посетителя. Проверяет наличие свободных столов,
# в случае наличия стола - начинает обслуживание посетителя (запуск потока), в противном случае -
# посетитель поступает в очередь. Время обслуживания 5 секунд.
# Customer - класс (поток) посетителя. Запускается, если есть свободные столы.
#
# Так же должны выводиться текстовые сообщения соответствующие событиям:
# Посетитель номер <номер посетителя> прибыл.
# Посетитель номер <номер посетителя> сел за стол <номер стола>. (начало обслуживания)
# Посетитель номер <номер посетителя> покушал и ушёл. (конец обслуживания)
# Посетитель номер <номер посетителя> ожидает свободный стол. (помещение в очередь)

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


