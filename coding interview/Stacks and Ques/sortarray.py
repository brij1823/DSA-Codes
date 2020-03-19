stack = []

stack.append(8)
stack.append(3)
stack.append(1)
stack.append(2)
stack.append(5)

answer = []
length = len(stack)
for i in range(length):
    temp = stack.pop()
    
    if(len(answer) == 0):
        answer.append(temp)
    else:
        if(temp <= answer[-1]):
            answer.append(temp)
            continue
        else:
            stack2 = []
            try:
                while(answer[-1]<temp):
                    stack2.append(answer.pop())
                answer.append(temp)
            except:
                answer.append(temp)
            
            while(len(stack2)!=0):
                answer.append(stack2.pop())
print(answer)
                
           