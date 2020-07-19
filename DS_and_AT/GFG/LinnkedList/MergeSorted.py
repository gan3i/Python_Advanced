#code

class Node():
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def add_node(new_node,head):
    temp = head
    head = new_node
    head.next = temp
    return head


a = Node(50)
head = add_node(Node(25),a)
head = add_node(Node(14),a)
head = add_node(Node(13),a)
head = add_node(Node(12),a)
head = add_node(Node(10),a)


b = Node(24)
head = add_node(Node(20),b)
head = add_node(Node(11),b)
head = add_node(Node(1),b)