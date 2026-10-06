def forall(domain, predicate):
    return all(predicate(x) for x in domain)

def exists(domain, predicate):
    return any(predicate(x) for x in domain)

def is_even(num):
    return num % 2 == 0

def is_greater_than_zero(num):
    return num > 0

def is_mortal(person):
    humans = {'Socrates', 'Plato', 'Aristotle'}
    return person in humans

if __name__ == '__main__':
    numbers = [2, 4, 6, 8, 10]
    mixed_numbers = [1, 2, 3, 4, 5]
    philosophers = ['Socrates', 'Plato', 'Aristotle']
    
    print('PREDICATE LOGIC DEMONSTRATION')
    print(f'Domain 1: {numbers}')
    print(f'Domain 2: {mixed_numbers}')
    print(f'Domain 3: {philosophers}\n')
    
    q1 = forall(numbers, is_even)
    print(f'Statement: For all x in numbers, is_even(x) -> {q1}')
    
    q2 = forall(mixed_numbers, is_even)
    print(f'Statement: For all x in mixed_numbers, is_even(x) -> {q2}')
    
    q3 = exists(mixed_numbers, is_even)
    print(f'Statement: Exists x in mixed_numbers such that is_even(x) -> {q3}')
    
    q4 = forall(philosophers, is_mortal)
    print(f'Statement: For all x in philosophers, is_mortal(x) -> {q4}')
