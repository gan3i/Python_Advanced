from Graph import Graph
from Node import Node
from AdjucencySetGraph import AdjucencySetGraph
from queue import Queue

adm_graph=  AdjucencySetGraph(10)
adm_graph.add_edge(0,1)
adm_graph.add_edge(0,2)
adm_graph.add_edge(2,7)
adm_graph.add_edge(1,3)
adm_graph.add_edge(3,4)
adm_graph.add_edge(4,5)
adm_graph.add_edge(4,6)
adm_graph.add_edge(6,8)
adm_graph.add_edge(8,7)
adm_graph.add_edge(2,9)

def DFS_recu(g,visited,current=0):
    if current in visited:
        return

    visited.add(current)
    print(current)
    for adj in g.get_adjucent_vertices(current):
        DFS_recu(g,visited,adj)

def DFS(g,start):
    stack = [start] # collections.deque
    #deque.append(start)
    visited = set()
    while stack:
        current = stack.pop()#deque.pop
        if current in visited:
            return

        visited.add(current)
        print(current)
        for adj in g.get_adjucent_vertices(current):
            if adj not in visited:
                stack.append(adj)#deque.append(adj)

DFS(adm_graph,0)

