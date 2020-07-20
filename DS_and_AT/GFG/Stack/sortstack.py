from stack import Stack

stack = Stack()
stack.push(4)
stack.push(6)
stack.push(1)
stack.push(10)
stack.push(35)

stack.print()
print(stack)
#stack.sort()
#s= stack.sortted()
s = sorted(stack)# after implementing the __iter__

print(s)


# for i in stack.items():
#     print(i)