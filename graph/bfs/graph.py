import sys


class Graph():
    def __init__(self, *nodes):
        self.nodes = dict()
        self.add_nodes(*nodes)

    def add_nodes(self, *nodes):
        for i in range(len(nodes)):
            node = nodes[i]
            node.set_index(len(self.nodes))
            self.nodes[node.index] = node

    def __str__(self):
        return f'{self.nodes}'

    def __repr__(self):
        return self.__str__()

    def dfs(self, node=None):
        order = []
        if node:
            order = node.dfs({}, [])
        else:
            for key in self.nodes:
                order = self.nodes[key].dfs({}, [])
        return order

    def vertex_matrix(self):
        matrix = []
        row = 0
        for i in self.nodes.keys():
            matrix.append(list())
            column = 0
            for k in self.nodes.keys():
                matrix[row].append(list())
                connection_length = self.nodes[i].has_connection(self.nodes[k])
                matrix[row][column] = connection_length
                column += 1
            row += 1
        return matrix

    def dijkstra(self, start_node):
        V = len(self.nodes)
        distances = [sys.maxsize] * V
        distances[start_node.index] = 0
        visited = {}

        while len(visited) < V:
            selected_node = {'value': sys.maxsize}
            for i in range(len(distances)):
                distance = distances[i]
                if distance < selected_node['value'] and i not in visited:
                    selected_node['value'] = distance
                    selected_node['index'] = i
            visited[selected_node['index']] = True

            for vertex in self.nodes[selected_node['index']].vertexes.values():
                new_path = vertex.value + distances[selected_node['index']]
                if new_path < distances[vertex.node.index]:
                    distances[vertex.node.index] = new_path
            # print(distances)

        return distances, visited

    def topological_sort(self):
        order = list()
        matrix = self.vertex_matrix()

        column = -1
        cycle = 0
        while len(order) != len(matrix):
            column += 1
            if column == len(matrix):
                if cycle == len(matrix):
                    break
                    # raise Exception('No node without dependencies is found there is a cycle in the graph')
                column = 0
                cycle += 1

            while column in order:
                column += 1
                if column == len(matrix):
                    column = 0
                    cycle += 1
            dependencies = 0
            for row in range(len(matrix)):
                if row in order:
                    continue
                # print(f'{matrix[row]}')
                dependencies += matrix[row][column]
            # print(f'dependencies of {column} are {dependencies}')
            if dependencies == 0:
                order.append(column)
                cycle = 0

        return [self.nodes[index] for index in order]

    # def delete_column(self, matrix, column):
    #     for row in matrix:
    #         row.remove(column)


class Vertex():
    def __init__(self, node, value=0):
        self.value = value
        self.node = node


class Node():
    def __init__(self, value, *vertexes):
        self.value = value
        self.vertexes = {}
        self.add_vertex(*vertexes)

    def set_index(self, index):
        self.index = index

    def add_vertex(self, *vertexes):
        for i in range(len(vertexes)):
            vertex = vertexes[i]
            self.vertexes[vertex.node.value] = vertex

    def get_vertex(self, value):
        return self.vertexes[value]

    def has_connection(self, node):
        if node.value in self.vertexes:
            return self.vertexes[node.value].value

        return 0

    def dfs(self, visited, order):
        if self.value not in visited:
            visited[self.value] = True
            for adjacent in self.vertexes:
                self.vertexes[adjacent].node.dfs(visited, order)
            order.append(self.value)

            return order

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return self.__str__()
