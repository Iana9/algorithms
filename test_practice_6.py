import unittest

from practice6.binary_search_tree import BinarySearchTree


class BinarySearchTreeTest(unittest.TestCase):
    def test_binary_search_tree_actions(self):
        """Тест из BinarySearchTreeTest.java."""
        bst = BinarySearchTree()

        bst.add(4, 4)
        bst.add(2, 2)
        bst.add(1, 1)
        bst.add(3, 3)
        bst.add(6, 6)
        bst.add(5, 5)
        bst.add(7, 7)

        self.assertIsNone(bst.remove(8))
        self.assertEqual(bst.get(3), 3)

        self.assertEqual(bst.remove(4), 4)
        self.assertIsNone(bst.get(4))

        self.assertEqual(bst.get(5), 5)
        bst.add(5, 10)
        self.assertEqual(bst.get(5), 10)

        self.assertEqual(bst.remove(5), 10)
        self.assertIsNone(bst.get(5))

    def test_empty_tree(self):
        bst = BinarySearchTree()
        self.assertIsNone(bst.get(1))
        self.assertIsNone(bst.remove(1))

    def test_single_element(self):
        bst = BinarySearchTree()
        bst.add(1, "one")
        self.assertEqual(bst.get(1), "one")
        self.assertEqual(bst.remove(1), "one")
        self.assertIsNone(bst.get(1))

    def test_overwrite_existing_key(self):
        bst = BinarySearchTree()
        bst.add(2, "old")
        bst.add(2, "new")
        self.assertEqual(bst.get(2), "new")

    def test_remove_leaf_node(self):
        bst = BinarySearchTree()
        bst.add(2, 2)
        bst.add(1, 1)
        bst.add(3, 3)
        self.assertEqual(bst.remove(1), 1)
        self.assertIsNone(bst.get(1))
        self.assertEqual(bst.get(2), 2)
        self.assertEqual(bst.get(3), 3)


if __name__ == "__main__":
    unittest.main()
