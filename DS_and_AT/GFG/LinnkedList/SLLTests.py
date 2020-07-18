import unittest
from SLL import *

class NodeTests(unittest.TestCase):

    def test_Node(self):
        node = Node(1)
        self.assertEqual(1,node.data)

    def test_Node_with_no_data(self):
        with self.assertRaises(TypeError):
            node = Node()

class TestSLL(unittest.TestCase):

    def test_insert_on_empty_list(self):
        #arrange
        sll = SLL()

        #act
        sll.insert(1)

        #assert
        self.assertEqual(sll.head.data, 1)
        self.assertEqual(sll.tail, sll.head)

    def test_insert_on_nonempty_list(self):
        #arrange
        sll = SLL()
        for i in range(3):
            sll.insert(i)

        #act
        sll.insert(4)

        #asser
        self.assertEqual(4,sll.tail.data)

    def test_insert_at_begining_on_empty_list(self):
        #arrange
        sll = SLL()
        
        #act
        sll.insert_at_begining(1)

        #assert
        self.assertEqual(1,sll.head.data)

    def test_insert_at_begining_on_nonempty_list(self):
        #arrange
        sll = SLL()
        for i in range(3):
            sll.insert(i)

        #act 
        sll.insert_at_begining(4)

        #assert
        self.assertEqual(4,sll.head.data)

class FindMidTests(unittest.TestCase):

    def test_findMid_m1_odd(self):
        #arrange
        sll = SLL()
        for i in range(5):
            sll.insert(i)

        #act - assert
        self.assertEqual(2,findMid_m1(sll.head))

    def test_findMid_m1_even(self):
        #arrange
        sll = SLL()
        for i in range(6):
            sll.insert(i)

        #act - assert
        self.assertEqual(3,findMid_m1(sll.head))

    def test_findMid_m2_odd(self):
        #arrange
        sll = SLL()
        for i in range(5):
            sll.insert(i)

        #act - assert
        self.assertEqual(2,findMid_m2(sll.head))

    def test_findMid_m2_even(self):
        #arrange
        sll = SLL()
        for i in range(6):
            sll.insert(i)

        #act - assert
        self.assertEqual(3,findMid_m2(sll.head))

    def test_findMid_m3_odd(self):
        #arrange
        sll = SLL()
        for i in range(5):
            sll.insert(i)

        #act - assert
        self.assertEqual(2,findMid_m3(sll.head))

    def test_findMid_m3_even(self):
        #arrange
        sll = SLL()
        for i in range(6):
            sll.insert(i)

        #act - assert
        self.assertEqual(3,findMid_m3(sll.head))



if __name__ == "__main__":
    unittest.main()



