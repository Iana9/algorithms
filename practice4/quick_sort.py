class QuickSort:
    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr)

    def quick_sort(self):
        if self.length <= 1:
            return self.arr
        else:
            pivot = self.arr[self.length // 2]
            left = [x for x in self.arr if x < pivot]
            middle = [x for x in self.arr if x == pivot]
            right = [x for x in self.arr if x > pivot]
            return self.quick_sort(left) + middle + self.quick_sort(right)

    def quick_sort_2(self):
        stack = [(0, self.length - 1)]
        while stack:
            start, end = stack.pop()
            if start >= end:
                continue

            left, right = start, end
            pivot = self.arr[(left + right) // 2]
            while left <= right:
                while self.arr[left] < pivot:
                    left += 1
                while self.arr[right] > pivot:
                    right -= 1
                if left <= right:
                    self.arr[left], self.arr[right] = self.arr[right], self.arr[left]
                    left += 1
                    right -= 1

            stack.append((start, right))
            stack.append((left, end))
        return self.arr