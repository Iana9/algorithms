import unittest

from practice3.LinkedList import LinkedList, Position


class LinkedListInitTest(unittest.TestCase):
    def test_empty_list(self):
        lst = LinkedList()
        self.assertEqual(len(lst), 0)
        self.assertEqual(list(lst), [])
        self.assertTrue(lst.begin().is_end())
        self.assertTrue(lst.end().is_end())


class LinkedListInsertTest(unittest.TestCase):
    def test_insert_begin(self):
        lst = LinkedList()
        pos = lst.insert_begin(10)
        self.assertEqual(len(lst), 1)
        self.assertEqual(list(lst), [10])
        self.assertEqual(lst.get_at(pos), 10)

    def test_insert_end(self):
        lst = LinkedList()
        pos = lst.insert_end(20)
        self.assertEqual(list(lst), [20])
        self.assertEqual(lst.get_at(pos), 20)

    def test_insert_begin_and_end(self):
        lst = LinkedList()
        lst.insert_begin(2)
        lst.insert_begin(1)
        lst.insert_end(3)
        self.assertEqual(list(lst), [1, 2, 3])

    def test_insert_at_middle(self):
        lst = LinkedList()
        lst.insert_end("a")
        lst.insert_end("c")
        pos_c = lst.find("c")
        lst.insert_at(pos_c, "b")
        self.assertEqual(list(lst), ["a", "b", "c"])

    def test_insert_at_begin_via_position(self):
        lst = LinkedList()
        lst.insert_end(2)
        lst.insert_at(lst.begin(), 1)
        self.assertEqual(list(lst), [1, 2])

    def test_insert_at_end_via_position(self):
        lst = LinkedList()
        lst.insert_end(1)
        lst.insert_at(lst.end(), 2)
        self.assertEqual(list(lst), [1, 2])


class LinkedListAccessTest(unittest.TestCase):
    def test_get_at(self):
        lst = LinkedList()
        p1 = lst.insert_end(1)
        p2 = lst.insert_end(2)
        self.assertEqual(lst.get_at(p1), 1)
        self.assertEqual(lst.get_at(p2), 2)

    def test_replace_at(self):
        lst = LinkedList()
        pos = lst.insert_end("old")
        lst.replace_at(pos, "new")
        self.assertEqual(list(lst), ["new"])
        self.assertEqual(lst.get_at(pos), "new")


class LinkedListSearchTest(unittest.TestCase):
    def test_contains_and_find(self):
        lst = LinkedList()
        lst.insert_end(1)
        lst.insert_end(2)
        lst.insert_end(3)

        self.assertTrue(lst.contains(2))
        self.assertFalse(lst.contains(99))

        pos = lst.find(2)
        self.assertIsNotNone(pos)
        self.assertEqual(lst.get_at(pos), 2)

    def test_find_returns_none_if_missing(self):
        lst = LinkedList()
        lst.insert_end(1)
        self.assertIsNone(lst.find(42))

    def test_find_first_occurrence(self):
        lst = LinkedList()
        lst.insert_end(1)
        lst.insert_end(2)
        lst.insert_end(1)

        pos = lst.find(1)
        self.assertEqual(lst.get_at(pos), 1)
        self.assertEqual(list(lst), [1, 2, 1])

    def test_contains_on_empty_list(self):
        lst = LinkedList()
        self.assertFalse(lst.contains(1))
        self.assertIsNone(lst.find(1))


class LinkedListRemoveTest(unittest.TestCase):
    def test_remove_begin(self):
        lst = LinkedList()
        lst.insert_end(1)
        lst.insert_end(2)
        value = lst.remove_begin()
        self.assertEqual(value, 1)
        self.assertEqual(list(lst), [2])

    def test_remove_end(self):
        lst = LinkedList()
        lst.insert_end(1)
        lst.insert_end(2)
        value = lst.remove_end()
        self.assertEqual(value, 2)
        self.assertEqual(list(lst), [1])

    def test_remove_at(self):
        lst = LinkedList()
        lst.insert_end(1)
        pos = lst.insert_end(2)
        lst.insert_end(3)
        value = lst.remove_at(pos)
        self.assertEqual(value, 2)
        self.assertEqual(list(lst), [1, 3])

    def test_remove_from_empty_list(self):
        lst = LinkedList()
        with self.assertRaises(ValueError):
            lst.remove_begin()
        with self.assertRaises(ValueError):
            lst.remove_end()

    def test_invalid_position_after_remove(self):
        lst = LinkedList()
        pos = lst.insert_end(10)
        lst.remove_at(pos)
        with self.assertRaises(ValueError):
            pos._check_valid()


class LinkedListMixedTest(unittest.TestCase):
    def test_sequence_of_operations(self):
        lst = LinkedList()
        lst.insert_end("a")
        lst.insert_end("c")
        pos_b = lst.insert_at(lst.find("c"), "b")
        lst.replace_at(pos_b, "B")
        self.assertEqual(list(lst), ["a", "B", "c"])

        self.assertEqual(lst.remove_begin(), "a")
        self.assertEqual(lst.remove_end(), "c")
        self.assertEqual(len(lst), 1)
        self.assertEqual(list(lst), ["B"])

    def test_different_value_types(self):
        lst = LinkedList()
        lst.insert_end(1)
        lst.insert_end("text")
        lst.insert_end([1, 2, 3])
        self.assertEqual(list(lst), [1, "text", [1, 2, 3]])


if __name__ == "__main__":
    unittest.main()
