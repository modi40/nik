from sklearn.datasets import make_classification, make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, silhouette_score
from sklearn.model_selection import train_test_split

def demonstrate_supervised():
    print('1. SUPERVISED LEARNING DEMONSTRATION')
    X, y = make_classification(n_samples=100, n_features=4, n_classes=2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    clf = LogisticRegression()
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    print('Model: Logistic Regression (Classification)')
    print(f'Training Samples: {len(X_train)} | Test Samples: {len(X_test)}')
    print(f'Evaluation Metric: Accuracy = {accuracy * 100:.2f}%\n')

def demonstrate_unsupervised():
    print('2. UNSUPERVISED LEARNING DEMONSTRATION')
    X, _ = make_blobs(n_samples=100, n_features=4, centers=3, random_state=42)
    
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(X)
    score = silhouette_score(X, cluster_labels)
    
    print('Model: K-Means Clustering')
    print(f'Samples Clustered: {len(X)} into 3 clusters')
    print(f'Evaluation Metric: Silhouette Score = {score:.4f}\n')

def print_comparative_report():
    print('=' * 60)
    print('COMPARATIVE REPORT: SUPERVISED vs UNSUPERVISED LEARNING')
    print('=' * 60)
    table = [
        ('Criterion', 'Supervised Learning', 'Unsupervised Learning'),
        ('Input Data', 'Labeled dataset (Features + Targets)', 'Unlabeled dataset (Features only)'),
        ('Primary Task', 'Classification, Regression', 'Clustering, Association, Dimensionality Reduction'),
        ('Goal', 'Predict outcomes for unseen data', 'Discover hidden patterns/structures in data'),
        ('Algorithms', 'Decision Tree, SVM, Random Forest, NB', 'K-Means, Hierarchical, PCA, Apriori'),
        ('Evaluation', 'Accuracy, Precision, Recall, MSE', 'Silhouette Score, WCSS Inertia, Davies-Bouldin'),
        ('Human Feedback', 'Requires labeled ground truth', 'No human labeling required')
    ]
    for row in table:
        print(f'{row[0]:<16} | {row[1]:<35} | {row[2]}')
    print('=' * 60)

if __name__ == '__main__':
    demonstrate_supervised()
    demonstrate_unsupervised()
    print_comparative_report()
