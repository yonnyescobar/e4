class DoubleNode():
    def __init__(self, d=None):
        self.__data=d
        self.__prev=None
        self.__next=None
    
    @property
    def data(self):
        return self.__data
    
    @property
    def prev(self):
        return self.__prev
        
    @property
    def next(self):
        return self.__next
     
    @data.setter
    def data(self,d):
        self.__data=d
    
    @prev.setter
    def prev(self,n):
        self.__prev=n
        
    @next.setter
    def next(self,n):
        self.__next=n
        
    
        