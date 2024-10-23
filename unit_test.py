import math
import unittest
from pathing import get_middle_path
from collections import deque
from pathing import get_dfs_path
from pathing import get_bfs_path


class TestPathFinding(unittest.TestCase):

    def setUp(self):
        self.graph = [
            [(0, 0), [1, 2]],
            [(100, 0), [0, 3]],
            [(0, 100), [0, 4]],
            [(200, 0), [1, 5]],
            [(100, 100), [2, 6]],
            [(300, 0), [3, 7]],
            [(200, 100), [4, 8]],
            [(400, 0), [5, 9]],
            [(300, 100), [6, 9]],
            [(500, 0), [7, 8]]
        ]

        global global_game_data
        global graph_data
        global_game_data = type('obj', 
                                 (object,), 
                                 {'current_graph_index': 0, 
                                  'target_node': [4]})()  # Let's assume the target node is 4
        graph_data = type('obj', (object,), {'graph_data': [self.graph]})()  # Use the sample graph

    
    def test_pathfinding_start_to_end(self):
        path = get_middle_path(self.graph, 0, 9)
        self.assertEqual(path[0], 0, "Path should start at index 0")
        self.assertEqual(path[-1], 9, "Path should end at index 9")

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)

    def test_dfs_path_start_to_end(self):
        path = get_dfs_path()  # Call the DFS function
        print(f"DFS Path: {path}")
        self.assertEqual(path[0], 0, "Path should start at index 0")  # Check start
        self.assertEqual(path[-1], 9, "Path should end at index 9")  # Check end

    def test_dfs_path_connected_edges(self):
        path = get_dfs_path()
        for i in range(len(path) - 1):
            current_node = path[i]
            next_node = path[i + 1]
            adjacent_list = self.graph[current_node][1]
            self.assertIn(next_node, adjacent_list, 
                          f"Nodes {current_node} and {next_node} are not connected by an edge.")
            

    def test_bfs_path_includes_target(self):
        path = get_bfs_path()
        target_node = global_game_data.target_node[global_game_data.current_graph_index]
        self.assertIn(target_node, path, f"Path should include the target node {target_node}.")

    def test_bfs_path_start_to_end(self):
        path = get_bfs_path()  # Call the BFS function
        print(f"BFS Path: {path}")
        self.assertEqual(path[0], 0, "Path should start at index 0")  # Check start
        self.assertEqual(path[-1], 9, "Path should end at index 9")  # Check end



if __name__ == '__main__':
    unittest.main()
