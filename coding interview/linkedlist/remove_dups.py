class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
    
    def insertend(self,data):
        temp = Node(data)
        if(self.head is None):
            self.head = temp
        else:
            tempo = self.head
            while(tempo.next):
                tempo = tempo.next
            tempo.next = temp
    
    def printlist(self):
        temp = self.head
        
        while(temp):
            print(temp.data)
            temp = temp.next
    
    def removeduplicates(self):
        temp = self.head
        hashmap = {}
        while(temp):
            try:
                tempo = temp.next
                hashmap[tempo.data] = hashmap[tempo.data]+1
                temp.next = temp.next.next
            except:                
                hashmap[tempo.data] = 1
            temp = temp.next

        

s = SLinkedList()
s.head = Node(1)
s.insertend(2)
s.insertend(2)
s.insertend(3)
s.insertend(2)
s.insertend(5)
s.insertend(2)
s.removeduplicates()
s.printlist()
    