def is_consistent(variable, value, assignment, constraints):
    for neighbor in constraints.get(variable, []):
        if neighbor in assignment:
            if assignment[neighbor] == value:
                return False
    return True

def backtrack_search(variables, domains, constraints, assignment=None):
    if assignment is None:
        assignment = {}
        
    if len(assignment) == len(variables):
        return assignment
        
    unassigned = [v for v in variables if v not in assignment]
    first_var = unassigned[0]
    
    for val in domains[first_var]:
        if is_consistent(first_var, val, assignment, constraints):
            assignment[first_var] = val
            result = backtrack_search(variables, domains, constraints, assignment)
            if result is not None:
                return result
            del assignment[first_var]
            
    return None

if __name__ == '__main__':
    vars_list = ['X1', 'X2', 'X3', 'X4']
    vars_domains = {
        'X1': [1, 2, 3],
        'X2': [1, 2, 3],
        'X3': [1, 2, 3],
        'X4': [1, 2, 3]
    }
    binary_constraints = {
        'X1': ['X2', 'X3'],
        'X2': ['X1', 'X3', 'X4'],
        'X3': ['X1', 'X2', 'X4'],
        'X4': ['X2', 'X3']
    }
    
    print('BACKTRACKING CSP SOLVER')
    solution = backtrack_search(vars_list, vars_domains, binary_constraints)
    if solution:
        print('Valid Assignment Found:')
        for v in vars_list:
            print(f'{v} = {solution[v]}')
    else:
        print('No consistent assignment exists.')
