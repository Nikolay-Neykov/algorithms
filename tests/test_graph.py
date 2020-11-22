from graph.bfs.graph import Node
from graph.bfs.graph import Graph
from graph.bfs.graph import Vertex
import unittest


class GraphScenarios(unittest.TestCase):

    def test_graph(self):

        node3 = Node(30)
        node4 = Node(40, Vertex(node3, 1))
        node2 = Node(20, Vertex(node3, 1), Vertex(node4, 1))
        node1 = Node(10, Vertex(node2, 1))
        node0 = Node(5, Vertex(node1, 1))

        # node1.add_vertex(node2, node3)

        graph = Graph(node0, node1, node2, node3, node4)
        # print(graph)
        print(graph.topological_sort())

    def test_graph_2(self):
        node1 = Node(10)
        node3 = Node(30, Vertex(node1, 1))
        node2 = Node(20, Vertex(node3, 1))
        node0 = Node(5)
        node4 = Node(40, Vertex(node0, 1), Vertex(node1, 1))
        node5 = Node(50, Vertex(node0, 1), Vertex(node2, 1))

        graph = Graph(node0, node1, node2, node3, node4, node5)
        # print(graph)
        print(graph.topological_sort())

    def test_graph_3(self):
        sofia = Node('Sofia10')
        plovdiv = Node('Plovdiv30', Vertex(sofia, 130))
        pleven = Node('Pleven20', Vertex(plovdiv, 200))
        varna = Node('Varna40', Vertex(pleven, 210), Vertex(sofia, 450))
        burgas = Node('Burgas0', Vertex(varna, 100))
        samokov = Node('Samokov50', Vertex(burgas, 350), Vertex(pleven, 250))

        sofia.add_vertex(Vertex(samokov, 170))

        graph = Graph(burgas, sofia, pleven, plovdiv, varna, samokov)
        # print(graph)
        print(graph.topological_sort())
        print(f'DFS: {graph.dfs(samokov)}')
        print(f'Dijkstra: {graph.dijkstra(varna)}')

    def test_dijkstra(self):
        node6 = Node('6')
        node4 = Node('4', Vertex(node6, 1))
        node5 = Node('5', Vertex(node4, 2), Vertex(node6, 5))
        node3 = Node('3', Vertex(node5, 3))
        node2 = Node('2', Vertex(node3, 1), Vertex(node4, 7))
        node1 = Node('1', Vertex(node2, 2), Vertex(node3, 4))

        graph = Graph(node1, node2, node3, node4, node5, node6)

        print(f'Topological {graph.topological_sort()}')
        print(f'DFS: {graph.dfs(node1)}')
        print(f'Dijkstra: {graph.dijkstra(node1)}')
