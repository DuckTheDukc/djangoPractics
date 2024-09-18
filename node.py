class Node:
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        



class LinkedList:
    start = None
    end = None
    
    def append(self, val):
        node = Node(val=val)
        
        if not self.start:

            self.start = node
            return
        last = self.start
      
        while last.next:
            print(last.val)
            last = last.next
    
        last.next, self.end = node,node 
    
    def n(self):
        self.start=self.start.next
        last=self.start
        n=0
        while  last:
            n+=1
            last = last.next
        print("число",n)
        return n

    def found(self,n):
        count=0
        a = self.start
        while a:
            count+=1
            if a.val==n:
                print(a.val,count)
                return a,count
            a=a.next
        
node = LinkedList()

node.append('1')
node.append('2')
node.append('3')
node.append('4')
node.append('5')
node.found('4')