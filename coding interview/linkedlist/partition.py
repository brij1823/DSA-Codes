class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def insertend(self,data):
        tempo = Node(data)
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = tempo
    def partition(self):
        l = SLinkedList()
        g = SLinkedList()
        
        temp = self.head
        while(temp):
            if(temp.data<5):
                if(l.head is None):
                    l.head = Node(temp.data)
                else:
                    l.insertend(temp.data)
            else:
                if(g.head is None):
                    g.head = Node(temp.data)
                else:
                    g.insertend(temp.data)
            temp = temp.next
        temp = l.head
        while(temp.next):
            temp = temp.next
        temp.next = g.head
        
        temp  = l.head
        while(temp):
            print(temp.data)
            temp = temp.next
            
                
s = SLinkedList()
s.head = Node(3)
s.insertend(5)
s.insertend(8)
s.insertend(5)
s.insertend(10)
s.insertend(2)
s.insertend(1)
s.partition()

#s.printlist()