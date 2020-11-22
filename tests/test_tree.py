from tree.tree import Tree as Tree
import unittest


class BFSScenarios(unittest.TestCase):
    pass
    # def test_tree_dfs(self):
    #     tree = Tree(1, Tree(2, Tree(3), Tree(4)), Tree(5, Tree(6), Tree(7)))
    #     expected_result = [3, 4, 2, 6, 7, 5, 1]

    #     print(tree.dfs())
    #     self.assertEqual(tree.dfs(), expected_result)

    # def test_tree_bfs(self):
    #     tree = Tree(1, Tree(2, Tree(3), Tree(4)), Tree(5, Tree(6), Tree(7)))
    #     expected_result = [1, 2, 3, 4, 5, 6, 7]

    #     print(tree.bfs())
    #     self.assertEqual(tree.bfs(), expected_result)

    # def test_tree_stack(self):
    #     tree = Tree(1, Tree(2, Tree(3), Tree(4)), Tree(5, Tree(6), Tree(7)))
    #     expected_result = [3, 4, 2, 6, 7, 5, 1]

    #     result = tree.dfs_stack()
    #     print(result)
    #     self.assertEqual(result, expected_result)

    # def test_tree_inorder_stack(self):
    #     tree = Tree(1, Tree(2, Tree(3), Tree(4)), Tree(5, Tree(6), Tree(7)))
    #     expected_result = [1, 2, 3, 4, 5, 6, 7]

    #     result = tree.dfs_in_order_stack()
    #     print(result)
    #     self.assertEqual(result, expected_result)

    # def test_tree_queue(self):
    #     tree = Tree(1, Tree(2, Tree(3), Tree(4)), Tree(5, Tree(6), Tree(7)))

    #     print(tree.dfs_stack())
    #     self.assertEqual(sum(dfs), 28)
    #     self.assertEqual(sum(bfs), 28)
