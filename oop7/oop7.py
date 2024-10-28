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
    def __init__(self, name, price, discount):
        self._name=name
        self._price=price
        self._discount=discount
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def set_price(self, amount):
        if amount >= 0:
            self._price=amount
        else:
            ValueError("Цена не может быть отрицательной")
    
    @property
    def discount(self):
        return self.discount
    
    @discount.setter
    def discount(self,amount):
        if 0<=amount<=100:
            self._discount=amount
        else:
            ValueError("Скидка не может быть менше нуля и больше ста")

    @property
    def price_with_discount(self, price, discount):
        true_price=price*discount/100
        return true_price

class Emloyee:
    def __init__(self, name, salary, age):
        self._name=name
        self._salary=salary
        self._age=age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def set_name(self,name):
        self._name=name

    @property
    def salary(self):
        return self.salary

    @salary.setter
    def set_salary(self, amount):
        if amount>=30000:
            self._salary=amount
        else:
            ValueError("Зарплата не может быть меньше 30000")

    def apply_raise(self,count):
        self.salary=int(self.salary*count)
    
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def set_age(self,age):
        self._age=age

    @age.deleter
    def delete_age(self):
        self._age=None



        

        
    