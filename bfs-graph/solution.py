from collections import deque

def bfs_traversal(graph, start_vertex):
    visited = []
    visited_set = {start_vertex}
    queue = deque([start_vertex])
    
    while queue:
        vertex = queue.popleft()
        visited.append(vertex)
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited_set:
                visited_set.add(neighbor)
                queue.append(neighbor)
                
    return visited

if __name__ == '__main__':
    graph_adjacency = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    start_node = 'A'
    print('GRAPH BFS TRAVERSAL')
    print('Adjacency List:')
    for node, neighbors in graph_adjacency.items():
        print(f'{node}: {neighbors}')
        
    traversal_order = bfs_traversal(graph_adjacency, start_node)
    print(f'\nBFS Order starting from {start_node}: {" -> ".join(traversal_order)}')
