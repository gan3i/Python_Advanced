from collections import defaultdict

# works for disconnected graph as well
#TODO try the same problem with colors
class Graph():
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u,v):
        self.graph[u].append(v)

    def isCyclic(self):
        visited = [False] * self.vertices
        recStack = [False] * self.vertices

        for v in range(self.vertices):
            if visited[v] == False:
                if self.isCyclicUtil(v,visited,recStack) == True:
                    return True
        return False
    def isCyclicUtil(self,v, visited, recStack):
        visited[v] = True
        recStack[v] = True

        for nhbr in self.graph[v]:
            if visited[nhbr] == False:
                if self.isCyclicUtil(nhbr, visited, recStack) == True:
                    return True
            elif recStack[nhbr] == True:
                return True

        recStack[v] = False
        return False 


g = Graph(10)
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(1, 3) 
g.addEdge(1, 6) 
g.addEdge(2, 5) 
g.addEdge(2, 3) 
g.addEdge(3, 4) 
g.addEdge(3, 7) 
g.addEdge(3, 6) 
g.addEdge(5, 3) 
g.addEdge(5, 4) 
g.addEdge(6, 7) 
# g.addEdge(6, 1) 

# disconnected graph
# g.addEdge(8,9)
# g.addEdge(9,8)


if g.isCyclic() == 1: 
    print ("Graph has a cycle")
else: 
    print ("Graph has no cycle")