import DoubleNode as dn

class DoubleList():
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0
    
    def size(self):
        return self.__size
    
    def isEmpty(self):
        return self.size()==0
    
    def first(self):
        return self.__head
    
    def last(self):
        return self.__tail
    
    def addFirst(self,e):
        n=dn.DoubleNode(e)
        if self.isEmpty():
            self.__head=n
            self.__tail=n
        else:
            n.next=self.__head
            self.__head.prev=n
            self.__head=n
            
        self.__size+=1
    
    def addLast(self,e):
        n=dn.DoubleNode(e)
        if self.isEmpty():
            self.__head=n
            self.__tail=n
        else: 
            self.__tail.next=n
            n.prev=self.__tail
            self.__tail=n
           
        self.__size+=1
    
    def removeFirst(self):
        if not(self.isEmpty()):
            temp_dato=self.__head.data
            if self.size()==1:
                self.__head=None
                self.__tail=None
            else:
                temp=self.__head.next 
                self.__head.next=None
                temp.prev=None
                self.__head=temp
            self.__size-=1
            return temp_dato
        else:
            return None
    
    def removeLast(self):
        if not(self.isEmpty()):
            temp_dato=self.__tail.data
            if self.size()==1:
                self.__head=None
                self.__tail=None
            else:
                temp=self.__tail.prev 
                self.__tail.prev=None
                temp.next=None
                self.__tail=temp
            self.__size-=1
            return temp_dato
        else:
            return None
        
    def remove(self,n):
        if n==self.__head:
            self.removeFirst()
        elif n==self.__tail:
            self.removeLast()
        else:
            temp_dato=n.data
            temp_prev=n.prev
            temp_next=n.next
            temp_prev.next=temp_next
            temp_next.prev=temp_prev
            n.next=None
            n.prev=None
            self.__size-=1
            return temp_dato
            
    def addAfter(self,n,e):
        if n == self.__tail:
            self.addLast(e)
        else:
            m=dn.DoubleNode(e)
            temp=n.next
            n.next=m
            m.prev=n
            m.next=temp
            temp.prev=m
            self.__size+=1
    
    def addBefore(self,n,e):
        if n==self.__head:
            self.addFirst(e)
        else:
            m=dn.DoubleNode(e)
            temp=n.prev
            temp.next=m
            m.prev=temp
            m.next=n
            n.prev=m
            self.__size+=1
    
    def print(self):
        if self.isEmpty():
            print("")
        else:
            temp=self.__head 
            while temp!=None:
                print(temp.data)
                temp=temp.next
            
            
            
                