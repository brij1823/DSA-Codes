class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
    def printlist(self):
        temp =self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def insertend(self,data):
        temp = Node(data)
        tempo = self.head
        while(tempo.next):
            tempo = tempo.next
        tempo.next = temp
    def ispalindrome(self):
        temp = self.head
        string1 = ""
        while(temp):
            string1+=temp.data
            temp = temp.next
        if(string1 == string1[::-1]):
            print("Palindrome")
        else:
            print("Not")
s = SLinkedList()
s.head = Node("a")
s.insertend("b")
s.insertend("b")
s.insertend("a")
s.ispalindrome()