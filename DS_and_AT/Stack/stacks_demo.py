
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

a = [286]
a_id = id(a[0])
i = 286
while True:
    print(id(a[-1]))
    i +=1
    a.append(i)
    if id(a[0])  != a_id:
        break
    if len(a) == 100:
        break

print(len(a))



