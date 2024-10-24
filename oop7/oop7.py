class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance=initial_balance
    @property
    def balance(self):
        return self._balance
        
    @balance.setter
    def balance(self, amount):
        if amount <0:
            raise ValueError("Баланс не может быть отрицательным")
        self._balance = amount
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма депозита должна быть положительной.")
        self.balance += amount

    def withdraw(self, amount):
        if amount >self.balance:
            raise ValueError("Недостаточно средств.")
        self.balance -= amount

class Product:
    