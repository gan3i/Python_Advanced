class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# root = Node(1)

# two = Node(2)
# three= Node(3)
# root.left = two
# root.right = three

# four= Node(4)
# five =  Node(5)  
# two.left = four
# two.right = five  


# seven = Node(7)
# six =  Node(6)
# three.left = seven
# three.right = six 

# eight = Node(8)
# nine =  Node(9)
# five.left = eight
# five.right = nine

def inOrder(root):  
    if root is None:
        return
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)

def preOrder(root):
    if root is None:
        return
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data)

def deleteTree(root):
    if root:
        deleteTree(root.left)
        deleteTree(root.right)
        root = None
    return root
from queue import Queue
def BFS(root):
    q = Queue()
    q.put(root)
    while not q.empty():
        current = q.get()
        print(current.data)
        if current.left is not None:
            q.put(current.left)
        if current.right is not None:
            q.put(current.right)


def DFS_recursion(root):
    if root:#using post order traversal
        DFS_recursion(root.left)
        DFS_recursion(root.right)
        print(root.data)

def Depth_first_traversal_using_list(root):
    s = [root]
    while len(s):
        current = s.pop()
        print(current.data)
        if current.right is not None:
            s.append(current.right)
        if current.left is not None:
            s.append(current.left)

def Breadth_first_traversal_list(root):
    s = [root]
    while len(s):
        current = s.pop(0)
        print(current.data)
        if current.right is not None:
            s.append(current.right)
        if current.left is not None:
            s.append(current.left)
# level order  traversal of tree uing height of the tree 
# takes O(n**2) in worst case
def height(root):
    if not root:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)

    return max(lheight , rheight) + 1


# Function to  print level order traversal of tree 
def printLevelOrder(root): 
    h = height(root) 
    for i in range(1, h+1): 
        printGivenLevel(root, i) 
  
  
# Print nodes at a given level 
def printGivenLevel(root , level): 
    if root is None: 
        return
    if level == 1: 
        print(root.data,end=" ") 
    elif level > 1 : 
        printGivenLevel(root.left , level-1) 
        printGivenLevel(root.right , level-1) 



        
# inOrder(root)
# preOrder(root)
# postOrder(root)
# root = deleteTree(root)
# if not root:
#     print("Tree is deleted")

# BFS(root)
# printLevelOrder(root)


