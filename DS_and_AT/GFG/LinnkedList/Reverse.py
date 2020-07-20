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


head = Node(14)
head = add_node(Node(20),head)
head = add_node(Node(13),head)
head = add_node(Node(12),head)
head = add_node(Node(15),head)
head = add_node(Node(10),head)


def reverse(head):
    if not head.next:
        return head

    prev = None
    current = head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev

head = reverse(head)
current = head
while current:
    print(current.data)
    current = current.next