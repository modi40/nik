from collections import deque

def is_valid_state(pegs):
    for peg in pegs:
        for i in range(len(peg) - 1):
            if peg[i] < peg[i + 1]:
                return False
    return True

def get_next_hanoi_states(pegs):
    next_states = []
    for from_peg in range(3):
        if not pegs[from_peg]:
            continue
        disk = pegs[from_peg][-1]
        for to_peg in range(3):
            if from_peg != to_peg:
                if not pegs[to_peg] or pegs[to_peg][-1] > disk:
                    new_pegs = list(list(p) for p in pegs)
                    new_pegs[from_peg].pop()
                    new_pegs[to_peg].append(disk)
                    state_tuple = tuple(tuple(p) for p in new_pegs)
                    action = f'Move disk {disk} from Peg {chr(65 + from_peg)} to Peg {chr(65 + to_peg)}'
                    next_states.append((state_tuple, action))
    return next_states

def solve_tower_of_hanoi(num_disks=3):
    initial_pegs = (tuple(range(num_disks, 0, -1)), (), ())
    goal_pegs = ((), (), tuple(range(num_disks, 0, -1)))
    
    queue = deque([(initial_pegs, [])])
    visited = {initial_pegs}
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == goal_pegs:
            return path
            
        for next_state, action in get_next_hanoi_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [(action, next_state)]))
                
    return None

if __name__ == '__main__':
    print('TOWER OF HANOI (STATE-SPACE SEARCH)')
    steps = solve_tower_of_hanoi(3)
    if steps:
        print(f'Solved in {len(steps)} moves:\n')
        for idx, (move, state) in enumerate(steps, 1):
            print(f'Step {idx}: {move} | State = {state}')
