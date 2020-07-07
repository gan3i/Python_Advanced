from AdjucencySetGraph import AdjucencySetGraph
from queue import Queue


graph = AdjucencySetGraph(7,False)

graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,5)
graph.add_edge(1,4)
graph.add_edge(2,3)
graph.add_edge(4,5)
graph.add_edge(3,4)
graph.add_edge(5,6)

graph.display()

def shortest_path(graph, start,end):
    q = Queue()
    visited = set()
    q.put([start])
    while not q.empty():
        current_path = q.get()
        current_node = current_path[-1]
        for adj in graph.get_adjucent_vertices(current_node):
            if adj in visited:
                continue
            visited.add(adj)
            next_path = current_path + [adj]
            q.put(next_path)
            if adj == end:
                return next_path

print(shortest_path(graph, 4, 6))






