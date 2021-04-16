
stack1 = list()
stack1.append(0)    
stack1.pop() 
stack1[-1]

from collections import deque

stack2 = deque()
stack2.append(0)
stack2.pop()
stack2.appendleft(1)
stack2.popleft()
print(stack2.count(0))

from queue import LifoQueue

stack3 = LifoQueue()
stack3.put(13)
stack3.get()



