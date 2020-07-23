#Implemented eith array

class Stack():
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)
    
    def push(self,value):
        self.data.append(value)
    
    def pop(self):
        return self.data.pop()
    @property
    def peek(self):
        if len(self.data) == 0:
            raise ValueError("stack is empty")
        return self.data[-1]
    @property
    def empty(self):
        return len(self.data)==0

    def print(self):
        print(self.data)

    def sort(self):
        if not self.empty:
            top = self.data.pop()
            self.sort()
            self._sortedInsert(top)

    def _sortedInsert(self, item):
        if self.empty or self.peek < item:
            self.push(item)
        else:
            top = self.pop()
            self._sortedInsert(item)
            self.push(top)
    def _sortedInsert1(self,stack, item):
        if stack.empty or stack.peek < item:
            stack.push(item)
        else:
            top = stack.pop()
            self._sortedInsert1(stack,item)
            stack.push(top)

    def sorted(self):
        stack = Stack()
        for i in self.data:
            self._sortedInsert1(stack,i)
        return stack
        
    def items(self):
        for i in self.data:
            yield i
    def __iter__(self):
        for i in self.data:
            yield i
# stack = Stack()


# s = stack.peek()


# print(s)
