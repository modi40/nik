class ExpertSystem:
    def __init__(self):
        self.rules = [
            ({'fever', 'cough'}, 'Flu'),
            ({'fever', 'rash'}, 'Measles'),
            ({'headache', 'fever'}, 'Viral Infection'),
            ({'Flu', 'fatigue'}, 'Severe Flu'),
            ({'sneezing', 'runny_nose'}, 'Common Cold')
        ]
        
    def diagnose(self, observed_symptoms):
        known_facts = set(observed_symptoms)
        inferred = True
        
        while inferred:
            inferred = False
            for premises, conclusion in self.rules:
                if premises.issubset(known_facts) and conclusion not in known_facts:
                    known_facts.add(conclusion)
                    inferred = True
                    print(f'Rule fired: IF {premises} THEN {conclusion}')
                    
        conclusions = [fact for fact in known_facts if fact not in observed_symptoms]
        return conclusions

if __name__ == '__main__':
    system = ExpertSystem()
    user_symptoms = ['fever', 'cough', 'fatigue']
    
    print('RULE-BASED EXPERT SYSTEM')
    print(f'Observed Symptoms: {user_symptoms}')
    print('\nInference Process:')
    results = system.diagnose(user_symptoms)
    print(f'\nFinal Diagnosis Conclusions: {results}')
