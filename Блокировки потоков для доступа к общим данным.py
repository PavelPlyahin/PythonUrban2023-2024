# Практически применить знания о механизмах блокировки потоков в Python, используя класс Lock из модуля threading.
#
# Задание:
# Реализуйте программу, которая имитирует доступ к общему ресурсу с использованием механизма блокировки потоков.
#
# Класс BankAccount должен отражать банковский счет с балансом и методами для пополнения и снятия денег.
# Необходимо использовать механизм блокировки, чтобы избежать проблемы гонок (race conditions) при модификации
# общего ресурса.

from time import sleep
import threading

locker = threading.Lock()


class BankAccount:

    def __init__(self):
        self.balance = 100

    def cash_in(self, amount):
        with locker:
            self.balance += amount
            print(f'Deposited {amount}, new balance is {self.balance}')
            sleep(0.5)

    def cash_out(self, amount):
        with locker:
            if self.balance >= amount:
                self.balance -= amount
                print(f'Withdrew {amount},  new balance is  {self.balance}')
                sleep(0.5)
            else:
                print(f'Low balance, please bill recharge ')


def deposit_thread(account, amount):
    for _ in range(3):
        account.cash_in(amount)


def withdraw_thread(account, amount):
    for _ in range(3):
        account.cash_out(amount)


account = BankAccount()

th_deposit = threading.Thread(target=deposit_thread, args=(account, 20))
th_withdraw = threading.Thread(target=withdraw_thread, args=(account, 80))

th_deposit.start()
th_withdraw.start()

th_deposit.join()
th_withdraw.join()
