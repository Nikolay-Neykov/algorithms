class Tree():
    def __init__(self, value=None):
        self.value = value
        self.children = set()

    def add(self, node, child):
        if not self.value:
            self.value = node
        if self.value == node:
            self.children.add(Tree(child))
        else:
            for curr_child in self.children:
                curr_child.add(node, child)

    def __hash__(self):
        # TODO check if value is None
        return self.value.__hash__()

    def __eq__(self, other):
        return self.value == other.value

    def __print(self, level):
        indent = level * '\t'
        result = f'\n{indent}{self.value}'
        for child in self.children:
            result += child.__print(level + 1)

        return result

    def __str__(self):
        return self.__print(0)


class Vertex():
    def __init__(self, from_node, to_node, value):
        self.from_node = from_node
        self.to_node = to_node
        self.value = value

    def __str__(self):
        return f'from: {self.from_node}, to: {self.to_node}, value:{self.value}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value


class Graph():
    def __init__(self, matrix):
        self.matrix = matrix
        self.vertexes = self.collect_vertexes(matrix)

    def collect_vertexes(self, matrix):
        vertexes = []
        n = len(matrix)

        for x in range(n):
            for y in range(n):
                value = matrix[x][y]
                if value:
                    vertexes.append(Vertex(x, y, value))
        vertexes.sort()
        return vertexes

    def prim(self):
        tree = Tree()
        print(self.vertexes)
        for vertex in self.vertexes:
            tree.add(vertex.from_node, vertex.to_node)
        return tree


matrix = [[0, 0, 0, 0],
          [10, 0, 0, 0],
          [6, 0, 0, 0],
          [5, 15, 4, 0]]

result = Graph(matrix).prim()
if not result:
    raise Exception('common case failed')

print(result)
