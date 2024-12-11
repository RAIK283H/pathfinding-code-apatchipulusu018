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

def floyd_warshall(matrix):
    # Number of vertices in the graph
    n = len(matrix)
    
    # Initialize the distance matrix with infinity
    dist = [[float('inf')] * n for _ in range(n)]
    parent = [[None] * n for _ in range(n)]
    
    # Set the distance from each vertex to itself as 0
    for i in range(n):
        dist[i][i] = 0
        parent[i][i] = i
    
    # Set the distance for edges present in the graph
    for u in range(n):
        for v in range(n):
            if matrix[u][v] != 0:  # Assumes 0 indicates no edge
                dist[u][v] = matrix[u][v]
                parent[u][v] = u 
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    parent[i][j] = parent[k][j]
    
    return dist, parent

def reconstructing_path(u, v, prev):
    # If there is no path, return an empty list
    if prev[u][v] is None:
        return []
    
    path = [v]
    while u != v:
        v = prev[u][v]
        path.insert(0, v)  # Prepend to the path
    return path




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

def main():
    # Example graph data (coordinates and neighbor indices)
    # Each node has a (coordinates, list of neighbors)
    graph = [
        ((0, 0), [1, 2]),  # Node 0 at (0, 0) connects to Node 1 and Node 2
        ((1, 0), [0, 2]),  # Node 1 at (1, 0) connects to Node 0 and Node 2
        ((0, 1), [0, 1])   # Node 2 at (0, 1) connects to Node 0 and Node 1
    ]
    
    # Step 1: Convert the adjacency list to a weighted adjacency matrix
    matrix = adjacency_list_to_matrix_with_weights(graph)
   
    # Step 2: Run the Floyd-Warshall algorithm to get distances and parent matrix
    dist, parent = floyd_warshall(matrix)
    
    # Step 3: Reconstruct the path from a given start (u) to end (v)
    u, v = 0, 2  # Example: Find path from vertex 0 to vertex 2
    path = reconstructing_path(u, v, parent)
    
    # Step 4: Print the results
    print(f"Shortest path from vertex {u} to vertex {v}: {path}")
    print(f"Distance: {dist[u][v]}")

if __name__ == "__main__":
    main()