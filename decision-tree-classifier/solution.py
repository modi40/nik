import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    data = {
        'Pregnancies': [6, 1, 8, 1, 0, 5, 3, 10, 2, 8, 4],
        'Glucose': [148, 85, 183, 89, 137, 116, 78, 115, 197, 125, 110],
        'BP': [72, 66, 64, 66, 40, 74, 50, 0, 70, 96, 92],
        'SkinThick': [35, 29, 0, 23, 35, 0, 32, 0, 45, 0, 0],
        'Insulin': [0, 0, 0, 94, 168, 0, 88, 0, 543, 0, 0],
        'BMI': [33.6, 26.6, 23.3, 28.1, 43.1, 25.6, 31.0, 35.3, 30.5, 0.0, 37.6],
        'DiabetesPF': [0.627, 0.351, 0.672, 0.167, 2.288, 0.201, 0.248, 0.134, 0.158, 0.232, 0.191],
        'Age': [50, 31, 32, 21, 33, 30, 26, 29, 53, 54, 30],
        'Outcome': [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0]
    }
    
    df = pd.DataFrame(data)
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=42
    )
    
    default_model = DecisionTreeClassifier(criterion='gini', random_state=42)
    default_model.fit(X_train, y_train)
    default_acc = accuracy_score(y_test, default_model.predict(X_test))
    
    print('DECISION TREE CLASSIFIER')
    print(f'Default GINI Accuracy: {default_acc:.4f}\n')
    print('TUNING CRITERION AND MAX_DEPTH:')
    print(f'{"Criterion":<12}{"Max Depth":<12}{"Accuracy":<10}')
    print('-' * 34)
    
    for crit in ['gini', 'entropy']:
        for depth in [2, 3, 4]:
            tuned_model = DecisionTreeClassifier(criterion=crit, max_depth=depth, random_state=42)
            tuned_model.fit(X_train, y_train)
            acc = accuracy_score(y_test, tuned_model.predict(X_test))
            print(f'{crit:<12}{depth:<12}{acc:.4f}')

if __name__ == '__main__':
    main()
