import unittest
from linked_lists import Node,LinkedList

class LinkedListTest(unittest.TestCase):

    def setUp(self) ->None:
        self.linkedlist = LinkedList()
        node1 = Node()
        node2 = Node()
        node1.next = node2
        node3 = Node()
        node2.next = node3
        self.linkedlist.head = node1

    def tearDowm(self) ->None:
        pass

    def test_linkedlist_length(self):
        self.assertEqual(3,self.linkedlist.len())

    def test_insert_at_begining(self):
        node_begining = Node
        self.linkedlist.insert_at_begining(node_begining)
        self.assertEqual(4,self.linkedlist.len())

    def test_insert_at_end(self):
        node_end = Node()
        self.linkedlist.insert_at_end(node_end)
        self.assertEqual(4,self.linkedlist.len())

    def test_insert_at_position(self):
        node_pos = Node()
        self.linkedlist.insert_at_position(0,node_pos)
        self.assertEqual(4,self.linkedlist.len())

        

