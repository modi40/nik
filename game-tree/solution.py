class GameTreeNode:
    def __init__(self, name, player_turn, value=None):
        self.name = name
        self.player_turn = player_turn
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def evaluate_minimax(node):
    if not node.children:
        return node.value

    if node.player_turn == 'MAX':
        best_val = -float('inf')
        for child in node.children:
            val = evaluate_minimax(child)
            best_val = max(best_val, val)
        node.value = best_val
        return best_val
    else:
        best_val = float('inf')
        for child in node.children:
            val = evaluate_minimax(child)
            best_val = min(best_val, val)
        node.value = best_val
        return best_val

def display_tree(node, level=0):
    indent = '    ' * level
    val_str = f'Value={node.value}' if node.value is not None else 'Unassigned'
    print(f'{indent}Node({node.name}, Turn={node.player_turn}, {val_str})')
    for child in node.children:
        display_tree(child, level + 1)

if __name__ == '__main__':
    root = GameTreeNode('Root', 'MAX')
    node_b = GameTreeNode('B', 'MIN')
    node_c = GameTreeNode('C', 'MIN')
    root.add_child(node_b)
    root.add_child(node_c)

    leaf_d = GameTreeNode('D', 'LEAF', 3)
    leaf_e = GameTreeNode('E', 'LEAF', 5)
    node_b.add_child(leaf_d)
    node_b.add_child(leaf_e)

    leaf_f = GameTreeNode('F', 'LEAF', 6)
    leaf_g = GameTreeNode('G', 'LEAF', 9)
    node_c.add_child(leaf_f)
    node_c.add_child(leaf_g)

    print('GAME TREE STRUCTURE (Before Minimax Evaluation):')
    display_tree(root)

    optimal_score = evaluate_minimax(root)

    print('\nGAME TREE STRUCTURE (After Minimax Evaluation):')
    display_tree(root)
    print(f'\nRoot Evaluated Payoff: {optimal_score}')
