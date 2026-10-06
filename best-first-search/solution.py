import heapq

def best_first_search(graph, heuristics, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristics[start], start, [start]))
    visited = set()
    
    while priority_queue:
        h_val, current_node, path = heapq.heappop(priority_queue)
        
        if current_node == goal:
            return path
            
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (heuristics.get(neighbor, float('inf')), neighbor, path + [neighbor]))
                    
    return None

if __name__ == '__main__':
    graph_map = {
        'S': ['A', 'B'],
        'A': ['C', 'D'],
        'B': ['E', 'F'],
        'C': [],
        'D': ['G'],
        'E': [],
        'F': ['G'],
        'G': []
    }
    
    heuristic_map = {
        'S': 13,
        'A': 10,
        'B': 4,
        'C': 15,
        'D': 6,
        'E': 8,
        'F': 2,
        'G': 0
    }
    
    start_vertex = 'S'
    goal_vertex = 'G'
    
    print('GREEDY BEST FIRST SEARCH')
    print(f'Start Node: {start_vertex}, Goal Node: {goal_vertex}')
    found_path = best_first_search(graph_map, heuristic_map, start_vertex, goal_vertex)
    
    if found_path:
        print(f'Path Found: {" -> ".join(found_path)}')
    else:
        print('No path found.')
