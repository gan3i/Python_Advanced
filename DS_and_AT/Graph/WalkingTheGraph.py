from Node import test_data

a = test_data()



def dep_resolve(node,resolved,unresolved):
    unresolved.append(node)
    for edge in node.edge:
        if edge not in resolved:
            if edge in unresolved:
                raise Exception('Circular reference detected : {0} -> {1}'.format(node.name,edge.name))
            dep_resolve(edge,resolved,unresolved)# this goes into first node in edges list.
    resolved.append(node)
    unresolved.remove(node)
    
resolved = []
dep_resolve(a, resolved,[])
print("Resolved Nodes")
for node in resolved:
    print(node.name)

s= "hello.txt"

print(s.lower)


