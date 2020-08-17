from collections import defaultdict


class Graph():
    def __init__(self,v):
        self.v = v
        self.graph = defaultdict()

    def add_edge(self,v,u,w):
        self.graph[(v,u)] = w
        self.graph[(u,v)] = w
    class Subset():
        def __init__(self,parent,rank):
            self.parent = parent
            self.rank = rank

    def kruskals_MST(self):

        subsets = [self.Subset(x,0) for x in range(self.v)]
        spanning_tree = {x :set() for x in range(self.v)}
        graph = sorted(self.graph , key=lambda value: value)
        for e in graph:
            x = self.find(subsets,e[0])
            y = self.find(subsets,e[1])

            if x is not y:
                vertex = sorted([e[0], e[1]])
                spanning_tree[vertex[0]].add(vertex[1])
                self.union(subsets, x, y)

        for item in spanning_tree.items():
            print(item)

    def find(self,subsets, i):
        if subsets[i].parent != i:
            subsets[i].parent = self.find(subsets,subsets[i].parent)
        return subsets[i].parent

    def union(self, subsets, u, v):
        x= self.find(subsets,u)
        y= self.find(subsets,v)

        if x == y:
            return

        if subsets[x].rank > subsets[y].rank:
            subsets[y].parent = x
        elif subsets[x].rank < subsets[y].rank:
            subsets[x].parent = y
        else:
            subsets[x].parent = y
            subsets[y].rank +=1


    

graph = Graph(7)

graph.add_edge(0,1,2)
graph.add_edge(0,2,1)
graph.add_edge(1,5,4)
graph.add_edge(1,4,3)
graph.add_edge(2,3,1)
graph.add_edge(4,5,2)
graph.add_edge(3,4,1)
graph.add_edge(5,6,1)

graph.kruskals_MST()
    
