class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def tell_fact(self, fact):
        self.facts.add(fact)

    def tell_rule(self, antecedents, consequent):
        self.rules.append((antecedents, consequent))

    def infer(self):
        added = True
        while added:
            added = False
            for antecedents, consequent in self.rules:
                if set(antecedents).issubset(self.facts) and consequent not in self.facts:
                    self.facts.add(consequent)
                    added = True
                    print(f'Inferring Fact: {consequent} from {antecedents}')

    def ask(self, query):
        return query in self.facts

if __name__ == '__main__':
    kb = KnowledgeBase()
    
    kb.tell_fact('has_fur')
    kb.tell_fact('gives_milk')
    kb.tell_fact('eats_meat')
    
    kb.tell_rule(['has_fur', 'gives_milk'], 'mammal')
    kb.tell_rule(['mammal', 'eats_meat'], 'carnivore')
    kb.tell_rule(['carnivore', 'has_tawny_color'], 'lion')
    
    print('KNOWLEDGE BASE WITH RULES AND FACTS')
    print(f'Initial Facts: {kb.facts}\n')
    
    print('Running Inference:')
    kb.infer()
    
    print(f'\nUpdated Facts: {kb.facts}')
    print(f'Query: Is it a mammal? -> {kb.ask("mammal")}')
    print(f'Query: Is it a carnivore? -> {kb.ask("carnivore")}')
    print(f'Query: Is it a lion? -> {kb.ask("lion")}')
