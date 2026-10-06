def forward_chaining(rules, initial_facts, goal):
    facts = set(initial_facts)
    derived = True
    
    print('FORWARD CHAINING INFERENCE')
    print(f'Initial Facts: {sorted(list(facts))}')
    print(f'Target Goal:   {goal}\n')
    
    while derived:
        derived = False
        for premises, conclusion in rules:
            if set(premises).issubset(facts) and conclusion not in facts:
                facts.add(conclusion)
                derived = True
                print(f'Derived: {conclusion} (Premises: {premises})')
                if conclusion == goal:
                    return True, facts
                    
    return goal in facts, facts

if __name__ == '__main__':
    kb_rules = [
        (['A', 'B'], 'C'),
        (['C', 'D'], 'E'),
        (['E'], 'Z')
    ]
    known_facts = ['A', 'B', 'D']
    target_goal = 'Z'
    
    achieved, final_facts = forward_chaining(kb_rules, known_facts, target_goal)
    print(f'\nGoal "{target_goal}" proven: {achieved}')
    print(f'All Derived Facts: {sorted(list(final_facts))}')
