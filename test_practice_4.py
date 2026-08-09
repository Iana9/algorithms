import unittest

from practice4.quick_sort import QuickSort


class QuickSort2Test(unittest.TestCase):
    def sort(self, arr):
        return QuickSort(arr).quick_sort_2()

    def test_empty_list(self):
        self.assertEqual(self.sort([]), [])

    def test_single_element(self):
        self.assertEqual(self.sort([5]), [5])

    def test_two_elements(self):
        self.assertEqual(self.sort([2, 1]), [1, 2])
        self.assertEqual(self.sort([1, 2]), [1, 2])

    def test_unsorted_list(self):
        self.assertEqual(self.sort([3, 6, 8, 10, 1, 2, 1]), [1, 1, 2, 3, 6, 8, 10])

    def test_already_sorted(self):
        self.assertEqual(self.sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(self.sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(self.sort([4, 2, 4, 1, 2, 4]), [1, 2, 2, 4, 4, 4])

    def test_all_equal(self):
        self.assertEqual(self.sort([7, 7, 7, 7]), [7, 7, 7, 7])

    def test_negative_numbers(self):
        self.assertEqual(self.sort([0, -3, 5, -1, 2]), [-3, -1, 0, 2, 5])

    def test_sorts_in_place(self):
        arr = [3, 1, 2]
        qs = QuickSort(arr)
        result = qs.quick_sort_2()
        self.assertIs(result, arr)
        self.assertEqual(arr, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()