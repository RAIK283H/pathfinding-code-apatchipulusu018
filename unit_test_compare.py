import math
import unittest
from f_w import FWSlidesAlgorithm, adjacency_list_to_matrix_with_weights, distance_weight
from pathing import find_dijkstra_path, get_middle_path
from collections import deque
from pathing import get_dfs_path
from pathing import get_bfs_path
from permutation import stepOne
from permutation import findLargestMobileVariable
from permutation import StepThreeSwap
from permutation import StepFourSwitch
from permutation import allPermutations


class TestCompare(unittest.TestCase):

   def test_floyd_and_dijkstra_same_paths():
    # Example graph in adjacency list format
    graph = [
        ((0, 0), [1, 2]),         # Node 0 connects to Node 1 and Node 2
        ((1, 0), [0, 2, 3]),      # Node 1 connects to Node 0, Node 2, and Node 3
        ((0, 1), [0, 1, 3]),      # Node 2 connects to Node 0, Node 1, and Node 3
        ((1, 1), [1, 2])          # Node 3 connects to Node 1 and Node 2
    ]
    
    # Generate the adjacency matrix with weights
    matrix = adjacency_list_to_matrix_with_weights(graph)

    # Run Floyd-Warshall Algorithm
    floyd_distances, _ = FWSlidesAlgorithm(matrix)

    # Run Dijkstra for each node as the start node
    dijkstra_distances = []
    for start_node in range(len(graph)):
        predecessors = find_dijkstra_path(graph, start_node, None)
        distances = [math.inf] * len(graph)
        for node, pred in predecessors.items():
            if pred is not None or node == start_node:  # Dijkstra initializes the start node itself
                distances[node] = distance_weight(graph, pred, node) if pred is not None else 0
        dijkstra_distances.append(distances)

    # Verify that Floyd-Warshall and Dijkstra distances are the same
    for i in range(len(graph)):
        for j in range(len(graph)):
            assert math.isclose(floyd_distances[i][j], dijkstra_distances[i][j], rel_tol=1e-9), \
                f"Mismatch in shortest path from {i} to {j}: Floyd-Warshall={floyd_distances[i][j]}, Dijkstra={dijkstra_distances[i][j]}"

    print("Floyd-Warshall and Dijkstra's shortest paths are consistent!")




if __name__ == '__main__':
    unittest.main()
