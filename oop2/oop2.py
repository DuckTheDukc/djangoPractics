from io import TextIOWrapper
import re


class UserSchem: pass
class DataBase:
    data: list=[]
    def get_data(self, url: str):
        with open(url, 'r', encoding='UTF-8') as f:
            result = f.readlines()
            self.serializers(result)
            f.close()
            return result
    def serializers(self, data:TextIOWrapper):
        content=[]
        for i in data:
            schema=dict()
            line = [i for i in re.split(r'\s',i) if i !='']
            for index in range(0,len(line)-1,2):
                schema[line[index]]=line[index+1]
            content.append(schema)
        return content



    def create(self, data):
        for i in data:
            user=UserSchem()
            for key,item in i.items():
                setattr(user, key, item)
            self.data.append(user)

    def search(self, search):
        for user in self.users_data:
            for _, value in user.__dier__.items():
                if search in str(value):
                    return user
                
class Translator:
    dictionary: dict={}                
    def add(self, eng:str, rus:str):
        if self.dictionary.get(eng) is not None:
            if type(self.dictionary.get(eng)) is list:
                self.dictionary[eng].append(rus)
            else:
                temp = self.dictionary[eng]
                self.dictionary[eng]=[temp, rus]
        else:
            self.dictionary[eng]=rus

    def remove(self, eng: str):
        if self.dictionary.get(eng) is not None:
            del self.dictionary[eng]
    
    def translate(self, eng:str):
        return self.dictionary.get(eng)

dat = DataBase()
trans=Translator()
text = dat.get_data('data.txt')
text = dat.serializers(text)
print(dat.create(text))
print(dat.data[1].__dict__)
print(trans.add('car', 'машина'))
print(trans.translate('car'))


