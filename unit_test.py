import math
import unittest
from f_w import FWSlidesAlgorithm, adjacency_list_to_matrix_with_weights, floyd_warshall
from pathing import get_middle_path
from collections import deque
from pathing import get_dfs_path
from pathing import get_bfs_path
from f_w import reconstructing_path
from pathing import distance_weight
from pathing import find_dijkstra_path
from pathing import reconstruct_path


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
        self.matrix = [
            [0, 3, float('inf')],
            [float('inf'), 0, 1],
            [4, float('inf'), 0]
        ]
        
        # Expected shortest path distances
        self.expected_dist = [
            [0, 3, 4],
            [5, 0, 1],
            [4, 7, 0]
        ]
        
        # Expected parent matrix
        self.expected_parent = [
            [0, 0, 1],
            [2, 1, 1],
            [2, 0, 2]
        ]

        self.parent1 = [
            [0, 0, 1],
            [2, 1, 1],
            [2, 0, 2]
        ]

        self.matrix2 = [
            [0, 1, float('inf'), float('inf')],
            [float('inf'), 0, -2, float('inf')],
            [float('inf'), float('inf'), 0, 2],
            [-1, float('inf'), float('inf'), 0]
        ]
        self.expected_dist2 = [
            [0, 1, -1, 1],
            [float('inf'), 0, -2, 0],
            [-1, 0, 0, 2],
            [-1, 0, -2, 0]
        ]
        self.expected_parent2 = [
            [0, 0, 1, 2],
            [None, 1, 1, 2],
            [3, 3, 2, 2],
            [3, 3, 1, 3]
        ]
        self.prev = [
            [None, 0, 0, 2],
            [None, None, 1, 2],
            [None, None, None, 2],
            [None, None, None, None]
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

    # def test_dfs_path_start_to_end(self):
    #     path = get_dfs_path()  # Call the DFS function
    #     print(f"DFS Path: {path}")
    #     self.assertEqual(path[0], 0, "Path should start at index 0")  # Check start
    #     self.assertEqual(path[-1], 9, "Path should end at index 9")  # Check end

    # def test_dfs_path_connected_edges(self):
    #     path = get_dfs_path()
    #     for i in range(len(path) - 1):
    #         current_node = path[i]
    #         next_node = path[i + 1]
    #         adjacent_list = self.graph[current_node][1]
    #         self.assertIn(next_node, adjacent_list, 
    #                       f"Nodes {current_node} and {next_node} are not connected by an edge.")
            

    # def test_bfs_path_includes_target(self):
    #     path = get_bfs_path()
    #     target_node = global_game_data.target_node[global_game_data.current_graph_index]
    #     self.assertIn(target_node, path, f"Path should include the target node {target_node}.")

    # def test_bfs_path_start_to_end(self):
    #     path = get_bfs_path()  # Call the BFS function
    #     print(f"BFS Path: {path}")
    #     self.assertEqual(path[0], 0, "Path should start at index 0")  # Check start
    #     self.assertEqual(path[-1], 9, "Path should end at index 9")  # Check end


    # These are my dikstras tests

    def test_reconstruct_path(self):
        # Test case 1: Normal case where path is successfully reconstructed
        predecessor_map = {1: 0, 2: 1, 3: 2, 4: 3}  # Sample predecessor map
        startV = 0
        exitV = 4
        expected_path = [0, 1, 2, 3, 4]
        result = reconstruct_path(predecessor_map, startV, exitV)
        self.assertEqual(result, expected_path)

    def test_distance(self):
        # Test case 1: Normal case with two nodes having valid coordinates
        graph = [((0, 0),), ((3, 4),)]  # Example graph with two nodes at (0, 0) and (3, 4)
        u, v = 0, 1
        expected_distance = 5.0  # Distance between (0, 0) and (3, 4) is 5 (Pythagorean theorem)
        result = distance_weight(graph, u, v)
        self.assertEqual(result, expected_distance)

    def test_dijkstra_path_basic(self):
        # Simple test case: 3 nodes with direct edges
        graph = [
            ((0, 0), [1, 2]),  # Node 0 connects to Node 1 and 2
            ((3, 4), [2]),      # Node 1 connects to Node 2
            ((6, 8), []),       # Node 2 has no neighbors
        ]
        start = 0
        end = 2
        expected_predecessors = {0: None, 1: 0, 2: 0}
        result = find_dijkstra_path(graph, start, end)
        self.assertEqual(result, expected_predecessors)

    def test_dijkstra_path_three_nodes(self):
        # Case with three nodes where nodes are connected in a simple linear way
        graph = [
            ((0, 0), [1]),  # Node 0 connects to Node 1
            ((3, 4), [2]),  # Node 1 connects to Node 2
            ((6, 8), []),    # Node 2 has no neighbors
        ]
        start = 0
        end = 2
        expected_predecessors = {0: None, 1: 0, 2: 1}
        result = find_dijkstra_path(graph, start, end)
        self.assertEqual(result, expected_predecessors)

    def test_dijkstra_path_four_nodes(self):
        # A graph with 4 nodes and direct connections between nodes
        graph = [
            ((0, 0), [1]),  # Node 0 connects to Node 1
            ((3, 4), [2]),  # Node 1 connects to Node 2
            ((6, 8), [3]),  # Node 2 connects to Node 3
            ((9, 12), []),   # Node 3 has no neighbors
        ]
        start = 0
        end = 3
        expected_predecessors = {0: None, 1: 0, 2: 1, 3: 2}
        result = find_dijkstra_path(graph, start, end)
        self.assertEqual(result, expected_predecessors)


###THE FOLLOWING TESTS ARE TESTING FLOYD-WARSHALL
    def test_adjacency_list_to_matrix_with_weights(self):
        # Test graph: Small example with known distances
        test_graph = [
            [(0, 0), [1, 2]],
            [(3, 0), [0, 3]],
            [(0, 4), [0]],
            [(3, 4), [1]]
        ]
        
        # Expected adjacency matrix (rounded for clarity)
        expected_matrix = [
            [0, 3.0, 4.0, float('inf')],
            [3.0, 0, float('inf'), 4.0],
            [4.0, float('inf'), 0, float('inf')],
            [float('inf'), 4.0, float('inf'), 0]
        ]
        
        # Get the adjacency matrix from the function
        actual_matrix = adjacency_list_to_matrix_with_weights(test_graph)
        
        # Check the values
        for i in range(len(expected_matrix)):
            for j in range(len(expected_matrix)):
                if expected_matrix[i][j] == float('inf'):
                    self.assertTrue(math.isinf(actual_matrix[i][j]), f"Expected infinity at ({i}, {j})")
                else:
                    self.assertAlmostEqual(
                        actual_matrix[i][j],
                        expected_matrix[i][j],
                        places=2,
                        msg=f"Value mismatch at ({i}, {j}): expected {expected_matrix[i][j]}, got {actual_matrix[i][j]}"
                    )

    def test_fwslides_algorithm(self):
        # Run the FWSlidesAlgorithm
        dist, parent = FWSlidesAlgorithm(self.matrix)
        
        # Test that the distance matrix is correct
        for i in range(len(self.expected_dist)):
            for j in range(len(self.expected_dist)):
                if self.expected_dist[i][j] == float('inf'):
                    self.assertTrue(math.isinf(dist[i][j]), f"Expected infinity at ({i}, {j})")
                else:
                    self.assertAlmostEqual(dist[i][j], self.expected_dist[i][j], places=2, 
                                           msg=f"Distance mismatch at ({i}, {j})")
        
        # Test that the parent matrix is correct
        for i in range(len(self.expected_parent)):
            for j in range(len(self.expected_parent)):
                self.assertEqual(parent[i][j], self.expected_parent[i][j], 
                                 f"Parent mismatch at ({i}, {j})")
    def test_fwslides_algorithm2(self):
        """Test the Floyd-Warshall implementation."""
        dist, parent = FWSlidesAlgorithm(self.matrix)
        
        # Assert distance matrix
        self.assertEqual(dist, self.expected_dist, "Distance matrix is incorrect.")
        
        # Assert parent matrix
        self.assertEqual(parent, self.expected_parent, "Parent matrix is incorrect.")

    def test_single_path(self):
        # Graph: 0 → 1 → 2
        matrix = [
            [0, 3, 0],
            [0, 0, 4],
            [0, 0, 0]
        ]
        dist, parent = floyd_warshall(matrix)
        
        # Check shortest path distances
        self.assertEqual(dist[0][1], 3)  # Distance from 0 to 1
        self.assertEqual(dist[1][2], 4)  # Distance from 1 to 2
        self.assertEqual(dist[0][2], 7)  # Distance from 0 to 2
        
        # Check if the parent matrix reflects the correct path
        self.assertEqual(parent[0][1], 0)  # Parent of 1 is 0
        self.assertEqual(parent[1][2], 1)  # Parent of 2 is 1

    def test_multiple_paths(self):
        # Graph with multiple paths
        matrix = [
            [0, 3, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 7],
            [0, 0, 0, 0]
        ]
        dist, parent = floyd_warshall(matrix)
        
        # Check shortest path distances
        self.assertEqual(dist[0][2], 4)  # Path from 0 → 1 → 2
        self.assertEqual(dist[0][3], 11) # Path from 0 → 1 → 2 → 3
        
        # Check if the parent matrix reflects the correct paths
        self.assertEqual(parent[0][2], 1)  # Parent of 2 is 1
        self.assertEqual(parent[0][3], 2)  # Parent of 3 is 2

    
    # def test_reconstruct_path(self):
    #     # Example parent matrix that might be generated by Floyd-Warshall
    #     parent = {
    #         0: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
    #         1: {2: 1, 3: 1, 4: 1, 5: 1},
    #         2: {3: 2, 4: 2, 5: 2},
    #         3: {4: 3, 5: 3},
    #         4: {5: 4},
    #         5: {}
    #     }
        
    #     # Test 1: Path from vertex 0 to vertex 5 (should return [0, 1, 2, 5])
    #     result = reconstruct_path(parent, 0, 5)
    #     self.assertEqual(result, [0, 1, 2, 5])

    #     # Test 2: Path from vertex 1 to vertex 4 (should return [1, 2, 4])
    #     result = reconstruct_path(parent, 1, 4)
    #     self.assertEqual(result, [1, 2, 4])

    #     # Test 3: Path from vertex 2 to vertex 3 (should return [2, 3])
    #     result = reconstruct_path(parent, 2, 3)
    #     self.assertEqual(result, [2, 3])

    #     # Test 4: Path from vertex 0 to vertex 4 (should return [0, 1, 2, 4])
    #     result = reconstruct_path(parent, 0, 4)
    #     self.assertEqual(result, [0, 1, 2, 4])

    #     # Test 5: Path from vertex 5 to vertex 5 (should return [5] because it's the same vertex)
    #     result = reconstruct_path(parent, 5, 5)
    #     self.assertEqual(result, [5])

    #     # Test 6: No path between 4 and 1 (should return None because there's no path)
    #     result = reconstruct_path(parent, 4, 1)
    #     self.assertEqual(result, None)

    def test_reconstruct_path_0_to_3(self):
        # Test path reconstruction from vertex 0 to 3
        path = reconstructing_path(0, 3, self.prev)
        self.assertEqual(path, [0, 2, 3])  # Expected path

    # def test_reconstruct_path_same_start_and_end(self):
    #     # Test path reconstruction when the start and end vertex are the same
    #     path = reconstruct_path(2, 2, self.prev)
    #     self.assertEqual(path, [2])  # Path should only contain the vertex itself


    
    
if __name__ == '__main__':
    unittest.main()
