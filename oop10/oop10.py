# class Model:
#     def query(self, *args, **kwargs):
#         for key, item in kwargs.items():
#             self.__dict__[key]=item
#     def __str__(self):
#         result=[]
#         for key, item in self.__dict__.items():
#             result.append(f"{key}={item}")

#             return "Model:"+",".join(result)
        
#     def __len__(self):
#         return len(self.__dict__)
    
class ShoppingCart:
    products=[]
    def __len__(self):
        return len(self.products)
    
class Book:
    title=None
    author=None
    pages=None

    def __str__(self):
        result=[]
        for key, item in self.__dict__.items():
            result.append(f"{key}={item}")
            return "Model:"+",".join(result)
    def __repr__(self):
        result=[]
        for key, item in self.__dict__.items():
            result.append(f"{key}={item}")
            return "Model:"+",".join(result)
    def __len__(self):
        return len(self.__dict__)

    