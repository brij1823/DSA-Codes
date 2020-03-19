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
    def getlength(self):
        temp = self.head
        counter = 0
        while(temp):
            counter+=1
            temp = temp.next
        return counter
    def removemiddle(self,n):
        temp = self.head
        counter = 0
        n = n//2-1 
        while(temp):
            if(counter == n):
                temp.next = temp.next.next
            counter+=1
            temp = temp.next
            
        
    
s = SLinkedList()
s.head = Node(1)
s.insertend(2)
s.insertend(3)
s.insertend(4)
s.insertend(5)
s.insertend(6)
s.removemiddle(s.getlength())
s.printlist()

    