import heapq

a = [7,2,1,4,5]

heapq.heapify(a) #O(n)
heapq.heappush(a, 8) #O(log(n))
print(heapq.heappop(a)) #O(log(n))
print(a[0]) # peeking the min element
print(heapq.nsmallest(2, a)) #O(nlog(k)
print(heapq.nlargest(2, a)) #O(nlog(k)


