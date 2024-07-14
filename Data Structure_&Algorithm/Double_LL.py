class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return 'Data: ' + str(self.data)
    
class DoubleNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.prev = None 
    
    def __str__(self):
        return 'Data: ' + str(self.data)
    
    
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        
    def 