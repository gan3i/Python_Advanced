
import heapq
class Val:
    def __init__(self,x:int) -> None:
        self.x = x
    def __lt__(self,other):
        return self.x > other.x

b = [Val(2),Val(4),Val(1)]
print([val.x for val in b])
heapq.heapify(b)
print([val.x for val in b])

heapq.heappush(b,Val(7))
heapq.heappop(b)
print(b[0].x)
print(heapq.nsmallest(2, b)) #O(nlog(k)
print(heapq.nlargest(2, b)) #O(nlog(k)
