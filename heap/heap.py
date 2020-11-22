from enum import Enum


class Heap():
    class Type(Enum):
        MIN = 'min'
        MAX = 'max'

    def __init__(self, condition, elements=[]):
        self.condition = condition
        self.elements = elements
        if len(elements) > 0:
            self.heapify()

    def push(self, value):
        self.elements.append(value)
        self.heapify()

    def pop(self):
        current_best = self.elements[0]
        last_index = len(self.elements)-1

        self.swap(0, last_index)
        self.delete(last_index)
        self.heapify()

        return current_best

    def swap(self, first, second):
        self.elements[first], self.elements[second] = self.elements[second], self.elements[first]

    def delete(self, index):
        self.elements.pop(index)

    def decreaseKey(self, key):
        pass

    def heapify(self):
        n = len(self.elements)

        for i in range(n//2 - 1, -1, -1):
            self.__heapify(self.elements, n, i)
        #print(f'heapified: {self}')

    def __heapify(self, arr, n, current):
        best = current
        left = 2 * current + 1   # left = 2*i + 1
        right = 2 * current + 2  # right = 2*i + 2

        # See if left child exists and is better
        if left < n:
            if self.condition is Heap.Type.MIN and arr[best] > arr[left]:
                best = left
            elif self.condition is Heap.Type.MAX and arr[best] < arr[left]:
                best = left

        # See if right child exists and is better
        if right < n:
            if self.condition is Heap.Type.MIN and arr[best] > arr[right]:
                best = right
            elif self.condition is Heap.Type.MAX and arr[best] < arr[right]:
                best = right

        if best != current:
            self.swap(current, best)

            # Heapify downwards.
            self.__heapify(arr, n, best)

    def __print(self, level, index):
        indent = level * "\t"
        elements_count = len(self.elements)

        output = f'\n{indent}{self.elements[index]}'

        right = 2 * index + 2     # right = 2*i + 2
        if right < elements_count:
            output += self.__print(level + 1, right)
        left = 2 * index + 1     # left = 2*i + 1
        if left < elements_count:
            output += self.__print(level + 1, left)

        return output

    def __str__(self):
        if len(self.elements) > 0:
            return self.__print(0, 0)
        else:
            return str([])
