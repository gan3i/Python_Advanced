

class Node:
    def __init__(self,name):
        self.name = name #name of the node/vertices
        self.edge = [] #name of nodes which this depends on/ called edges


    def addEdge(self,node):
        self.edge.append(node)

def test_data():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')

    a.addEdge(b) # a depends on b
    a.addEdge(d) # a depends on d
    b.addEdge(c) # b depends on c
    b.addEdge(e) # b depends on e
    c.addEdge(d) # c depends on d
    c.addEdge(e) # c depends on e  
    # d.addEdge(b) # d depends on b and this causes cyclic dependency.

    return a





