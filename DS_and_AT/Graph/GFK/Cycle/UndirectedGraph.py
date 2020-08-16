from collections import defaultdict

#usinf disjointset
# naive union and find

class Graph():
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u,v):
        self.graph[u].append(v)

    def isCyclic(self):

        # [0,1,2,3,4]
        # [-1,-1,-1,-1,-1]
        subset = [-1] * self.vertices

        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(subset, i)
                y = self.find_parent(subset, j)
                if x== y :
                    return True
                subset[x] = y 

        return False
    def find_parent(self, subset,i):
        if subset[i] == -1:
            return i
        return self.find_parent(subset, subset[i])

    def union(self,subset,x, y):
        # x_set = self.find_parent(subset, x)
        # y_set = self.find_parent(subset, y)
        subset[x] = y 


g = Graph(10)

g.addEdge(0,1)
# g.addEdge(1,0)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(0,4)
# g.addEdge(0,5)
g.addEdge(2,6)
g.addEdge(2,5)
g.addEdge(3,7)
g.addEdge(3,4)
g.addEdge(7,8)
g.addEdge(7,9)

print(g.isCyclic())