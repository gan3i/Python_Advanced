# Python3 program to find the maximum depth of tree 

# A binary tree node 
class Node: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

# Compute the "maxDepth" of a tree -- the number of nodes 
# along the longest path from the root node down to the 
# farthest leaf node 
def maxDepth(node): 
    if node is None: 
        return 0 
    else :
        lDepth = maxDepth(node.left) + 1
        rDepth = maxDepth(node.right) + 1
        
        return max(lDepth,rDepth)


# Driver program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

root.left.left.left = Node(6) 


print ("Height of tree is %d" %(maxDepth(root))) 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
