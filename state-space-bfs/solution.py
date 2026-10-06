from collections import deque

def bfs_state_space(graph, start_vertex, goal_vertex=None):
    visited_sequence = []
    visited_set = {start_vertex}
    queue = deque([(start_vertex, [start_vertex])])
    goal_path = None
    
    while queue:
        current, path = queue.popleft()
        visited_sequence.append(current)
        
        if current == goal_vertex and goal_path is None:
            goal_path = path
            
        for neighbor in graph.get(current, []):
            if neighbor not in visited_set:
                visited_set.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                
    return visited_sequence, goal_path

if __name__ == '__main__':
    state_space = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'G'],
        'F': ['C', 'G'],
        'G': ['E', 'F']
    }
    
    start_node = 'A'
    goal_node = 'G'
    
    print(f'STATE SPACE SEARCH USING BFS (Start Vertex = {start_node})')
    traversed_order, found_path = bfs_state_space(state_space, start_node, goal_node)
    
    print(f'Traversal Sequence: {" -> ".join(traversed_order)}')
    if found_path:
        print(f'Path from {start_node} to {goal_node}: {" -> ".join(found_path)}')
