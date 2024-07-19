# Реализуйте программу, которая имитирует доступ к общему ресурсу с использованием механизма блокировки потоков.
#
# Класс BankAccount должен отражать банковский счет с балансом и методами для пополнения и снятия денег.
# Необходимо использовать механизм блокировки, чтобы избежать проблемы гонок (race conditions) при модификации
# общего ресурса.



from threading import Thread, Lock
lock = Lock()
balance = 1000
class BankAccount(Thread):

    def __init__(self):
        super().__init__()
        #self.amount = amount

    def deposit(self, amount):
        global balance
        with lock:
            balance = balance + amount
            print(f'Deposited {amount}, new balance is {balance}')
            return balance

    def withdraw(self, amount):
        global balance
        with lock:
            balance = balance - amount
            print(f'Withdrew {amount}, new balance is {balance}')


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)

def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)

account = BankAccount()

deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
