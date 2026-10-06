def minimax(depth, node_index, is_max, values, counter):
    counter[0] += 1
    if depth == 3:
        return values[node_index]
        
    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, values, counter),
            minimax(depth + 1, node_index * 2 + 1, False, values, counter)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, values, counter),
            minimax(depth + 1, node_index * 2 + 1, True, values, counter)
        )

def alpha_beta(depth, node_index, is_max, values, alpha, beta, counter):
    counter[0] += 1
    if depth == 3:
        return values[node_index]
        
    if is_max:
        best_val = -float('inf')
        for i in range(2):
            val = alpha_beta(depth + 1, node_index * 2 + i, False, values, alpha, beta, counter)
            best_val = max(best_val, val)
            alpha = max(alpha, best_val)
            if beta <= alpha:
                break
        return best_val
    else:
        best_val = float('inf')
        for i in range(2):
            val = alpha_beta(depth + 1, node_index * 2 + i, True, values, alpha, beta, counter)
            best_val = min(best_val, val)
            beta = min(beta, best_val)
            if beta <= alpha:
                break
        return best_val

if __name__ == '__main__':
    terminal_values = [3, 5, 6, 9, 1, 2, 0, -1]
    
    minimax_evals = [0]
    mm_result = minimax(0, 0, True, terminal_values, minimax_evals)
    
    ab_evals = [0]
    ab_result = alpha_beta(0, 0, True, terminal_values, -float('inf'), float('inf'), ab_evals)
    
    print('COMPARISON: MINIMAX vs ALPHA-BETA PRUNING')
    print(f'Terminal Leaf Values: {terminal_values}')
    print(f'Minimax Score:        {mm_result} (Nodes Visited: {minimax_evals[0]})')
    print(f'Alpha-Beta Score:     {ab_result} (Nodes Visited: {ab_evals[0]})')
    pruned_nodes = minimax_evals[0] - ab_evals[0]
    efficiency = (pruned_nodes / minimax_evals[0]) * 100
    print(f'Nodes Pruned:         {pruned_nodes}')
    print(f'Search Reduction:     {efficiency:.2f}%')
