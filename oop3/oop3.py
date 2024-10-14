# class Resource:
#     def __init__(self, name:str, resource_type:str):
#         self.name=name
#         self.resource_type=resource_type


#     def __del__(self):
#         print(f"Ресурс {self.name} типа {self.resource_type} удалён.")
        

# r1=Resource("соединение1", "подключение к базе данных")
# r2=Resource("соединение2", "подключение к базе данных")

# for _ in range(1,11):
#     print(_)
#     if _ ==5:
#         del r2

# for _ in range(1,11):
#     print(_)
#     if _ ==5:
#         del r2

class Node:
    data=None
    next=None

    def __init__(self, data:str)->None:
        self.data=data


class LinkedList:
    start: Node=None
    end: Node=None

    def append(self, object):
        new_node=Node(object)
        if self.start is None:
             self.start = new_node
             return
        
        current_node=self.start
        while(current_node.next):
            current_node=current_node.next
            current_node.next=new_node

    def len(self):
        temp=self.start
        i=0
        while(temp):
            i+=1
            temp=temp.next
            return i
    
    def search(self,data):
        temp=self.start
        while(temp):
            if data==temp.data:
                return temp
            
            temp=temp.next
    
        
    def remove(self,index:str):
        if self.start==None:
            return
        current_node = self.start
        position = 0
        if position == index:
            self.start = self.start.next
        else:
            while(current_node != None and position + 1 != index):
                position += 1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
        
    