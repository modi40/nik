def dfs_state_space(graph, start_vertex, goal_vertex=None):
    visited = []
    visited_set = set()
    path_found = []
    
    def dfs_helper(current_vertex, current_path):
        visited.append(current_vertex)
        visited_set.add(current_vertex)
        
        if current_vertex == goal_vertex:
            path_found.extend(current_path)
            return True
            
        for neighbor in graph.get(current_vertex, []):
            if neighbor not in visited_set:
                if dfs_helper(neighbor, current_path + [neighbor]):
                    return True
        return False

    dfs_helper(start_vertex, [start_vertex])
    return visited, path_found

if __name__ == '__main__':
    graph = {
        1: [2, 3],
        2: [1, 4, 5],
        3: [1, 6],
        4: [2],
        5: [2, 7],
        6: [3, 7],
        7: [5, 6]
    }
    
    start_node = 1
    goal_node = 7
    
    print(f'DFS STATE-SPACE SEARCH (Start Vertex = {start_node})')
    visited_nodes, solution_path = dfs_state_space(graph, start_node, goal_node)
    
    print(f'Visited Vertices in Order: {visited_nodes}')
    print(f'Path to Goal ({goal_node}): {solution_path}')
