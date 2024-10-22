from string import ascii_lowercase, digits
import re
class CardCheck:
    CHARS_FOR_NAME=ascii_lowercase.upper() + digits
    
    @staticmethod
    def check_card_number(number):
        pattern=r'^\d{4}-\d{4}-\d{4}-\d{4}$'
        return bool(re.match(pattern,number))
    
    @classmethod
    def check_name(cls,name):
        words=name.split()
        if len(words)!=2:
            return False
        
        first_name,last_name=words
        return all(char in cls.CHARS_FOR_NAME for char in first_name)and \
            all(char in cls.CHARS_FOR_NAME for char in last_name)

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheint(cels):
        far= cels *(9/5) +32
        return far
    
    @classmethod
    def from_kelvin(cls,kelv):
        cels=kelv-273,15
        return super(TemperatureConverter, cls).__new__(cls)
    
class Employee:
    name=None
    age=None
    profession=None
    @staticmethod
    def is_valid_age(age):
        return age > 18 and age < 65
    
    @classmethod
    def from_string(cls, data):
        arr=data.split(',')
        if Employee.is_valid_age(int(arr[1])):
            cls.name=arr[0]
            cls.age=arr[1]
            cls.profession=arr[2] 
            return super().__new__(cls)
        else:
            raise ValueError("Возраст не совпадает")
    def get_details(self):
        return f"Имя:"(self.name),"Возраст:"(self.age),"Должность:"(self.profession)
        
        