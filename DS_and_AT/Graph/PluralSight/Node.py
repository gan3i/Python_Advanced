class Node:

    def __init__(self,vertexId):
        self.vertexId = vertexId
        self.adjucency_set = set()

    def add_edge(self,v):
        if self.vertexId == v:
            raise ValueError(f'The vertex {v} cannot  be adjucent to itself')

        self.adjucency_set.add(v)

    def get_adjucent_vertices(self):
        return sorted(self.adjucency_set)



