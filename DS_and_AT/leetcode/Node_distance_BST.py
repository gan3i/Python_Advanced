

class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insertToBST(root, data):

    if root is None:
        root = Node(data)
    elif data < root.data:
        root.left = insertToBST(root.left, data)
    elif data> root.data:
        root.right - insertToBST(root.left, data)
    return root

def distanceFromRoot(root, key):
    if root.data == key:
        return 1
    elif key < root.data:
        return 1+ distanceFromRoot(root.left, key)
    elif key > root.data:
        return 1+ distanceFromRoot(root.right, key)

def getNodeDistance(root, a, b):

    if root == None:
        return 0

    if a > root.data and b>root.data:
        return getNodeDistnace(root.right, a , b)
    
    if a < root.data and b < root.data:
        return getNodeDistance(root.left, a , b)

    return distanceFromRoot(root, a) + distanceFromRoot(root,b)




    







