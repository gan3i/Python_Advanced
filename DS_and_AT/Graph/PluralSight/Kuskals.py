from PriorityDict import priority_dict

from AdjucencyMatrixGraph import AdjucencyMatrixGraph

def spanning_tree(graph,source):

    pq = priority_dict()

    for v in range(graph.numVertices):
        for nhbr in graph.get_adjucent_vertices(v):
            pq[(v,nhbr)] = graph.get_edge_weight(v,nhbr)

    spanning_tree = {x:set() for x in range(graph.numVertices)}

    num_edges = 0
    while len(pq.keys()) > 0 and num_edges < graph.numVertices:

        v1,v2 = pq.pop_smallest()

        if v1 in spanning_tree[v2]:
            continue

        vertex_pair = sorted([v1,v2])
        spanning_tree[vertex_pair[0]].add(vertex_pair[1])
        if has_cycle(spanning_tree):
            spanning_tree[vertex_pair[0]].remove(vertex_pair[1])
            continue

        num_edges +=1
    for item in spanning_tree.items():
        print(item)
def has_cycle(spanning_tree):

    for source in spanning_tree:
        q = []
        q.append(source)

        visited = set()

        while len(q)>0:
            current = q.pop()

            if current in visited:
                return True

            visited.add(current)

            q.extend(spanning_tree[current])

    return False


graph = AdjucencyMatrixGraph(7,False)

graph.add_edge(0,1,2)
graph.add_edge(0,2,1)
graph.add_edge(1,5,4)
graph.add_edge(1,4,3)
graph.add_edge(2,3,1)
graph.add_edge(4,5,2)
graph.add_edge(3,4,1)
graph.add_edge(5,6,1)

spanning_tree(graph,0)