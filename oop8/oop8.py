from typing import Any


class Shop:
    
    def __init__(self):
        self.goods=[]
    def add_product(self,product):
        self.goods.append(product)
    def remove_product(self, product):
        for index in range(len(self.goods)):
            if self.goods[index] == product:
                self.goods.pop(index)
                return

class Product:
    __id=0
    def __new__(cls, *args, **kwargs):
        cls.__id+=1
        obj = super().__new__(cls)
        obj.id=cls.__id
        return obj

def __init__(self,name:str,weight:float,price:float):
    self.name=name
    self.weight=weight
    self.price=price
    
def __setattr__(self,  name:str, value)->None:
    type_dict={
        "id":int,
        "name":str,
        "weight":(int,float),
        "price":(int,float),
    }
        
    if not isinstance(value, type_dict[name]):
        raise TypeError("Неверный тип присваиваемых данных")
    
    if name=='weight' and not value>0:
        raise TypeError("Неверный тип присваиваемых данных")
    if name=='price' and not value>0:
        raise TypeError("Неверный тип присваиваемых данных")
    super().__setattr__(name,value)
    
    def __delattr__(self, name:str)->None:
        if name == 'id':
            raise AttributeError("Атрибут id удалять запрещено")
    super().__delattr__(name)
    
class Library:
    
    name:str=None
    books:list[str]=[]
    max_books:int=None
    
    def __init__(self,name:str,max_books:int):
        self.name=name
        self.max_books=max_books
        
    def add_book(self,book):
        if self.max_books>len(self.books):
            self.books.append(book)
            
    def remove_book(self, book):
        self.books.remove(book)
        
    def list_books(self):
        return self.books
    
    
    
    def __setattr__(self, name, value):
        if name=="max_books" and self.max_books is not None:
           raise AttributeError("Нельзя изменить max_books после инициализации")
        if name == 'books' and len(self.books) > self.max_books:
            raise AttributeError("количество книг превышает максимум")
        
    def __getattribute__(self, name):
        print(name)
        super().__getattribute__(name)
        
    def __getattr__(self, name):
        print("Запрашиваемый атрибут не найден")
        
    def __delattr__(self,name):
        if name =='name':
            raise AttributeError("нельзя удалить атрибут name")
        print(f'Атрибут {name} удалён')
        super().__delattr__(name)
        
            
            