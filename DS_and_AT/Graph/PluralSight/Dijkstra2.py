from heapq import heappush, heappop
from collections import defaultdict


def build_distance_table(connections, source):
    graph = defaultdict(set)
    for u, v, w in connections:
        graph[u].add((v,w))
        graph[v].add((u,w))

    dist_table = {x: [None, None] for x in graph}
    dist_table[source] = [0, source]
    heap = [[0, source]]

    while heap:
        _ , curr_node = heappop(heap)
        curr_dist = dist_table[curr_node][0]

        for nhbr, w in graph[curr_node]:
            new_dist = curr_dist + w
            old_dist  = dist_table[nhbr][0]
            if old_dist is None  or old_dist > new_dist: # you missed this None COndition.
                dist_table[nhbr] = [new_dist, curr_node]
                heappush(heap, [new_dist, nhbr])

    return dist_table



def shortest_path(connections, source, end):
    distance_table = build_distance_table(connections, source)
    result = []
    if end not in distance_table:
        return result
    result.append(end)	

    while distance_table[end][1] != end:
	    end  = distance_table[end][1]
	    result.append(end)

    return result[-1::-1]

con = [['A',"B",1],['A',"D",6],['B',"E",2],['B',"D",4],['D',"E",1],['E',"F",3],['E',"C",6],['F',"C",1],['B',"C",4], ['k',"L",4]]


print(shortest_path(con,'A',"K"))
