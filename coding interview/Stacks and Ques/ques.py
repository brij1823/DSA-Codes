stack1 = []
stack1.append(1)
stack1.append(2)
stack1.append(3)

stack2 = []

while(stack1):
    stack2.append(stack1.pop())
print(stack2)
stack2.pop()
print(stack2)