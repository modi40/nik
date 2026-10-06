def alpha_beta_search(depth, node_index, is_max_turn, leaf_values, alpha, beta, pruned_counter):
    if depth == 3:
        return leaf_values[node_index]
        
    if is_max_turn:
        best_val = -float('inf')
        for child_offset in range(2):
            val = alpha_beta_search(depth + 1, node_index * 2 + child_offset, False, leaf_values, alpha, beta, pruned_counter)
            best_val = max(best_val, val)
            alpha = max(alpha, best_val)
            if beta <= alpha:
                pruned_counter[0] += 1
                break
        return best_val
    else:
        best_val = float('inf')
        for child_offset in range(2):
            val = alpha_beta_search(depth + 1, node_index * 2 + child_offset, True, leaf_values, alpha, beta, pruned_counter)
            best_val = min(best_val, val)
            beta = min(beta, best_val)
            if beta <= alpha:
                pruned_counter[0] += 1
                break
        return best_val

if __name__ == '__main__':
    leaves = [3, 5, 6, 9, 1, 2, 0, -1]
    pruned_cuts = [0]
    
    print('ALPHA-BETA PRUNING ALGORITHM')
    print(f'Leaf Values: {leaves}')
    
    optimal_value = alpha_beta_search(0, 0, True, leaves, -float('inf'), float('inf'), pruned_cuts)
    
    print(f'Optimal Minimax Value: {optimal_value}')
    print(f'Pruning Cutoffs Occurred: {pruned_cuts[0]}')
