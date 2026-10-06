import heapq

def manhattan_distance(state, goal_coords):
    distance = 0
    for r in range(2):
        for c in range(2):
            val = state[r][c]
            if val != 0:
                target_r, target_c = goal_coords[val]
                distance += abs(r - target_r) + abs(c - target_c)
    return distance

def get_neighbors(state):
    neighbors = []
    blank_r, blank_c = 0, 0
    for r in range(2):
        for c in range(2):
            if state[r][c] == 0:
                blank_r, blank_c = r, c
                break

    moves = [(-1, 0, 'UP'), (1, 0, 'DOWN'), (0, -1, 'LEFT'), (0, 1, 'RIGHT')]
    for dr, dc, move_name in moves:
        nr, nc = blank_r + dr, blank_c + dc
        if 0 <= nr < 2 and 0 <= nc < 2:
            new_board = [list(row) for row in state]
            new_board[blank_r][blank_c], new_board[nr][nc] = new_board[nr][nc], new_board[blank_r][blank_c]
            neighbors.append((tuple(tuple(r) for r in new_board), move_name))
    return neighbors

def solve_4_puzzle(start_state, goal_state):
    goal_coords = {}
    for r in range(2):
        for c in range(2):
            goal_coords[goal_state[r][c]] = (r, c)

    open_queue = []
    initial_h = manhattan_distance(start_state, goal_coords)
    heapq.heappush(open_queue, (initial_h, 0, start_state, []))
    visited = {start_state: 0}

    while open_queue:
        f_cost, g_cost, state, path = heapq.heappop(open_queue)

        if state == goal_state:
            return path

        for neighbor, move_name in get_neighbors(state):
            new_g = g_cost + 1
            if neighbor not in visited or new_g < visited[neighbor]:
                visited[neighbor] = new_g
                new_f = new_g + manhattan_distance(neighbor, goal_coords)
                heapq.heappush(open_queue, (new_f, new_g, neighbor, path + [(move_name, neighbor)]))

    return None

if __name__ == '__main__':
    start = ((1, 2), (0, 3))
    goal = ((1, 2), (3, 0))

    print('4-PUZZLE SOLVER USING A* SEARCH')
    print(f'Initial State: {start}')
    print(f'Goal State:    {goal}\n')

    solution = solve_4_puzzle(start, goal)
    if solution:
        print(f'Optimal Path Found in {len(solution)} moves:')
        for step_num, (direction, board) in enumerate(solution, 1):
            print(f'Step {step_num}: Move {direction} -> {board}')
    else:
        print('No solution found.')
