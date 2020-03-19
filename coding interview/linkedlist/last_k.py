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
        counter = 0
        temp = self.head
        while(temp):
            counter+=1
            temp = temp.next
        return counter
    def printkelement(self,m,n):
        tempo = n-m
        temp = self.head
        counter = 0
        while(temp):
            if(counter == tempo):
                print(temp.data)
            temp = temp.next
            counter+=1
            
s = SLinkedList()
s.head = Node(1)
s.insertend(2)
s.insertend(3)
s.insertend(4)
s.insertend(5)
s.printkelement(5,s.getlength())