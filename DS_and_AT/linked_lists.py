
class Node():

    def __init__(self):
        self.data = None
        self.next = None

    # def set_data(self,data):
    #     self._data = data

    # def get_data(self):
    #     return self._data

    # def set_next(self, next):
    #     self._next = next

    # def get_next(self, next):
    #     return self._next

    # def has_next(self):
    #     return self._next !=None 


class LinkedList():

    def __init__(self):
        self.head = None
        # self.length = self.len()

    def len(self):
        
        current = self.head
        count = 0
        while current != None:
            # print(current)
            count +=1
            current = current.next
        
        return count

    def next(self):
        return 1

    def insert_at_begining(self,data):

        if self.len() == 0:
            self.head = data
        else:
            old_node = self.head
            self.head = data
            self.head.next = old_node

    def insert_at_end(self, data):

        current = self.head

        while current.next != None:
            current = current.next

        current.next = data

    def insert_at_position(self,pos,data):

        current = self.head
        
        if 0 < pos > self.len():
            return None

        while pos > 0:
            current = current.next
            pos -=1

        next = current.next 
        data.next = next
        current.next =data








   