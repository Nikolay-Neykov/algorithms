from stack.stack import Stack


class Tree():
    def __init__(self, value, *nodes):
        self.value = value
        self.nodes = nodes

    def dfs(self):
        return self.__dfs([])

    def __dfs(self, result):
        for node in self.nodes:
            node.__dfs(result)
        result.append(self.value)
        return result

    def bfs(self):
        return self.__bfs([])

    def __bfs(self, result):
        result.append(self.value)
        for node in self.nodes:
            node.__bfs(result)
        return result

    def dfs_stack(self):
        result = []
        stack = Stack()

        stack.push(self)
        current_node = stack.peek()
        index = 0
        while current_node and index < 8:
            for node in reversed(current_node.nodes):
                stack.push(node)

            current_node = stack.peek()
            if len(current_node.nodes) == 0:
                result.append(current_node.value)
                stack.pop()
                current_node = stack.peek()
            print(result)
            index += 1

    def dfs_in_order_stack(self):
        result = []
        stack = Stack()

        stack.push(self)
        while stack.peek():
            current_node = stack.pop()

            result.append(current_node.value)
            for node in current_node.nodes:
                stack.push(node)

        return result

    def bfs_queue():
        return NotImplementedError

    def __str__(self):
        return f'{self.value} -> {self.nodes}'

    def __repr__(self):
        return self.__str__()
