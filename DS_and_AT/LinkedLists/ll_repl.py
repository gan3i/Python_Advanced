from linked_lists import Node,LinkedList

lst = [2,3,4,5,6]

if "__main__" == __name__:

    llst = LinkedList()

    node1 = Node()
    node1.data = 1

    node2 =Node()
    node2.data = 2
    node1.next = node2

    node3 = Node()
    node3.data = 3
    node2.next = node3

    llst.head = node1 

    #inserting the value at the begining.
    node = Node()
    node.data =0
    llst.insert_at_begining(node)

    #inserting the value at the end
    node4 = Node()
    node4.data = 4
    llst.insert_at_end(node4)

    #insert value at given position
    node23 = Node()
    node23.data =23
    llst.insert_at_position(0,node23)
    
    print(llst.len())
    