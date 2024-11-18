import math
import graph_data
import global_game_data
from numpy import random
from collections import deque
import heapq

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    #global_game_data.graph_paths.append(get_random_path())
    #global_game_data.graph_paths.append(get_dfs_path())
    #global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    target_index = global_game_data.target_node[global_game_data.current_graph_index]

    start_to_target_path = get_middle_path(graph, 0, target_index)
    target_to_end_path = get_middle_path(graph, target_index, len(graph)-1)

    assert start_to_target_path[0] == 0
    assert target_to_end_path[-1] == len(graph) - 1

    if target_index in start_to_target_path and target_index in target_to_end_path:
         target_to_end_path.remove(target_index)

    complete_path = start_to_target_path + target_to_end_path

    assert complete_path[0] == 0
    assert complete_path[-1] == len(graph) - 1

    return complete_path


def get_middle_path(graph, index_start, index_end):
    
    current_index = index_start
    last_index = None
    visited = []
    visited.append(index_start)

    assert 0 <= index_end < len(graph)

    while current_index != index_end:
        
        adjacent_list = graph[current_index][1]
        assert adjacent_list

        chosen_neighbor_index = int(random.choice(adjacent_list))
        assert chosen_neighbor_index in adjacent_list
        
        while chosen_neighbor_index == last_index and len(adjacent_list) > 1:
             chosen_neighbor_index = int(random.choice(adjacent_list))
        
        if index_end != len(graph)-1:
            while chosen_neighbor_index == len(graph)-1:
                chosen_neighbor_index = int(random.choice(adjacent_list))

        assert current_index in visited
        last_index = current_index
        current_index = chosen_neighbor_index
        visited.append(chosen_neighbor_index)

    return visited


def get_dfs_path():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    index_start = 0
    target_index = global_game_data.target_node[global_game_data.current_graph_index]
    
    assert 0 <= target_index < len(graph)
    
    start_to_target = find_dfs_path(graph,index_start,target_index)
    target_to_end = find_dfs_path(graph,target_index, len(graph)-1)

    assert start_to_target, "No path found from start to target"
    assert target_to_end, "No path found from target to end"

    assert target_index in start_to_target

    target_to_end.remove(target_index)
    assert target_index not in target_to_end, "Failed to remove target from second path"
    
    complete_path = start_to_target + target_to_end

    exit_node = len(graph) - 1
    assert complete_path[-1] == exit_node

    for i in range(len(complete_path) - 1):
        current_node = complete_path[i]
        next_node = complete_path[i + 1]
        adjacent_list = graph[current_node][1]
        assert next_node in adjacent_list
    
    return complete_path


def find_dfs_path(graph, index_start, end):
    path = []
    stack = [index_start]
    discovered = set()
    
    while stack:
        current = stack.pop()

        if current == end:
            path.append(current)
            return path

        adjacent_list = graph[current][1]
        assert adjacent_list

        if current not in discovered:
            path.append(current)
            discovered.add(current)
            for a in adjacent_list:
                if a not in discovered:
                    stack.append(a)

    return path
    


def get_bfs_path():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    index_start = 0
    target_index = global_game_data.target_node[global_game_data.current_graph_index]

    start_to_target = find_bfs_path(graph,index_start,target_index)
    target_to_end = find_bfs_path(graph,target_index, len(graph)-1)
    assert target_index in start_to_target
    
    target_to_end.remove(target_index)
    complete_path = start_to_target + target_to_end

    exit_node = len(graph) - 1
    assert complete_path[-1] == exit_node

    for i in range(len(complete_path) - 1):
        current_node = complete_path[i]
        next_node = complete_path[i + 1]
        adjacent_list = graph[current_node][1]
        assert next_node in adjacent_list

    return complete_path


def find_bfs_path(graph, index_start, end):
    queue = deque()
    path = []
    parents = {}
    parents[index_start] = None

    discovered = set([index_start])
    queue.append(index_start)

    while queue:
        current = queue.popleft()
        #path.append(current)



        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = parents[current]
            return path[::-1]

        adjacent_list = graph[current][1]
        assert adjacent_list

        for neighbor in adjacent_list:
            if neighbor not in discovered:
                discovered.add(neighbor)
                parents[neighbor] = current
                queue.append(neighbor)

    return []





def get_dijkstra_path():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    index_start = 0
    target_index = global_game_data.target_node[global_game_data.current_graph_index]

    start_to_target_predecessor = find_dijkstra_path(graph,index_start,target_index)
    target_to_end_predecessor = find_dijkstra_path(graph,target_index, len(graph)-1)

    path_one = reconstruct_path(start_to_target_predecessor, index_start, target_index)
    path_two = reconstruct_path(target_to_end_predecessor, target_index, len(graph)-1)

    # 1. Path one should start at index_start and end at target_index
    assert path_one[0] == index_start, f"Path one does not start at the correct start node: {path_one[0]}"
    assert path_one[-1] == target_index, f"Path one does not end at the target node: {path_one[-1]}"

    # 2. Path two should start at target_index and end at the last node
    assert path_two[0] == target_index, f"Path two does not start at the target node: {path_two[0]}"
    assert path_two[-1] == len(graph) - 1, f"Path two does not end at the last node: {path_two[-1]}"

    path_two.remove(target_index)
    complete_path = path_one + path_two

    # 3. Complete path should start at index_start and end at the last node
    assert complete_path[0] == index_start, f"Complete path does not start at the correct start node: {complete_path[0]}"
    assert complete_path[-1] == len(graph) - 1, f"Complete path does not end at the last node: {complete_path[-1]}"

    return complete_path

def find_dijkstra_path(graph, index_start, end):

    distance_map = {v: float('inf') for v in range(len(graph))}
    predecessor_map = {v: None for v in range(len(graph))}
    distance_map[index_start] = 0
    unvisited_queue = [(float('inf'), v) for v in range(len(graph))]
    unvisited_queue = [(0, index_start)]
    heapq.heapify(unvisited_queue)

    while unvisited_queue:
        current_distance, currentV = heapq.heappop(unvisited_queue)

        if current_distance > distance_map[currentV]:
            continue

        adjacent_list = graph[currentV][1]

        for neighbor in adjacent_list:
            edgeWeight = distance_weight(graph, currentV, neighbor)

            altPathDistance = distance_map[currentV] + edgeWeight
            
            if(altPathDistance < distance_map[neighbor]):
                distance_map[neighbor] = altPathDistance
                predecessor_map[neighbor] = currentV

                heapq.heappush(unvisited_queue, (distance_map[neighbor], neighbor))
    
    assert predecessor_map[index_start] is None, "Start node should not have a predecessor."

    reachable_nodes = {node for node in predecessor_map if predecessor_map[node] is not None}
    assert all(distance_map[node] < float('inf') for node in reachable_nodes), \
        "Nodes with predecessors should have finite distances."
    
    if end in predecessor_map and predecessor_map[end] is not None:
        assert distance_map[end] < float('inf'), "End node is unreachable despite having a predecessor."

    
    return predecessor_map


def distance_weight(graph, u,v):
    assert 0 <= u < len(graph), f"Node {u} is out of range for the graph."
    assert 0 <= v < len(graph), f"Node {v} is out of range for the graph."


    x1,y1 = graph[u][0]
    x2,y2 = graph[v][0]
    return math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)

def reconstruct_path(predecessor_map, startV, exitV):
    path = []
    current_node = exitV

    assert exitV in predecessor_map or exitV == startV, "Exit vertex is not reachable from the start vertex."

    while current_node != startV:
        path.append(current_node)
        assert current_node in predecessor_map, f"Path is broken: No predecessor for node {current_node}."
        current_node = predecessor_map[current_node]
    path.append(startV)  # Add the start node at the end
    return path[::-1]