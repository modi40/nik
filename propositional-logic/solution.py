def op_not(p):
    return not p

def op_and(p, q):
    return p and q

def op_or(p, q):
    return p or q

def op_implies(p, q):
    return (not p) or q

def evaluate_expressions():
    truth_values = [True, False]
    
    print(f'{"P":<6}{"Q":<6}{"NOT P":<10}{"P AND Q":<10}{"P OR Q":<10}{"P -> Q":<10}')
    print('-' * 52)
    
    for p in truth_values:
        for q in truth_values:
            not_p = op_not(p)
            p_and_q = op_and(p, q)
            p_or_q = op_or(p, q)
            p_imp_q = op_implies(p, q)
            print(f'{str(p):<6}{str(q):<6}{str(not_p):<10}{str(p_and_q):<10}{str(p_or_q):<10}{str(p_imp_q):<10}')

    print('\nTRUTH TABLE FOR COMPLEX EXPRESSION: (P AND Q) IMPLIES (P OR Q)')
    print(f'{"P":<6}{"Q":<6}{"(P AND Q) -> (P OR Q)":<25}')
    print('-' * 35)
    for p in truth_values:
        for q in truth_values:
            expr = op_implies(op_and(p, q), op_or(p, q))
            print(f'{str(p):<6}{str(q):<6}{str(expr):<25}')

if __name__ == '__main__':
    evaluate_expressions()
