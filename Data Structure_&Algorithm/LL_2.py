"""
class Node:
    def __init__(self, data):     ## Constructor
        self.data = data
        self.next = None 
        
    def __str__(self):
        return 'Data: ' + str(self.data)


node = Node(37)
print(node)


print(node.data)





array= list()
"""

class Node:
    def __init__(self, data):     ## Constructor
        self.data = data
        self.next = None 
        
    def __str__(self):
        return 'Data: ' + str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        this_node = self.head
        while this_node != None:
            print(this_node.data)
            this_node = this_node.next
        
        msg = " : LL ENDED"
        return msg
    
    def insert(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next
            last_node.next = new_node

    def search(self, data):
        find_data = data
        this_node = self.head 
        flag = False
        while this_node.data != find_data:
            this_node = this_node.next
            if(flag == False):
                flag = True
        if flag == True:
            return this_node
        
        return None

    def delete(self, data):
        find_data = data
        index = 0 
        this_node = self.head
        pre_node = self.head
        flag = False
        while this_node.data != find_data:
            this_node = this_node.next
            index += 1
            if(flag == False):
                flag = True
            pre_node = this_node
            this_node = this_node.next
            
        if(index != 0):
            pre_index -=1 

        pre_node.next = this_node.next
            
LL1 = LinkedList()

LL1.insert(12)
LL1.insert(99)
LL1.insert(37)
LL1.insert(24)
LL1.insert(56)

result = LL1.search(37)
print(result)

print(LL1)  