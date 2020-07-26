from tree import inOrder
class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

six = Node(6)

two = Node(2)
eight= Node(8)
six.left = two
six.right = eight

one= Node(1)
four =  Node(4)  
two.left = one
two.right = four  


three = Node(3)
five =  Node(5)
four.left = three
four.right = five 

seven = Node(7)
nine =  Node(9)
eight.left = seven
eight.right = nine
# left <= root < right
class BST():
    def __init__(self,root=None):
        self.root = root

    @staticmethod 
    def getNodeByKey_recursion(root, key):
        if root == None or root.data == key:
            return root
        elif root.data > key :
            return BST.getNodeByKey_recursion(root.left,key)
        elif root.data < key :
            return BST.getNodeByKey_recursion(root.right,key)

    @staticmethod
    def insertNode_recursion(root, key):
        if not root:
            root = Node(key)
            return
        if key < root.data:
            if not root.left:
                root.left = Node(key)
                return
            else:
                BST.insertNode_recursion(root.left, key)
        elif key >= root.data :
            if not root.right:
                root.right = Node(key)
                return
            else:
                BST.insertNode_recursion(root.right, key)
    
    @staticmethod
    def inOrder(root):
        if not root:
            return
        BST.inOrder(root.left)
        print(root.data)
        BST.inOrder(root.right)

    @staticmethod
    def getInOrderSuccessor(root):
        if root is None:
            return root
        current = root
        while current.left is not None:
            current = current.left

        return current
    @staticmethod
    def getInOrderPredecessor(root):
        if root is None:
            return root
        current = root

        while current.right is not None:
            current = current.right

        return current
            
    @staticmethod
    def delete(root, key):
        if root is None:
            return root

        if root.data < key:
            root.right = BST.delete(root.right , key)
        elif root.data > key:
            root.left = BST.delete(root.left , key)
        else:

            if root.left is None:
                temp = root.right
                root = None
                return temp
            if root.right is None:
                temp = root.left
                root = None
                return temp
            temp = BST.getInOrderSuccessor(root.right)

            root.data = temp.data

            root.right = BST.delete(root.right, temp.data) 
        return root
    @staticmethod
    def delete2(root, key):
        if root is None:
            return root

        if root.data < key:
            root.right = BST.delete(root.right , key)
        elif root.data > key:
            root.left = BST.delete(root.left , key)
        else:

            if root.left is None:
                temp = root.right
                root = None
                return temp
            if root.right is None:
                temp = root.left
                root = None
                return temp

            parent = root
            successor = parent.right

            while successor.left:
                parent = successor
                successor = successor.left

            root.data = successor.data

            if  successor.right:
                parent.left = successor.right
                successor =None
            else:
                parent.left = None
                successor = None   
            # return root
        return root

    def getNodeByKey2_itiration(self, key):
        current= self.root
        while current:
            if current.data == key:
                break
            elif current.data > key:
                current = current.left
            elif current.data < key:
                current = current.right

        return current

    def insertNode_itiration(self, key):
        if not self.root:
            self.root= Node(key)
            return
        current = self.root 
        while current:
            if key < current.data:
                if not current.left:
                    current.left = Node(key)
                    break 
                else:
                    current = current.left
            elif key >= current.data :
                if not current.right:
                    current.right = Node(key)
                    break
                else:
                    current = current.right
        return current

    def print_inOrder(self):
        BST.inOrder(self.root)

    def deleteNodeByKey(self, key):
        return BST.delete2(self.root, key)
    def minValue(self):
        if self.root is None:
            return self.root
        current = self.root
        while current.left:
            current = current.left
        return current.data
    def maxValue(self):
        if self.root is None:
            return self.root
        current = self.root.right
        while current.right:
            current = current.right

        return current.data
    
    def successor(self,key):
        Node = BST.getNodeByKey_recursion(self.root,key)
        if not Node:
            return Node
        return BST.getInOrderSuccessor(Node.right)
    def predecessor(self,key):
        Node = BST.getNodeByKey_recursion(self.root,key)
        if not Node:
            return Node
        return BST.getInOrderPredecessor(Node.left)
bst = BST(six)
# print(BST.getNodeByKey_recursion(bst.root,5).data)
# print(bst.getNodeByKey2_itiration(11).data)

# print(getNodeByKey2(six,6).data)
# BST.insertNode_recursion(bst.root,6)
# bst.insertNode_itiration(6)

# insertNode2(six,6)
# insertNode2(six,6)
# insertNode(root,6)

# r = bst.deleteNodeByKey(2)
# bst.print_inOrder()
# print(bst.minValue())
# print(bst.maxValue())
print(bst.successor(1))
print(bst.predecessor(6).data)


