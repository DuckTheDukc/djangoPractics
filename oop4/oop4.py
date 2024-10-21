# class Singleton:
#     __insance=None

#     def __new__(cls, *args, **kwargs ):
#         if cls.__insance is None:
#             cls.__insance=super().__new__(cls)
#         return cls.__insance
# s1= Singleton()
# s2= Singleton()
    
# print(s1 is s2)
# print(s1)
# print(s2)

class fiveObj:
 lastObj=None

 count:int=0

def __new__(cls, *args, **kwargs ):
    if fiveObj.count<5:
       return super(fiveObj, cls).__new__(cls)
    else:
       return cls.lastObj

def __init__(self, *args, **kwargs):
    fiveObj.count +=1
    if fiveObj.count == 5:
       fiveObj.lastObj=self

class Book:
   allBooks:list=[]
   title:str=None
   author:str=None
   year:str=None

   def __new__(cls, *args, **kwargs ):
    for i in Book.allBooks:
       if i.title==args[0] and i.author==args[1]:
          return i
       return super(Book, cls).__new__(cls)
    
    def __init__(self, title:str, author:str, year:str):
        self.title=title
        self.author=author
        self.year=year



