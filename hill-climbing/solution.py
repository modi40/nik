def objective_function(x):
    return -(x ** 2) + 4 * x

def hill_climbing(start_x, step_size=0.01, max_iterations=1000):
    current_x = start_x
    current_val = objective_function(current_x)
    
    for iteration in range(max_iterations):
        left_x = current_x - step_size
        right_x = current_x + step_size
        
        left_val = objective_function(left_x)
        right_val = objective_function(right_x)
        
        if left_val > current_val and left_val >= right_val:
            current_x = left_x
            current_val = left_val
        elif right_val > current_val and right_val > left_val:
            current_x = right_x
            current_val = right_val
        else:
            break
            
    return current_x, current_val

if __name__ == '__main__':
    initial_x = 0.0
    print('HILL CLIMBING OPTIMIZATION')
    print('Objective Function: F(x) = -x^2 + 4x')
    print(f'Starting Point: x = {initial_x}, F(x) = {objective_function(initial_x)}')
    
    peak_x, peak_val = hill_climbing(initial_x)
    print(f'Local/Global Maximum found at: x = {peak_x:.4f}')
    print(f'Maximum Value F(x) = {peak_val:.4f}')
