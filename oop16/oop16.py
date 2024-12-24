class InfiniteRange:
    def __init__(self, start):
        self.start=start
    
    def __next__(self):
        self.start +=1
        return self.start
    
    def __iter__(self):
        return self
    
class Fibonachi:
    prev= 0
    current= 1
    index = None
    def __init__(self, index:int):
        self.index=index

    def __next__(self):
        if self.current+self.prev < self.index:
            next=self.current+self.prev
            self.prev=self.current
            self.current=next

            return self.current
        raise StopIteration
        
    def __iter__(self):
        return self
    
f = Fibonachi(12)

for i in f:
    print(i)