
class MinHeap():
    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def newMinHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode

    def swapMinHeapNode(self, a, b):
        temp = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = temp

    def minHeapfy(self, index):
        smallest = index
        left = 2*index +1
        right = 2* index +2

        if left < self.size and self.array[left][1] < self.array[smallest][1]:
            smallest = left

        if right <self.size and self.array[right][1] < self.array[smallest][1]:
            smallest = right

        if smallest != index:

            #swap pos
            self.pos[self.array[smallest][0]] = index
            self.pos[self.array[index][0]] = smallest

            #Swap nodes
            self.swapMinHeapNode(smallest, index)

            self.minHeapfy(smallest)
            

    def extractMin(self):
        
        if self.isEmpty():
            return

        root = self.array[0]

        lastnode = self.array[-1]
        self.array[0] = lastnode

        self.pos[lastnode[0]] = 0
        self.pos[root[0]] = self.size-1

        self.size -= 1
        self.minHeapfy(0)

    def isEmpty(self):
        return self.size == 0

    def decreaseKey(self,v, dist):

        index = self.pos[v]

        self.array[index][1] = dist

        while index >0 and self.array[index][1] < self.array[(index-1)/2][1]:

            self.pos[self.array[index][0]] = (index-1)/2
            self.pos[self.array[(index-1)/2][0]] = index
            self.swapMinHeapNode(index, (index-1)/2)

            index = (index-1) / 2

    def isInMinHeap(self, v):

        if self.pos[v] < self.size:
            return True
        else:
            return False





