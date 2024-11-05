from graph_data_hamiltonian import graph_data
from permutation import allPermutations

def has_hamiltonian_cycle(graph):
    start_node = 0
    end_node = len(graph) - 1
    stack = [(start_node, set([start_node]), 0)]  # (current_node, visited, path_length)

    while stack:
        current_node, visited, path_length = stack.pop()

        # If we've visited all nodes from 1 to n-1, check if we can return to start
        if path_length == end_node - 1 and start_node in graph[current_node][1]:
            return True

        # Try visiting each neighbor of the current node
        for neighbor in graph[current_node][1]:
            if neighbor != start_node and neighbor != end_node and neighbor not in visited:
                # Add neighbor to visited nodes and push the new state onto the stack
                new_visited = visited | {neighbor}
                stack.append((neighbor, new_visited, path_length + 1))

    return False

    
def find_hamiltonian_cycles(graph):
    num_nodes = len(graph) - 2  # exclude start (0) and exit (n)
    hamiltonian_cycles = []

    # Generate permutations for nodes 1 to n-1
    for perm in allPermutations(num_nodes):
        # Create the path from the permutation
        path = [0] + list(perm) + [len(graph) - 1]
        
        # Check if the path is a Hamiltonian cycle
        if is_hamiltonian_cycle(graph, path):
            hamiltonian_cycles.append(path)

    return hamiltonian_cycles


def is_hamiltonian_cycle(graph, path):
    # Check if the path visits each node exactly once (excluding start and end) and returns to start
    visited = set(path[:-1])  # Exclude the exit node
    if len(visited) != len(path) - 2:  # Exclude start and exit
        return False
    # Check if path connects correctly (adjacency)
    for i in range(len(path) - 1):
        if path[i + 1] not in graph[path[i]][1]:
            return False
    return True

#graph = graph_data[1]

for index, graph in enumerate(graph_data):
    print(f"Checking graph {index}:")

    if has_hamiltonian_cycle(graph):
        print(f"Graph {index} has a Hamiltonian cycle.")
        hamiltonian_cycles = find_hamiltonian_cycles(graph)
        print(f"Hamiltonian cycles in graph {index}: {hamiltonian_cycles}")
    else:
        print(f"Graph {index} does not have a Hamiltonian cycle.")

#print(has_hamiltonian_cycle(graph))
#print(find_hamiltonian_cycles(graph))