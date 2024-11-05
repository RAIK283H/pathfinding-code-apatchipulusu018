'''
graph_data[a] = gives you graph at index a
graph_data[a][0] = start node of graph a
graph_data[a][length-1] = exit node of graph a
graph_data[a][b][0] = x-y coordinates as tuple of point b in graph a
graph_data[a][b][1] = adjacency list of point b in graph a

Only the start and exit nodes are dead ends (all other nodes have degree >= 2)
'''


graph_data = [
    # Graph 0: Tree Does not exist
    [
        [(0, 0), [1, 2]],        # Node 0 (start)
        [(100, 0), [0, 3]],      # Node 1
        [(50, 100), [0, 4]],     # Node 2
        [(100, 100), [1]],       # Node 3 (dead end)
        [(150, 100), [2]]        # Node 4 (dead end)
    ],

    # Graph 1: Exists
    [
        [(0, 0), [1, 2, 3]],     # Node 0 (start)
        [(0, 100), [0, 2, 4]],   # Node 1
        [(100, 100), [1, 0, 3]],  # Node 2
        [(100, 0), [0, 2, 4]],    # Node 3
        [(50, 50), [1, 3]]        # Node 4 (exit)
    ],

    # Graph 2: Hamiltonian cycle exists
    [
        [(0, 0), [1, 2]],        # Node 0 (start)
        [(100, 0), [0, 2, 3]],  # Node 1
        [(50, 100), [0, 1, 3]],  # Node 2
        [(100, 100), [1, 2]],    # Node 3
        [(150, 0), [2]]          # Node 4 (exit)
    ],

    # Graph 3: No Hamiltonian cycle exists
    [
        [(0, 0), [1, 2, 3]],      # Node 0 (start)
        [(100, 0), [0, 2, 4]],    # Node 1
        [(50, 100), [0, 1, 5]],    # Node 2
        [(100, 100), [0, 5, 6]],   # Node 3
        [(200, 0), [1, 6]],        # Node 4
        [(150, 150), [2, 3]],      # Node 5
        [(250, 50), [3, 4]]        # Node 6 (exit)
    ],

    # Graph 4: No Hamiltonian cycle (tree structure)
    [
        [(0, 0), [1, 2]],          # Node 0 (start)
        [(100, 0), [0, 3]],        # Node 1
        [(50, 100), [0, 4]],       # Node 2
        [(100, 100), [1, 5]],      # Node 3
        [(150, 100), [2]],         # Node 4 (dead end)
        [(100, 200), [3, 6]],      # Node 5
        [(200, 200), [5]]           # Node 6 (dead end)
    ],
    #Graph 5: Does have a hamiltonian cycle
    [
        [(0, 0), [1, 2]],        # Node 0 (start)
        [(100, 0), [0, 2, 3]],   # Node 1
        [(50, 100), [0, 1, 4]],   # Node 2
        [(100, 100), [1, 4, 5]],  # Node 3
        [(200, 0), [2, 3, 6]],    # Node 4
        [(150, 150), [3, 4, 6]],  # Node 5
        [(250, 100), [4, 5]]      # Node 6 (exit)
    ]

]

test_path = [
    [0, 1, 3, 6, 9, 11],
    [0, 2, 4, 6, 8, 10, 11],
    [0, 1, 3, 5, 7, 9, 11],
    [1, 2],
    [1, 2, 3],
    [22, 3, 11, 17, 18, 23],
    [1, 5, 6, 10, 11, 15],
    [1, 2, 5, 8, 9, 10],
    [1, 14, 5, 6, 9, 15],
]
