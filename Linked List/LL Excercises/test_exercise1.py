from unittest import TestCase

class TestNode(TestCase):
    def test_node_value(self):
        import exercise1
        node = exercise1.Node(1)
        self.assertEqual(node.value, 1)

    def test_node_next(self):
        import exercise1
        node1 = exercise1.Node(1)
        self.assertIsNone(node1.next)
        node2 = exercise1.Node(2)
        node1.next = node2
        self.assertEqual(node1.next, node2)
        
class TestLinkedList(TestCase):
    def test_initialization_of_linked_list(self):
        import exercise1
        linked_list = exercise1.LinkedList(1)
        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.tail.value, 1)
        self.assertEqual(linked_list.length, 1)

    def test_head(self):
        import exercise1
        linked_list = exercise1.LinkedList(1)
        self.assertEqual(linked_list.head.value, 1)

    def test_tail(self):
        import exercise1
        linked_list = exercise1.LinkedList(1)
        self.assertEqual(linked_list.tail.value, 1)

    def test_length(self):
        import exercise
        linked_list = exercise.LinkedList(1)
        self.assertEqual(linked_list.length, 1) 