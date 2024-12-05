import math
import config_data
import global_game_data
import graph_data

#unit tests for this algorithm are all at the bottom of unit_test.py

def FWSlidesAlgorithm(matrix):
    
    vertices = len(matrix)

    #making copy of array
    dist = []
    for i in range(vertices):
        row = []
        for j in range(vertices):
            row.append(matrix[i][j])
        dist.append(row)
    
    parent = [[None if matrix[i][j] == float('inf') else i for j in range(vertices)] for i in range(vertices)]

    for k in range(vertices):
        for i in range(vertices): #start
            for j in range(vertices): #end
                
                #dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    parent[i][j] = parent[k][j]

    return dist, parent

def reconstruct_path(parent, u, v):
    if parent[u][v] is None:
        return None  # No path exists
    path = [u]
    while u != v:
        u = parent[u][v]
        path.append(u)
    return path


def FWBonus(graph):
    arg = 5

    return arg

def distance_weight(graph, u,v):
    assert 0 <= u < len(graph), f"Node {u} is out of range for the graph."
    assert 0 <= v < len(graph), f"Node {v} is out of range for the graph."


    x1,y1 = graph[u][0]
    x2,y2 = graph[v][0]
    return math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)

def adjacency_list_to_matrix_with_weights(graph):
    n = len(graph)
    # Initialize the matrix with 'inf' for no edges and 0 for the diagonal
    matrix = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 0 

    for node_index, (coords, neighbors) in enumerate(graph):
        for neighbor in neighbors:
            # Calculate the distance weight for the edge
            weight = distance_weight(graph, node_index, neighbor)
            matrix[node_index][neighbor] = weight

    return matrix