


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.map = dict()
    
    def size(self):
        return len(self.heap)

    def _get_parent_index(self, index):
    	return (index-1) // 2

    def _get_left_child_index(self, index):
    		return (2 * index) + 1

    def _get_right_child_index(self, index):
    		return (2 * index) + 2

    def _swap(self, a, b) -> None:
    	self.map[self.heap[b][1]] = a
    	self.map[self.heap[a][1]] = b
    	self.heap[a], self.heap[b] = self.heap[b], self.heap[a] 
    
    def _heapify_down(self, start):
        left_index = self._get_left_child_index(start)
        right_index = self._get_right_child_index(start)
        if left_index < self.size() - 1 and  self.heap[left_index][0] < self.heap[start][0]:
        	self._swap(start, left_index)
	        self._heapify_down(left_index)
        elif right_index < self.size() - 1 and  self.heap[right_index][0] < self.heap[start][0]:
            self._swap(start, right_index)
            self._heapify_down(right_index)
    
    def _heapify_up(self, index):
        parent_index = self._get_parent_index(index)
        while parent_index >= 0 and  self.heap[parent_index][0] > self.heap[index][0]:
            self._swap(parent_index, index)
            index = parent_index
            parent_index = self._get_parent_index(index)


    def insert(self, key, priority):
    	self.heap.append([priority, key])
    	index =  len(self.heap) - 1
    	self.map[key] = index
    	self._heapify_up(index)
    
    def find(self, key):
    	return key in self.map

    def get_priority(self, key):
        if self.find(key):
            return self.heap[self.map[key]][0]


    def extract_min(self):
        if self.size() ==1:
            del self.map[self.heap[0][1]]
            return self.heap.pop()[1]
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        del self.map[min_value[1]]
        self.map[self.heap[0][1]] = 0
        self._heapify_down(0)
        return min_value[1]

    def update_priority(self, key, value):
        if key in self.map:
            index = self.map[key]
            self.heap[index] = [value, key]
            parent_index = self._get_parent_index(index)
            if self.heap[parent_index][0] > self.heap[index][0]:
                self._heapify_up(index)
            else:
                self._heapify_down(index)

# pq = PriorityQueue()

# pq.insert('A',10)
# pq.insert('B',8)
# pq.insert('C',11)
# pq.insert('D',2)
# pq.insert('E',7)

# print(pq.extract_min())

# pq.update_priority('C', 1)
# print(pq.extract_min())

# print(pq.heap)