from AdjucencySetGraph import AdjucencySetGraph
from queue import Queue

ads_graph =  AdjucencySetGraph(10,True)
ads_graph.add_edge(0,2)
ads_graph.add_edge(9,2)
ads_graph.add_edge(2,3)
ads_graph.add_edge(2,7)
ads_graph.add_edge(3,1)
ads_graph.add_edge(3,4)
ads_graph.add_edge(7,8)
ads_graph.add_edge(6,8)
ads_graph.add_edge(6,4)
ads_graph.add_edge(4,5)
ads_graph.add_edge(7,4)

# ads_graph.display()

def topological_sort(g):
    q = Queue()
    indegree_map= {}
    for vertex in g.vertices:
        indegree =  g.get_indegree(vertex.vertexId)
        indegree_map[vertex.vertexId] =indegree
        if indegree == 0:
            q.put(vertex.vertexId)
    sortedlist= []
    while not q.empty():
        current = q.get()
        sortedlist.append(current)
        for adj_vertex in ads_graph.get_adjucent_vertices(current):
            indegree = indegree_map[adj_vertex]
            indegree -=1
            indegree_map[adj_vertex] =indegree
            if indegree == 0:
                q.put(adj_vertex)



    if len(sortedlist)>ads_graph.numVertices:
        return "graph has cycles"
    return sortedlist      



sl = topological_sort(ads_graph)
print(sl)
