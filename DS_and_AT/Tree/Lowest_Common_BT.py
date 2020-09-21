class Node():
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None


def findLCA(root : Node , a : Node , b: Node) -> Node:


    if root == None:
        return None

    if root.val == a.val or root.val == b.val:
        return root
    else:
        left = findLCA(root.left, a, b)
        right = findLCA(root.right, a , b)

        if not left and not right:
            return None
        elif left and right:
            return root
        elif left:
            return left
        else:
            return right



