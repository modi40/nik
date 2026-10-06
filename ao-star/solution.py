class AOStar:
    def __init__(self, graph, heuristics):
        self.graph = graph
        self.heuristics = heuristics
        self.marked_path = {}

    def get_minimum_cost_child_node(self, node):
        min_cost = float('inf')
        best_child_branch = None
        
        for branch in self.graph.get(node, []):
            branch_cost = 0
            for child_node, edge_cost in branch:
                branch_cost += edge_cost + self.heuristics.get(child_node, 0)
            if branch_cost < min_cost:
                min_cost = branch_cost
                best_child_branch = branch
                
        return min_cost, best_child_branch

    def compute_ao_star(self, node):
        if node not in self.graph or not self.graph[node]:
            return
            
        min_cost, best_branch = self.get_minimum_cost_child_node(node)
        self.heuristics[node] = min_cost
        self.marked_path[node] = best_branch
        
        for child_node, _ in best_branch:
            self.compute_ao_star(child_node)

if __name__ == '__main__':
    and_or_graph = {
        'A': [[('B', 1), ('C', 1)], [('D', 1)]],
        'B': [[('G', 1)], [('H', 1)]],
        'D': [[('E', 1), ('F', 1)]]
    }
    
    node_heuristics = {
        'A': -1,
        'B': 4,
        'C': 2,
        'D': 3,
        'E': 6,
        'F': 8,
        'G': 2,
        'H': 0
    }
    
    print('AO* ALGORITHM FOR AND-OR GRAPHS')
    print(f'Initial Heuristics: {node_heuristics}')
    
    solver = AOStar(and_or_graph, node_heuristics)
    solver.compute_ao_star('A')
    
    print(f'\nUpdated Heuristic Costs: {solver.heuristics}')
    print('\nMarked Optimal Branches:')
    for parent, branch in solver.marked_path.items():
        branch_desc = ' AND '.join(f'{child}(cost={cost})' for child, cost in branch)
        print(f'{parent} -> [{branch_desc}]')
