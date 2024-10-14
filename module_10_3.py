import threading
import time
import random
from threading import Thread, Lock


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        count_iter = 0
        while count_iter <= 99: 
            bk = random.randint(50, 500)
            self.lock.acquire()
            try:
                self.balance += bk  
                print(f'Пополнение: {bk}. Баланс: {self.balance}\n')
            finally:
                self.lock.release()
            time.sleep(0.01) 
            count_iter += 1  

    def take(self):
        count_iter = 0
        while count_iter <= 99:
            bk = random.randint(50, 500)
            print(f'Запрос на {bk}')
            self.lock.acquire()
            try:
                if bk <= self.balance: 
                    self.balance -= bk
                    print(f'Снятие: {bk}. Баланс: {self.balance}\n')
                else:
                    print('Запрос отклонён, недостаточно средств')
            finally:
                self.lock.release()
            time.sleep(0.01)
            count_iter += 1


bk = Bank() # создаем объект класса

th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()  
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
