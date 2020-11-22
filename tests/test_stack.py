from stack.stack import Stack as Stack
import unittest


class StackScenarios(unittest.TestCase):

    def test_stack(self):
        elements = [5, 1, 6, 9, 72, 42, 51]
        expected_result = elements.copy()
        expected_result.reverse()
        stack = Stack()

        for element in elements:
            stack.push(element)

        actual_result = []
        while stack.peek():
            actual_result.append(stack.pop())

        self.assertEqual(expected_result, actual_result)
