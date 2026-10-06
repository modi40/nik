def is_valid_color(region, chosen_color, assignment, neighbors_map):
    for adjacent_region in neighbors_map.get(region, []):
        if adjacent_region in assignment and assignment[adjacent_region] == chosen_color:
            return False
    return True

def solve_map_coloring(regions, colors_domain, neighbors_map, assignment=None):
    if assignment is None:
        assignment = {}
        
    if len(assignment) == len(regions):
        return assignment
        
    unassigned = [r for r in regions if r not in assignment]
    current_region = unassigned[0]
    
    for color in colors_domain:
        if is_valid_color(current_region, color, assignment, neighbors_map):
            assignment[current_region] = color
            result = solve_map_coloring(regions, colors_domain, neighbors_map, assignment)
            if result is not None:
                return result
            del assignment[current_region]
            
    return None

if __name__ == '__main__':
    map_regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    available_colors = ['Red', 'Green', 'Blue']
    
    adjacency = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }
    
    print('MAP COLORING CSP SOLVER')
    solution = solve_map_coloring(map_regions, available_colors, adjacency)
    if solution:
        print('Valid Assignment Found:')
        for reg in map_regions:
            print(f'{reg:5} -> {solution[reg]}')
    else:
        print('No valid coloring exists.')
