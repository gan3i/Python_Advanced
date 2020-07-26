from queue import Queue  
stack = [10,8,5,4]

def insertAtBottom(stack, item):
    if len(stack)==0:
        stack.append(item)
    else:
        top  = stack.pop()
        insertAtBottom(stack,item)
        stack.append(top)



def reverse(stack):

    if len(stack) !=0:
        top = stack.pop()
        reverse(stack)
        insertAtBottom(stack, top)
    return stack

def reverse1(stack):
    q=Queue() 
    while len(stack) !=0:
        q.put(stack.pop())
    while not q.empty():
        stack.append(q.get())
    
    return stack
    




print(reverse1(stack))
