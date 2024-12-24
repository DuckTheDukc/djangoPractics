from io import TextIOWrapper
class List:
    def __init__(self, *data:list[any]):
        self.__data=List(data)
    
    def __getitem__(self,index):
        if index > len(self.__data):
            return self.__data[-1]
        return self.__data[index]
    
    def __setitem__(self,index,value):
        if index > len(self.__data):
            self.__data[-1]=value
            return self.__data
        self.__data[index]=value
        return self.__data
    
    def __delitem__(self,index):
        if index > len(self.__data):
            del self.__data[-1]
        del self.__data[index]

class KeyValueStore:

    filename_path: str = "folder/log.txt"
    file: TextIOWrapper = None 
    __data: dict[any] = {}
    def __init__(self, *data:dict, filename_path="folder/log.txt"):
        self.filename_path=filename_path
        self.__data=dict(data)
        self.file = open(self.filename_path, 'w')

    def __del__(self):
        self.file.close()

    def __getitem__(self,index):
        return self.__data[index]
    
    def __setitem__(self,index,value):
        self.__data[index]=value
        self.file.write(self.__data)
        return self.__data

    def __delitem__(self,index):
        del self.__data[index]
        self.file.write(self.__data)