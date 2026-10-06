def minimax(node, depth, is_maximizing, game_tree, leaf_scores):
    if node in leaf_scores:
        return leaf_scores[node]
        
    children = game_tree.get(node, [])
    if not children:
        return 0
        
    if is_maximizing:
        best_score = -float('inf')
        for child in children:
            score = minimax(child, depth + 1, False, game_tree, leaf_scores)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for child in children:
            score = minimax(child, depth + 1, True, game_tree, leaf_scores)
            best_score = min(best_score, score)
        return best_score

if __name__ == '__main__':
    tree = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G']
    }
    
    leaf_values = {
        'D': 3,
        'E': 5,
        'F': 2,
        'G': 9
    }
    
    print('MINIMAX ALGORITHM FOR TWO-PLAYER GAME')
    print('Game Tree Nodes:')
    for parent, children in tree.items():
        print(f'  {parent} -> {children}')
    print(f'Leaf Payoff Values: {leaf_values}')
    
    root_value = minimax('A', 0, True, tree, leaf_values)
    print(f'\nOptimal Evaluated Value at Root A: {root_value}')
    
    best_first_move = None
    best_move_score = -float('inf')
    for child in tree['A']:
        move_score = minimax(child, 1, False, tree, leaf_values)
        if move_score > best_move_score:
            best_move_score = move_score
            best_first_move = child
    print(f'Optimal Opening Move for MAX Player: Move to {best_first_move}')
