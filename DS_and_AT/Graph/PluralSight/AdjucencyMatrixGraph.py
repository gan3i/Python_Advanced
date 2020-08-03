from Graph import Graph

class AdjucencyMatrixGraph(Graph):

    def __init__(self,numVertices,directed = True):
        super(AdjucencyMatrixGraph,self).__init__(numVertices,directed)
        self.matrix = [[0 for x in range(numVertices)] for y in range(numVertices)]

    def add_edge(self,v1,v2,weight = 1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1<0 or v2< 0:
            raise ValueError(f'Vertices {v1} and {v2} are out of bounds')

        if weight < 0:
            raise ValueError("An Edge cannot have negative weight")

        self.matrix[v1][v2] = weight

        if self.directed == False:
            self.matrix[v2][v1]  =  weight

    def get_adjucent_vertices(self,v):
        if v <0  or v >= self.numVertices:
            raise ValueError(f"cannot access vertex {v}")

        adjucent_vertices = []
        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                adjucent_vertices.append(i)
        return adjucent_vertices

    def get_indegree(self,v):
        if v<0 or v >= self.numVertices:
            raise ValueError(f'cannot access vertex {v}')

        indegree = 0
        for i in range(self.numVertices):
            if self.matrix[i][v] >0:
                indegree +=1
        return indegree      
    def get_edge_weight(self,v1,v2):
        if v1 >= self.numVertices or v1<0 or v2 >=self.numVertices or v2 <0:
            raise ValueError(f'Vertices {v1} and {v2} are out of bound')
        return self.matrix[v1][v2]
    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjucent_vertices(i):
                print(i,"-->",v)

# adm_graph=  AdjucencyMatrixGraph(4,False)# make it True for directed graph
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
         