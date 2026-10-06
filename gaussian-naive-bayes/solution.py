import numpy as np
from sklearn.datasets import make_blobs
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def main():
    X, y = make_blobs(
        n_samples=200,
        n_features=2,
        centers=3,
        cluster_std=1.5,
        random_state=42
    )
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    
    model = GaussianNB()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    
    test_points = np.array([[-2, 5], [0, 0], [6, -0.3]])
    predictions = model.predict(test_points)
    
    print('GAUSSIAN NAIVE BAYES CLASSIFIER')
    print(f'Total Dataset Samples: {len(X)}')
    print(f'Number of Classes: 3')
    print(f'Model Accuracy Score: {acc:.4f}')
    print(f'Input (Values)  : {test_points.tolist()}')
    print(f'Output          : {predictions}')

if __name__ == '__main__':
    main()
