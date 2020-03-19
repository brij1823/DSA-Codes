class Solution:
    def __init__(self,stack=None):
        self.stack = stack
        self.minimum = 999
    def push(self,data):
        self.stack.append(data)
        if(self.minimum == -1):
            self.minimum = data
        else:
            if(data<self.minimum):
                self.minimum = data
    def get_minimum(self):
        return self.minimum
    def pop(self):
        self.stack.pop()
    
stack = []
s = Solution(stack)
s.push(100)
s.push(10)
s.push(3)
s.push(13)
s.push(32)
s.push(34)
s.push(23)
s.push(31)
print(s.get_minimum())