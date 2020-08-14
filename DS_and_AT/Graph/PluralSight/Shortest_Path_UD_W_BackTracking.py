

from queue import Queue
from AdjucencySetGraph import AdjucencySetGraph


def build_distance_table(graph, start):
    distance_table = {x:(None, None) for x in range(graph.numVertices)}
    distance_table[start] = (0,start)

    q = Queue()
    q.put(start)
    while not q.empty():
        current = q.get()
        current_distance = distance_table[current][0]
        for adj in graph.get_adjucent_vertices(current):
            if distance_table[adj][1] == None:
                distance = current_distance + 1
                distance_table[adj] = (distance, current)
                q.put(adj)
            else :
                continue
    
    return distance_table


def shortest_path(graph, start, end):
    distance_table = build_distance_table(graph,start)
    previous = distance_table[end][1]
    path = [end]

    while previous != None and previous != start:
        path = [previous] + path
        previous = distance_table[previous][1]
    if not previous or  previous !=start:
        return "there is no path"
    return [start] + path

graph = AdjucencySetGraph(8,True)

graph.add_edge(0,1)
graph.add_edge(0,7)
graph.add_edge(7,2)
graph.add_edge(0,2)
# graph.add_edge(1,5)
graph.add_edge(1,4)
graph.add_edge(2,3)
graph.add_edge(2,1)
graph.add_edge(4,5)
graph.add_edge(3,4)
graph.add_edge(5,6)

path = shortest_path(graph,7,6)
print(path)







