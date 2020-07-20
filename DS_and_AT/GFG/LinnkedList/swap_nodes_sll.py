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

def swap(head, x, y):
    
    if head.data == x:
        return swap_head(head,y)
    elif head.data == y:
        return swap_head(head,y)

    xnode,pre_xnode = get_nodes(head,x)
    ynode,pre_ynode = get_nodes(head,y)
    if xnode and ynode:
        if xnode.next ==ynode :
            swap_adjucent( xnode,pre_xnode,ynode )
        elif ynode.next == xnode :
            swap_adjucent( ynode,pre_ynode,xnode )
        else :
            temp = xnode.next
            pre_xnode.next = ynode
            xnode.next = ynode.next
            pre_ynode.next = xnode
            ynode.next= temp


    return head       



def swap_adjucent( node,pre_node,next_node):
    node.next= next_node.next
    pre_node.next = next_node
    next_node.next = node

def swap_head(head,val):
    node,pre_node = get_nodes(head,val)
    if node:   
        temp = head.next
        head.next = node.next
        pre_node.next = head
        node.next = temp
        head = node
    return head

def get_nodes(head, val):
    pre_node = head
    node = head.next
    while node and node.data!=val:
        pre_node = node
        node = node.next

    return node, pre_node

head = swap(head,10,14)
current = head
while current:
    print(current.data)
    current = current.next