

class Deque():
    def __init__(self,size):
        self.size = size
        self.rear = self.front = -1
        self._data = [None]*size

    def __len__(self):
        return self.size
    @property
    def isFull(self):
        if (self.size + self.rear -1)%self.size == self.front:
            return True
        else:
            False
    @property
    def isEmpty(self):
        return self.rear == -1 or self.front == -1
    def insertAtFront(self,value):
        if self.front ==-1 and self.rear ==-1:
            self.front = 0
            self.rear = 0
            self._data[self.front] = value
        else:
            if self.isFull:
                raise ValueError("Deque is full")
            else:
                self.front = (self.front + 1)% self.size
                self._data[self.front] = value
    
    def insertAtRear(self,value):
        if self.rear == -1 and self.front == -1:
            self.rear = 0
            self.front = 0
            self._data[self.rear] = value 
        else :
            if self.isFull:
                raise ValueError("Deque is full")
            else:
                self.rear = (self.size + self.rear - 1) % self.size
                self._data[self.rear] = value 
    
    def deleteAtFront(self):
        if self.isEmpty:
            raise ValueError("Deck is Empty")
        else:
            if self.rear == self.front:
                value = self._data[self.front]
                self.rear = -1
                self.front = -1
                return value
            else:
                value = self._data[self.front]
                self.front = (self.size + self.front-1) % self.size
                return value
    def deleteAtRear(self):
        if self.isEmpty:
            raise ValueError("Deck is Empty")
        else:
            if self.rear == self.front:
                value = self._data[self.front]
                self.rear = -1
                self.front = -1
                return value
            else:
                value = self._data[self.rear]
                self.rear = (self.size + self.rear+1) % self.size
                return value

    def getFront(self):
        if self.front == -1:
            raise ValueError("Deck underflow")
        else:
            return self._data[self.front]
    def getRear(self):
        if self.rear == -1:
            raise ValueError("Deck underflow")
        else:
            return self._data[self.rear]
