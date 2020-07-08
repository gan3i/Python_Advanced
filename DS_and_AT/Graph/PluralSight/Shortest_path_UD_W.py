from AdjucencyMatrixGraph import AdjucencyMatrixGraph
from queue import Queue

graph = AdjucencyMatrixGraph(7,False)

graph.add_edge(0,1,2)
graph.add_edge(0,2,4)
graph.add_edge(1,5,4)
graph.add_edge(1,4,3)
graph.add_edge(2,3,1)
graph.add_edge(4,5,2)
graph.add_edge(3,4,1)
graph.add_edge(5,6,1)

# graph.display()

# def shortest_path(graph,start,end):
#     distace_table = {x:(None,None) for x in range(graph.numVertices)}
#     for key,value in distace_table.items():
#         print(key,value)
#         if distace_table[current][0] is not None:

def build_distanec_table(graph,start):
    distance_table = {x : (None,None) for x in range(graph.numVertices)}
    distance_table[start] = (0,start)
    q = Queue()
    q.put(start)
    while not q.empty():
        current = q.get()
        curent_distance = distance_table[current][0]
        for adj in graph.get_adjucent_vertices(current):
            new_dist = curent_distance + graph.get_edge_weight(current,adj)
            
            if distance_table[adj][0] is not None :
                if new_dist < distance_table[adj][0] :
                    distance_table[adj] = (new_dist,current)
                    q.put(adj)
                    distance_table[adj] = new_dist
                else:
                    continue
            distance_table[adj] = (new_dist,current)
            q.put(adj)
    return distance_table


def shortest_path(gaph, start, end):
    distance_table = build_distanec_table(graph, start)
    path = [end]
    previous_vertex = distance_table[end][1]
    while previous_vertex is not start:
        path = [previous_vertex] + path
        previous_vertex = distance_table[previous_vertex][1]
    return [start]+ path



print(shortest_path(graph,0,6))


