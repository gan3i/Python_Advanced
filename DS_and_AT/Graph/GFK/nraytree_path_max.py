'''
Given a tree with N nodes and N-1 edges, calculate the maximum sum of the node values from root to any of the leaves without re-visiting any node

'''
#if nodes and edges is what we get as input then method signature would look like this
def max_path_sum(nodes, edges):
    tree = dict()

    #build a directed graph
    for u, v in edges:
        if u > v:
            u, v = v, u # we may get revered edges this line just corrects that.
        if u in tree:
            tree[u].append(v)
        else:
            tree[u] = [v]
    # we know that first element in the array is the root of the tree,
    return path_sum_helper(tree, nodes, 1)

def path_sum_helper(tree, nodes, root):
    if root not in tree: # it's a leaf node so just return the value
        return nodes[root-1] 

    child_path_max = float('-inf')
    for child in tree[root]:
        child_path_sum = path_sum_helper(tree, nodes, child)
        child_path_max = max(child_path_max, child_path_sum)

    return child_path_max + nodes[root-1]

#driver code
nodes = [ 3, 2, 1, 10, 1, 3, 9, 1, 5, 3, 4, 50, 9, 8 ]
# edges are based on indices of the aray
edges = [[1,2], [1,3], [1,4], [2,5], [2,6], [3,7], [4,8],[4,9], [4,10], [5,11], [5,12], [7, 13], [7, 14]]

print(max_path_sum(nodes, edges))






        
    