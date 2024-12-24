class Man:

    def __init__(self, balance:int, credit:int)-> None:
        self.balance=balance
        self.credit=credit

    def __bool__(self):
        return self.balance > 0 and self.credit > 0
    
class Device:
    def __init__(self, is_on:bool, battery_level:int)->None:
        self.is_on=is_on
        self.battery_level=battery_level

    def __bool__(self):
        return self.is_on==True and self.battery_level > 10
        