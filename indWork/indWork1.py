class Node:
    data: int=None
    node_one=None
    node_two=None

def __init__(self, data:int, node_one, node_two):
    self.data=data
    self.node_one=node_one
    self.node_two=node_two

def search(self, query:int):
    if query < self.data:
        if self.node_one is None:
            return None
        return self.node_one.search(query)
    elif query > self.data:
        if self.node_two is None:
            return None
        return self.node_two.search(query)
    else:
        return self
    
def insert(self, data:int):
    if self.data:
        if data < self.data:
            if self.node_one is None:
                self.node_one = Node(data)
            else: self.node_one.insert(data)
        elif data > self.data:
            if self.node_two is None:
                self.node_two = Node(data)
            else:
                self.node_two.insert(data)

class BinaryTree:
    root: Node=None

    def search (self, query:int):
        if self.root is None:
            return None
        
        if self.root.data==query:
            return self.root
        return self.root.search(query)

    def delete(self, query:int):
        element = self.search(query)
        if element is not None:
            element.data = None
            element.node_one = None
            element.node_two=None

    def insert(self, data:int):
        if self.root is None:
            self.root = Node(data)
            