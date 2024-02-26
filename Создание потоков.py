# Задание:
# Напишите программу, которая создает два потока.
# Первый поток должен выводить числа от 1 до 10 с интервалом в 1 секунду.
# Второй поток должен выводить буквы от 'a' до 'j' с тем же интервалом.
# Оба потока должны работать параллельно.
import time
from datetime import datetime
from threading import Thread


def out_num_by_sec():
    # вывод чисел с интревалом 1 сек и выводим время операции
    start_time = datetime.now()
    for i in range(1, 11):
        print(i, end=' ', flush=True)
        time.sleep(0.5)
    end_time = datetime.now()
    print(f'\n\nTime num per second: {end_time-start_time}', flush=True)


def out_chair_by_sec():
    # вывод букв  с интревалом  1 сек и выводим время операции
    start_time = datetime.now()
    for i in range(ord('a'), ord('j') + 1):
        char = chr(i)
        print(char, end=' ', flush=True)
        time.sleep(0.5)
    end_time = datetime.now()
    print(f'\n\nTime char per second: {end_time-start_time}', flush=True)


t1 = Thread(target=out_num_by_sec)
t2 = Thread(target=out_chair_by_sec)

t1.start()
t2.start()
t1.join()
t2.join()