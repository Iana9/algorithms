import unittest

from findminmax import Result, findMinMax, findMinMax2


class FindMinMaxTest(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(findMinMax([5]), Result(min=5, max=5))

    def test_two_elements(self):
        self.assertEqual(findMinMax([3, 7]), Result(min=3, max=7))
        self.assertEqual(findMinMax([7, 3]), Result(min=3, max=7))

    def test_unsorted_list(self):
        self.assertEqual(findMinMax([4, 1, 9, 2, 7]), Result(min=1, max=9))

    def test_sorted_ascending(self):
        self.assertEqual(findMinMax([1, 2, 3, 4, 5]), Result(min=1, max=5))

    def test_sorted_descending(self):
        self.assertEqual(findMinMax([5, 4, 3, 2, 1]), Result(min=1, max=5))

    def test_all_equal(self):
        self.assertEqual(findMinMax([7, 7, 7]), Result(min=7, max=7))

    def test_negative_numbers(self):
        self.assertEqual(findMinMax([-5, -1, -10, 3]), Result(min=-10, max=3))

    def test_mixed_positive_and_negative(self):
        self.assertEqual(findMinMax([-2, 0, 5, -8, 12]), Result(min=-8, max=12))


class FindMinMaxTest2(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(findMinMax2([5]), Result(min=5, max=5))

    def test_two_elements(self):
        self.assertEqual(findMinMax2([3, 7]), Result(min=3, max=7))
        self.assertEqual(findMinMax2([7, 3]), Result(min=3, max=7))

    def test_unsorted_list(self):
        self.assertEqual(findMinMax2([4, 1, 9, 2, 7]), Result(min=1, max=9))

    def test_sorted_ascending(self):
        self.assertEqual(findMinMax2([1, 2, 3, 4, 5]), Result(min=1, max=5))

    def test_sorted_descending(self):
        self.assertEqual(findMinMax2([5, 4, 3, 2, 1]), Result(min=1, max=5))

    def test_all_equal(self):
        self.assertEqual(findMinMax2([7, 7, 7]), Result(min=7, max=7))

    def test_negative_numbers(self):
        self.assertEqual(findMinMax2([-5, -1, -10, 3]), Result(min=-10, max=3))

    def test_mixed_positive_and_negative(self):
        self.assertEqual(findMinMax2([-2, 0, 5, -8, 12]), Result(min=-8, max=12))


if __name__ == "__main__":
    unittest.main()