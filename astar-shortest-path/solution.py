import heapq

def a_star_search(graph, heuristics, start, destination):
    open_set = []
    heapq.heappush(open_set, (heuristics[start], 0, start, [start]))
    visited_costs = {start: 0}
    
    while open_set:
        f_cost, g_cost, current_node, path = heapq.heappop(open_set)
        
        if current_node == destination:
            return path, g_cost
            
        for neighbor, edge_weight in graph.get(current_node, []):
            new_g_cost = g_cost + edge_weight
            if neighbor not in visited_costs or new_g_cost < visited_costs[neighbor]:
                visited_costs[neighbor] = new_g_cost
                new_f_cost = new_g_cost + heuristics.get(neighbor, 0)
                heapq.heappush(open_set, (new_f_cost, new_g_cost, neighbor, path + [neighbor]))
                
    return None, float('inf')

if __name__ == '__main__':
    adjacency_graph = {
        'V1': [('V2', 2), ('V3', 4)],
        'V2': [('V1', 2), ('V4', 7), ('V5', 3)],
        'V3': [('V1', 4), ('V5', 1)],
        'V4': [('V2', 7), ('V6', 1)],
        'V5': [('V2', 3), ('V3', 1), ('V4', 2), ('V6', 5)],
        'V6': [('V4', 1), ('V5', 5)]
    }
    
    heuristic_values = {
        'V1': 6,
        'V2': 4,
        'V3': 4,
        'V4': 1,
        'V5': 3,
        'V6': 0
    }
    
    source_vertex = 'V1'
    destination_vertex = 'V6'
    
    print(f'A* Search Shortest Path from {source_vertex} to {destination_vertex}')
    shortest_path, total_path_cost = a_star_search(adjacency_graph, heuristic_values, source_vertex, destination_vertex)
    
    if shortest_path:
        print(f'Optimal Path: {" -> ".join(shortest_path)}')
        print(f'Total Shortest Cost: {total_path_cost}')
    else:
        print('Path not found.')
