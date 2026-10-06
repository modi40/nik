def dls(graph, current_node, target_node, depth_limit, path=None):
    if path is None:
        path = []
        
    path.append(current_node)
    
    if current_node == target_node:
        return True, path
        
    if depth_limit <= 0:
        return 'cutoff', path
        
    cutoff_occurred = False
    for neighbor in graph.get(current_node, []):
        if neighbor not in path:
            found, result_path = dls(graph, neighbor, target_node, depth_limit - 1, path.copy())
            if found is True:
                return True, result_path
            elif found == 'cutoff':
                cutoff_occurred = True
                
    if cutoff_occurred:
        return 'cutoff', path
    return False, path

if __name__ == '__main__':
    tree_graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [],
        'E': [],
        'F': [],
        'G': []
    }
    
    start_v = 'A'
    goal_v = 'G'
    
    print(f'DEPTH LIMITED SEARCH (Start={start_v}, Target={goal_v})')
    
    for limit in [1, 2, 3]:
        status, traveled_path = dls(tree_graph, start_v, goal_v, limit)
        if status is True:
            print(f'Depth Limit {limit}: SUCCESS! Path = {" -> ".join(traveled_path)}')
        elif status == 'cutoff':
            print(f'Depth Limit {limit}: CUTOFF REACHED! Explored = {" -> ".join(traveled_path)}')
        else:
            print(f'Depth Limit {limit}: NOT FOUND')
