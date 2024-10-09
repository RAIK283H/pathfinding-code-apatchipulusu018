import graph_data
import global_game_data
from numpy import random

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
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
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
