from enum import Enum
from termcolor import colored


class Color(Enum):
    RED = 'red'
    BLACK = 'white'


class Tree():
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            self.root.color = Color.BLACK
            return
        else:
            new_node = self.root.add(value)
            self.fixViolation(new_node)

    def check_coloring(self, new_node):
        if not new_node.get_grand_parent():
            return
        if new_node.parent.color is Color.RED and new_node.get_uncle().color is Color.RED:
            self.push_blackness_down_from_grandparent(new_node.get_grand_parent(), new_node.get_uncle())
        return

    def push_blackness_down_from_grandparent(self, grandparent):
        grandparent.color = Color.RED
        grandparent.left_node.color = Color.BLACK
        grandparent.right_node.color = Color.BLACK

    def swap(self, parent_node, grandparent_node):
        parent_color = parent_node.color
        parent_node.color = grandparent_node.color
        grandparent_node.color = parent_color

    def rotateLeft(self, node):
        right_child = node.right_node
        node.right_node = right_child.left_node
        if node.right_node:
            node.right_node.parent = node
        right_child.parent = node.parent
        if not node.parent:
            self.root = right_child
        elif node == node.parent.left_node:
            node.parent.left_node = right_child
        else:
            node.parent.right_node = right_child
        right_child.left_node = node
        node.parent = right_child

    def rotateRight(self, node):
        left_child = node.left_node
        node.left_node = left_child.right_node
        if node.left_node:
            node.left_node.parent = node
        left_child.parent = node.parent
        if not node.parent:
            self.root = left_child
        elif node == node.parent.left_node:
            node.parent.left_node = left_child
        else:
            node.parent.right_node = left_child
        left_child.right_node = node
        node.parent = left_child

    def fixViolation(self, node):
        while node != self.root and node.color != Color.BLACK and node.parent.color == Color.RED:
            parent = node.parent
            grand_parent = node.get_grand_parent()
            uncle = node.get_uncle()
            # Case: A Parent of node is left child of Grand-parent of node
            if parent == grand_parent.left_node:
                # Case: 1 The uncle of node is also red Only Recoloring required
                if uncle and uncle.color == Color.RED:
                    self.push_blackness_down_from_grandparent(grand_parent)
                    node = grand_parent
                else:
                    # Case: 2 node is right child of its parent Left-rotation required
                    if node == parent.right_node:
                        self.rotateLeft(parent)
                        node = parent
                        parent = node.parent
                    # Case: 3 node is left child of its parent Right-rotation required
                    self.rotateRight(grand_parent)
                    self.swap(parent, grand_parent)
                    node = parent
            # Case: B Parent of node is right child of Grand-parent of node
            else:
                # Case: 1 The uncle of node is also red Only Recoloring required
                if uncle and uncle.color == Color.RED:
                    self.push_blackness_down_from_grandparent(grand_parent)
                    node = grand_parent
                else:
                    # Case: 2 node is left child of its parent Right-rotation required
                    if node == parent.left_node:
                        self.rotateRight(parent)
                        node = parent
                        parent = node.parent
                    # Case: 3 node is right child of its parent Left-rotation required
                    self.rotateLeft(grand_parent)
                    self.swap(parent, grand_parent)
                    node = parent
        self.root.color = Color.BLACK

    def get(self, value):
        return self.root.get(value)

    def __str__(self):
        return self.root.__str__()


class Node():
    def __init__(self, value=None, parent=None):
        self.parent = parent
        self.value = value
        self.left_node = None
        self.right_node = None
        self.color = Color.RED

    def get_grand_parent(self):
        return self.parent.parent if self.parent else None

    def get_uncle(self):
        grand_parent = self.get_grand_parent()
        return grand_parent.left_node if grand_parent.left_node != self.parent else grand_parent.right_node

    def add(self, value):
        if value < self.value:
            if not self.left_node:
                self.left_node = Node(value, self)
                return self.left_node
            return self.left_node.add(value)
        else:
            if not self.right_node:
                self.right_node = Node(value, self)
                return self.right_node
            return self.right_node.add(value)

    def get(self, value):
        if value == self.value:
            return self
        elif value < self.value:
            return self.left_node.get(value)
        else:
            return self.right_node.get(value)

    def print_node(self, level):
        indent = level * "\t"
        value = f'{self.parent.value}-{self.value}' if self.parent else f'{self.value}'
        output = f'\n{indent}{colored(value, self.color.value)}'
        if self.right_node:
            output += self.right_node.print_node(level + 1)
        if self.left_node:
            output += self.left_node.print_node(level + 1)
        return output

    def __str__(self):
        return self.print_node(0)

    def __repr__(self):
        return self.__str__()
