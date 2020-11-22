from heap.heap import Heap
import unittest


class HeapScenarios(unittest.TestCase):

    def test_max_heap(self):
        arr = [5, 1, 6, 9, 72, 42, 51]
        heap = Heap(Heap.Type.MAX, arr.copy())

        arr.sort()

        for i in range(len(arr)-1, -1, -1):
            expected = arr[i]
            actual = heap.pop()
            # print(f'expected: {expected}, actual: {actual}')
            self.assertEqual(expected, actual)

    def test_min_heap(self):
        arr = [5, 1, 6, 9, 72, 42, 51]
        heap = Heap(Heap.Type.MIN, arr.copy())

        arr.sort()

        for i in range(0, len(arr)):
            expected = arr[i]
            actual = heap.pop()
            # print(f'expected: {expected}, actual: {actual}')
            self.assertEqual(expected, actual)
