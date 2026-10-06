def backward_chain(goal, facts, rules, depth=0):
    indent = '  ' * depth
    print(f'{indent}Testing Goal: {goal}')
    
    if goal in facts:
        print(f'{indent}-> Fact {goal} is known!')
        return True
        
    for premises, conclusion in rules:
        if conclusion == goal:
            print(f'{indent}Found Rule with conclusion {goal}: Requires {premises}')
            all_premises_proven = True
            for premise in premises:
                if not backward_chain(premise, facts, rules, depth + 1):
                    all_premises_proven = False
                    break
            if all_premises_proven:
                print(f'{indent}-> All premises for {goal} satisfied!')
                return True
                
    print(f'{indent}-> Could not prove {goal}')
    return False

if __name__ == '__main__':
    kb_rules = [
        (['A', 'B'], 'C'),
        (['C'], 'D'),
        (['D', 'E'], 'Goal')
    ]
    known_facts = {'A', 'B', 'E'}
    target_hypothesis = 'Goal'
    
    print('BACKWARD CHAINING INFERENCE MECHANISM')
    print(f'Known Facts: {known_facts}')
    print(f'Goal Hypothesis: {target_hypothesis}\n')
    
    result = backward_chain(target_hypothesis, known_facts, kb_rules)
    print(f'\nHypothesis "{target_hypothesis}" Proven: {result}')
