from collections import defaultdict
from PriorityQueue import PriorityQueue

def get_MST(connections, n):
    if n <= 1:
        return []

    graph = defaultdict(set)
    pq = PriorityQueue()
    INT_MAX = 2 ** 32 - 1
    map  = dict()
    result = []
	
    for u, v , w in connections:
	    graph[u].add((v, w))
	    graph[v].add((u, w))
	    if not pq.find(u):
	    	pq.insert(u,INT_MAX)
	    if not pq.find(v):
	    	pq.insert(v, INT_MAX)

    pq.update_priority(connections[0][0], 0)

    while pq.size() > 0:
        curr_node  = pq.extract_min()
        if curr_node in map:
            result.append(map[curr_node])
            del map[curr_node]	
		
        for nhbr in graph[curr_node]:
            node = nhbr[0]
            if pq.find(node):
                if pq.get_priority(node) > nhbr[1]:
                    pq.update_priority(node, nhbr[1])
                    map[node] = [curr_node,node]

	
    if len(result) == n-1:
        return result
    else:
        return -1

con = [['A',"B",1],['A',"D",6],['B',"E",2],['B',"D",4],['D',"E",1],['E',"F",3],['E',"C",6],['F',"C",1],['B',"C",4],]

print(len(con))

print(get_MST(con,6))

