import unittest
from deque import Deque

class DequeTests(unittest.TestCase):

    def test_deque(self):
        #arrange - act
        dq = Deque(4)
        #assert
        self.assertEqual(4,dq.size)
        self.assertEqual(-1,dq.rear)
        self.assertEqual(-1,dq.front)
        self.assertFalse(dq.isFull)
        self.assertTrue(dq.isEmpty)

    def test_insertAtFront(self):
        #arrange
        dq = Deque(4)
        #act
        dq.insertAtFront(1)
        # assert
        self.assertEqual(0,dq.front)
        self.assertEqual(0,dq.rear)
        #act
        dq.insertAtFront(2)
        #assert
        self.assertEqual(1,dq.front)
        self.assertEqual(0,dq.rear)
        #act
        dq.insertAtFront(3)
        #assert
        self.assertEqual(2,dq.front)
        self.assertEqual(0,dq.rear)
        #act
        dq.insertAtFront(4)
        #assert
        self.assertEqual(3,dq.front)
        self.assertEqual(0,dq.rear)
        #act - assert
        with self.assertRaises(ValueError):
            dq.insertAtFront(5)
        self.assertEqual(3,dq.front)
        self.assertEqual(0,dq.rear)
    # @unittest.skip("test")
    def test_insertAtRear(self):
        #arrange
        dq = Deque(3)
        #act
        dq.insertAtRear(1)
        #assert
        self.assertEqual(0,dq.front)
        self.assertEqual(0,dq.rear)
        #act
        dq.insertAtRear(2)
        #assert
        self.assertEqual(2,dq.rear)
        self.assertEqual(0 ,dq.front)
        #act
        dq.insertAtRear(3)
        #assert
        self.assertEqual(1,dq.rear)
        self.assertEqual(0 ,dq.front)
        #act - assert
        with self.assertRaises(ValueError):
            dq.insertAtRear(4)
        self.assertEqual(1,dq.rear)
        self.assertEqual(0 ,dq.front)

    def test_deleteAtFront(self):
        #arrange
        dq = Deque(4)
        #assert
        with self.assertRaises(ValueError):
            dq.deleteAtFront()
        #act
        dq.insertAtFront(1)
        #assert
        self.assertEqual(1, dq.deleteAtFront())
        #act
        dq.insertAtRear(1)
        dq.insertAtRear(2)
        #assert
        self.assertEqual(1,dq.deleteAtFront())
        self.assertEqual(2,dq.deleteAtFront())
        with self.assertRaises(ValueError):
            dq.deleteAtFront()
        #act
        dq.insertAtRear(1)
        dq.insertAtFront(2)
        #assert
        self.assertEqual(2,dq.deleteAtFront())
        self.assertEqual(1,dq.deleteAtFront())

        with self.assertRaises(ValueError):
            dq.deleteAtFront()

    def test_deleteAtRear(self):
        #arrange
        dq = Deque(4)
        #assert
        with self.assertRaises(ValueError):
            dq.deleteAtRear()
        #act
        dq.insertAtRear(1)
        #assert
        self.assertEqual(1, dq.deleteAtFront())
        #act
        dq.insertAtRear(1)
        #assert
        self.assertEqual(1, dq.deleteAtRear())
        with self.assertRaises(ValueError):
            dq.deleteAtFront()
        #act
        dq.insertAtFront(1)
        dq.insertAtFront(2)
        dq.insertAtRear(3)
        #assert
        self.assertEqual(3,dq.deleteAtRear())
        self.assertEqual(1,dq.deleteAtRear())
        self.assertEqual(2,dq.deleteAtRear())
        with self.assertRaises(ValueError):
            dq.deleteAtFront()
        #act
        dq.insertAtRear(1)
        dq.insertAtFront(2)
        dq.insertAtRear(3)
        #assert
        self.assertEqual(3,dq.deleteAtRear())
        self.assertEqual(1,dq.deleteAtRear())
        self.assertEqual(2,dq.deleteAtRear())

        with self.assertRaises(ValueError):
            dq.deleteAtFront()

    def test_getFront(self):
        #arrange
        dq = Deque(4)
        dq.insertAtFront(1)
        self.assertEqual(1,dq.getFront())
        dq.insertAtFront(1)
        dq.insertAtFront(2)
        dq.insertAtFront(3)
        self.assertEqual(3,dq.getFront())
        dq.deleteAtFront()
        self.assertEqual(2,dq.getFront())
        dq.deleteAtFront()
        self.assertEqual(1,dq.getFront())
        dq.deleteAtFront()
        self.assertEqual(1,dq.getFront())
        dq1 = Deque(4)
        dq1.insertAtFront(2)
        dq1.insertAtFront(3)

        self.assertEqual(3,dq1.getFront())
        dq2 = Deque(4)
        dq2.insertAtFront(2)
        dq2.insertAtRear(3)

        self.assertEqual(2,dq2.getFront())
        dq2.deleteAtFront()
        self.assertEqual(3,dq2.getFront())

    def test_getRear(self):
        #arrange
        dq = Deque(4)
        dq.insertAtRear(1)
        self.assertEqual(1,dq.getRear())
        dq.insertAtRear(1)
        dq.insertAtRear(2)
        dq.insertAtRear(3)
        self.assertEqual(3,dq.getRear())
        dq.deleteAtRear()
        self.assertEqual(2,dq.getRear())
        dq.deleteAtRear()
        self.assertEqual(1,dq.getRear())
        dq.deleteAtRear()
        self.assertEqual(1,dq.getRear())
        dq1 = Deque(4)
        dq1.insertAtRear(2)
        dq1.insertAtRear(3)

        self.assertEqual(3,dq1.getRear())
        dq2 = Deque(4)
        dq2.insertAtRear(2)
        dq2.insertAtFront(3)

        self.assertEqual(2,dq2.getRear())
        dq2.deleteAtRear()
        self.assertEqual(3,dq2.getRear())





if __name__ == "__main__":
    unittest.main()
