from collections import deque

def solve_monkey_banana():
    initial_state = ('door', False, 'window', False)
    goal_state = True
    
    queue = deque([(initial_state, [])])
    visited = {initial_state}
    positions = ['door', 'window', 'middle']
    
    while queue:
        (monkey_pos, on_box, box_pos, has_banana), path = queue.popleft()
        
        if has_banana == goal_state:
            return path
            
        for next_pos in positions:
            if not on_box and next_pos != monkey_pos:
                new_state = (next_pos, on_box, box_pos, has_banana)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [f'Monkey walks from {monkey_pos} to {next_pos}']))
                    
        if not on_box and monkey_pos == box_pos:
            for next_pos in positions:
                if next_pos != box_pos:
                    new_state = (next_pos, False, next_pos, has_banana)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, path + [f'Monkey pushes box from {box_pos} to {next_pos}']))
                        
        if not on_box and monkey_pos == box_pos:
            new_state = (monkey_pos, True, box_pos, has_banana)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [f'Monkey climbs onto the box at {box_pos}']))
                
        if on_box:
            new_state = (monkey_pos, False, box_pos, has_banana)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [f'Monkey climbs down from the box at {box_pos}']))
                
        if on_box and box_pos == 'middle' and not has_banana:
            new_state = (monkey_pos, True, box_pos, True)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + ['Monkey grasps the banana']))
                
    return None

if __name__ == '__main__':
    print('BFS FOR MONKEY BANANA PROBLEM')
    print('Initial State: Monkey at door, Box at window, Banana at middle')
    solution_steps = solve_monkey_banana()
    if solution_steps:
        print(f'Goal reached in {len(solution_steps)} steps:')
        for step_num, action in enumerate(solution_steps, 1):
            print(f'Step {step_num}: {action}')
    else:
        print('No solution found.')
