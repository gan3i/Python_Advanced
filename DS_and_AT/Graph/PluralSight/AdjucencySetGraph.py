from Graph import Graph
from Node import Node

class AdjucencySetGraph(Graph):
    def __init__(self,numVertices,directed = False):
        super(AdjucencySetGraph,self).__init__(numVertices,directed)

        self.vertex_list = []
        for  i in range(numVertices):
            self.vertex_list.append(Node(i))
    @property        
    def vertices(self):
        return self.vertex_list
    def add_edge(self,v1,v2,weight = 1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1<0 or v2< 0:
            raise ValueError(f'Vertices {v1} and {v2} are out of bounds')

        if weight != 1:
            raise ValueError("An Edge cannot have negative weight")

        self.vertex_list[v1].add_edge(v2)

        if not self.directed:
            self.vertex_list[v2].add_edge(v1)

    def get_adjucent_vertices(self,v):
        if v <0  or v >= self.numVertices:
            raise ValueError(f"cannot access vertex {v}")

        return self.vertex_list[v].get_adjucent_vertices()

    def get_indegree(self,v):
        if v<0 or v >= self.numVertices:
            raise ValueError(f'cannot access vertex {v}')

        indegree = 0
        for i in range(self.numVertices):
            if v in self.get_adjucent_vertices(i):
                indegree +=1
        return indegree
    def get_edge_weight(self,v1,v2):
        return 1
    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjucent_vertices(i):
                print(i,"-->",v)

# adm_graph=  AdjucencySetGraph(4)
# adm_graph.add_edge(0,1)
# adm_graph.add_edge(0,2)
# adm_graph.add_edge(2,3) 
# for i in range(4):
#     print('Adjucent to :',i,adm_graph.get_adjucent_vertices(i))
# for i in range(4):
#     print('Indegree :',i,adm_graph.get_indegree(i))
# for i in range(4):
#     for j in adm_graph.get_adjucent_vertices(i):
#         print('Edge :',i,j," weight : " ,adm_graph.get_edge_weight(i,j))

# adm_graph.display()

