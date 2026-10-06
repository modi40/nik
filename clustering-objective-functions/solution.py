import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score, davies_bouldin_score

def main():
    X, _ = make_blobs(n_samples=200, centers=4, cluster_std=1.2, random_state=42)
    
    k_range = list(range(2, 9))
    wcss = []
    silhouette_scores = []
    davies_bouldin_scores = []
    gmm_log_likelihood = []
    
    for k in k_range:
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        km_labels = km.fit_predict(X)
        wcss.append(km.inertia_)
        silhouette_scores.append(silhouette_score(X, km_labels))
        davies_bouldin_scores.append(davies_bouldin_score(X, km_labels))
        
        gmm = GaussianMixture(n_components=k, random_state=42)
        gmm.fit(X)
        gmm_log_likelihood.append(gmm.score(X))
        
    print('CLUSTERING OBJECTIVE FUNCTIONS')
    print(f'{"K":<4}{"WCSS (Inertia)":<16}{"Silhouette":<14}{"Davies-Bouldin":<16}{"GMM Log-Likelihood":<18}')
    print('-' * 68)
    for i, k in enumerate(k_range):
        print(f'{k:<4}{wcss[i]:<16.2f}{silhouette_scores[i]:<14.4f}{davies_bouldin_scores[i]:<16.4f}{gmm_log_likelihood[i]:<18.4f}')
        
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    axes[0].plot(k_range, wcss, 'bo-', linewidth=2)
    axes[0].set_title('Elbow Curve (WCSS / Inertia)')
    axes[0].set_xlabel('Number of Clusters (K)')
    axes[0].set_ylabel('Inertia')
    
    axes[1].plot(k_range, silhouette_scores, 'ro-', linewidth=2)
    axes[1].set_title('Silhouette Scores')
    axes[1].set_xlabel('Number of Clusters (K)')
    axes[1].set_ylabel('Score')
    
    axes[2].plot(k_range, davies_bouldin_scores, 'go-', linewidth=2)
    axes[2].set_title('Davies-Bouldin Index')
    axes[2].set_xlabel('Number of Clusters (K)')
    axes[2].set_ylabel('Score (Lower is better)')
    
    plt.tight_layout()
    plt.savefig('clustering_evaluation.png')
    print('\nEvaluation plot saved to clustering_evaluation.png')

if __name__ == '__main__':
    main()
