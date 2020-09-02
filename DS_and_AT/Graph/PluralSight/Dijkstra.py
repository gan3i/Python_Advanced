from AdjucencyMatrixGraph import AdjucencyMatrixGraph
import PriorityDict

def build_distance_table(graph,start):
    distance_table = {x :(None,None) for x in range(graph.numVertices)}
    distance_table[start] = (0,start)
    pq =  PriorityDict.priority_dict()
    pq[start] = 0

    while len(pq.keys()) :
        current = pq.pop_smallest()

        current_distance = distance_table[current][0]
        for nhbr in graph.get_adjucent_vertices(current):
            distance = current_distance + graph.get_edge_weight(current,nhbr)

            nhbr_distance = distance_table [nhbr][0]

            if nhbr_distance is None or nhbr_distance > distance:
                distance_table[nhbr] = (distance, current)

                pq[nhbr] = distance

    return distance_table


def shortest_path(graph,start,end):
    dt = build_distance_table(graph,start)

    path = [end]
    previous = dt[end][1]
    while previous != None and previous  != start:
         path = [previous]+ path 
         previous = dt[previous][1]

    if previous is None  or previous != start:
        return 'NO PATH Exists'
    else:
         return [start] + path 

    
graph = AdjucencyMatrixGraph(7,True)

graph.add_edge(0,1,2)
graph.add_edge(0,2,4)
graph.add_edge(1,5,4)
graph.add_edge(1,4,3)
graph.add_edge(2,3,1)
graph.add_edge(4,5,2)
graph.add_edge(3,4,1)
graph.add_edge(5,6,1)

print(shortest_path(graph,2,6))


