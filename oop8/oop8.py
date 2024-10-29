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

def __init__(self,name:str,weight:float,price:float)
        