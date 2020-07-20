class StackNode():
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self, root):
        self.root = None 

    def isEmpty(self):
        return self.root is None
    def push(self,value):
            new_node = StackNode(value)
            new_node.next = self.root
            self.root = new_node

    def pop(self):
        if self.root is None:
            raise ValueError("Stack is Empty")
        else:
            popped = self.root.data
            self.root = self.root.next
            return  popped

    def peek(self):
        if self.root is None:
            raise ValueError("Stack is empty")
        else:
            return self.root.data

    


        