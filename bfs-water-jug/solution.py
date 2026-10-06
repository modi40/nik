from collections import deque

def solve_water_jug_bfs(jug1_cap, jug2_cap, target):
    initial_state = (0, 0)
    queue = deque([(initial_state, [])])
    visited = {initial_state}
    
    while queue:
        (j1, j2), path = queue.popleft()
        
        if j1 == target or j2 == target:
            return path + [(j1, j2, f'Target {target}L reached')]
            
        possible_moves = [
            (jug1_cap, j2, f'Fill Jug 1 to {jug1_cap}L'),
            (j1, jug2_cap, f'Fill Jug 2 to {jug2_cap}L'),
            (0, j2, 'Empty Jug 1'),
            (j1, 0, 'Empty Jug 2'),
            (j1 - min(j1, jug2_cap - j2), j2 + min(j1, jug2_cap - j2), 'Pour Jug 1 -> Jug 2'),
            (j1 + min(j2, jug1_cap - j1), j2 - min(j2, jug1_cap - j1), 'Pour Jug 2 -> Jug 1')
        ]
        
        for next_j1, next_j2, action_desc in possible_moves:
            next_state = (next_j1, next_j2)
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [(j1, j2, action_desc)]))
                
    return None

if __name__ == '__main__':
    cap1, cap2, goal_amount = 4, 3, 2
    print(f'WATER JUG PROBLEM VIA BFS (Capacities: {cap1}L, {cap2}L | Target: {goal_amount}L)')
    steps = solve_water_jug_bfs(cap1, cap2, goal_amount)
    if steps:
        print(f'Solution found in {len(steps)} steps:')
        for idx, (curr_j1, curr_j2, action) in enumerate(steps, 1):
            print(f'Step {idx}: Action="{action}" | State=({curr_j1}L, {curr_j2}L)')
    else:
        print('No solution possible.')
