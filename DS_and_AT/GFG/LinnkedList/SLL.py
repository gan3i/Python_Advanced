
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None


class SLL():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        self.length +=1

    def insert_at_begining(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail =self.head
        else:
            new_head = Node(val)
            new_head.next  = self.head
            self.head = new_head
        self.length +=1
#TODO insert after a node
#TODO insert after a value
#TODO insert at Position
#TODO insert afrer a Position
#TODO delete at begining 
#TODO delete at end 
#TODO delete after a node
# TODO delete after a value 
# TODO delete after a position
# TODO delete at  position

def findMid_m1(head):
    if head is None:
        return -1
    count = 0
    current = head
    while current is not None:
        count +=1
        current = current.next
    mid = head
    midc = (count//2)
    for _ in range(midc):
        mid = mid.next
    return mid.data

def findMid_m2(head):
    if head is None:
        return -1
    ptr1 = head
    ptr2 = head
    while ptr2.next is  not None:
        ptr1 = ptr1.next
        ptr2 = ptr1.next.next

    return ptr1.data

def findMid_m3(head):
    if head is None:
        return -1
    count = 0
    mid = head
    while head is not None:
        if count%2:
            mid= mid.next
        count +=1
        head = head.next

    return mid.data

def binarysearch(head, value):
    pass





