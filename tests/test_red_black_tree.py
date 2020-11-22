from tree.red_black_tree import Tree as Tree
import unittest


class RedBlackTreeTest(unittest.TestCase):
    def test_red_black_tree_auto_balancing(self):
        # numbers = [1, 2, 3, 4, 5, 6, 7]
        # tree = Tree()
        # for number in numbers:
        #     tree.add(number)
        #numbers = [7, 3, 18, 10, 11, 22, 26, 8]
        numbers = [7, 3, 18, 10, 11, 22, 26, 8, 2, 6, 13]
        tree = Tree()
        for number in numbers:
            tree.add(number)
            # print(tree)
        print(tree)
        # tree.add(2)
        # print(tree)
        # tree.add(6)
        # print(tree)
        # tree.add(13)
        # print(tree)
        # ten = tree.get(10)
        # print(ten)
