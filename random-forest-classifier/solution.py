import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    data = [
        ['vhigh', 'vhigh', '2', '2', 'small', 'low', 'unacc'],
        ['vhigh', 'vhigh', '2', '2', 'small', 'med', 'unacc'],
        ['vhigh', 'vhigh', '2', '2', 'small', 'high', 'unacc'],
        ['vhigh', 'vhigh', '2', '2', 'med', 'low', 'unacc'],
        ['vhigh', 'vhigh', '2', '2', 'med', 'med', 'unacc'],
        ['vhigh', 'vhigh', '2', '2', 'med', 'high', 'unacc'],
        ['vhigh', 'vhigh', '2', '2', 'big', 'low', 'unacc'],
        ['vhigh', 'vhigh', '2', '2', 'big', 'med', 'unacc'],
        ['vhigh', 'vhigh', '2', '2', 'big', 'high', 'unacc'],
        ['vhigh', 'vhigh', '2', '4', 'small', 'low', 'unacc']
    ]
    
    columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
    df = pd.DataFrame(data, columns=columns)
    
    print('CAR EVALUATION RANDOM FOREST CLASSIFIER')
    print('\nMissing Values Check:')
    print(df.isnull().sum())
    
    print('\nFrequency Counts of Categorical Variables:')
    for col in columns:
        print(f'\nColumn {col}:')
        print(df[col].value_counts())
        
    X = df.drop('class', axis=1)
    y = df['class']
    
    encoder = OrdinalEncoder()
    X_encoded = encoder.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y, test_size=0.33, random_state=42
    )
    
    rf = RandomForestClassifier(random_state=42)
    rf.fit(X_train, y_train)
    
    y_pred = rf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f'\nRandom Forest Model Accuracy: {accuracy * 100:.2f}%')

if __name__ == '__main__':
    main()
