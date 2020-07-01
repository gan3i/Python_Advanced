from Graph import Graph
from Node import Node
from AdjucencySetGraph import AdjucencySetGraph
from queue import Queue

adm_graph=  AdjucencySetGraph(9)
adm_graph.add_edge(0,1)
adm_graph.add_edge(0,2)
adm_graph.add_edge(2,7)
adm_graph.add_edge(1,3)
adm_graph.add_edge(3,4)
adm_graph.add_edge(4,5)
adm_graph.add_edge(4,6)
adm_graph.add_edge(6,8)
adm_graph.add_edge(8,7)


# adm_graph.display()

def BFS(g,start):
    visited = set()
    q = Queue()
    q.put(start)
    while q:
        current = q.get()
        if current in visited:
            continue
        visited.add(current)
        print(current)
        for adj in g.get_adjucent_vertices(current):
            if adj not in visited:
                q.put(adj)
                

BFS(adm_graph,0)