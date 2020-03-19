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
        
    def summation(self,b):
        temp  = self.head
        tempo = b.head
        
        string1 = ""
        string2 = ""
        
        while(temp):
            string1+=str(temp.data)
            temp = temp.next
        while(tempo):
            string2+=str(tempo.data)
            tempo=tempo.next
        string1 = string1[::-1]
        string2 = string2[::-1]
        
        print(int(string1)+int(string2))
 
s = SLinkedList()
s.head = Node(1)
s.insertend(1)
s.insertend(2)

b = SLinkedList()
b.head = Node(5)
b.insertend(2)
b.insertend(1)

s.summation(b)
# 211 + 125 = 336   


    