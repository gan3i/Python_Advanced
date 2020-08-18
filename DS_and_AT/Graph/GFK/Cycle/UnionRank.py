#undirected graph
# https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/

# using disjoint set 


from collections import defaultdict

class Graph():
    def __init__(self, v):
        self.v =v
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    class Subset():
        def __init__(self,parent, rank):
            self.parent = parent
            self.rank = rank

    def isCyclic(self):


        subsets = [self.Subset(x,0) for x in range(self.v)]

        for u in self.graph:
            for v in self.graph[u]:
                u_p = self.find_parent(subsets, u) 
                v_p = self.find_parent(subsets, v)

                if v_p == u_p:
                    return True
                else:
                    self.union(subsets, u, v)

        return False

    #path compresion
    def find_parent(self,subsets, v):
        if subsets[v].parent != v:
            subsets[v].parent = self.find_parent(subsets, subsets[v].parent)
        return subsets[v].parent

    #union by rank
    def union(self,subsets, u, v):

        #Attach smaller rank tree under root
        # of higher rank tree (Union by rank)
        if subsets[u].rank > subsets[v].rank:
            subsets[u].parent = v
        elif subsets[u].rank < subsets[v].rank:
            subsets[v].parent = u
        else:
            subsets[v].parent =u
            subsets[u].rank +=1

        
g = Graph(3) 
g.addEdge(0, 1) 
g.addEdge(1, 2) 
g.addEdge(0, 2) 
  
if g.isCyclic(): 
    print('Graph contains cycle') 
else: 
    print('Graph does not contain cycle') 