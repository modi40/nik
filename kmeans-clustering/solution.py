import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def main():
    data = {
        'country_nm': ['Country_A', 'Country_B', 'Country_C', 'Country_D', 'Country_E', 'Country_F', 'Country_G', 'Country_H', 'Country_I', 'Country_J'],
        'child_mortality': [90.2, 16.6, 27.3, 119.0, 10.3, 70.5, 4.5, 62.0, 8.2, 55.4],
        'exports': [10.0, 28.0, 38.4, 62.3, 30.7, 16.9, 76.7, 23.8, 48.0, 20.5],
        'health': [7.58, 6.55, 4.17, 2.85, 6.03, 4.56, 11.0, 5.21, 9.4, 4.88],
        'imports': [44.9, 48.6, 31.4, 42.9, 32.9, 14.5, 74.7, 30.1, 41.2, 28.6],
        'income': [1610, 9930, 12900, 5900, 19100, 3300, 41400, 3200, 29000, 4500],
        'inflation': [9.44, 4.47, 16.1, 22.4, 3.15, 12.1, 0.88, 15.3, 1.25, 8.9],
        'life_expectancy': [56.2, 76.3, 76.5, 60.1, 76.8, 60.5, 82.0, 62.1, 79.5, 65.0],
        'total_fer': [5.82, 1.55, 2.89, 6.16, 2.13, 4.87, 1.39, 4.67, 1.62, 3.8],
        'gdp': [553, 4480, 4460, 3530, 12200, 1310, 41900, 1380, 21100, 1980]
    }
    
    df = pd.DataFrame(data)
    feature_columns = ['child_mortality', 'exports', 'health', 'imports', 'income', 'inflation', 'life_expectancy', 'total_fer', 'gdp']
    X = df[feature_columns]
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    print('K-MEANS CLUSTERING (country_data.csv)')
    print('\nELBOW METHOD ANALYSIS (k = 1 to 10):')
    print(f'{"k":<4}{"Inertia (WCSS)":<15}')
    print('-' * 20)
    for k in range(1, 11):
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        km.fit(X_scaled)
        print(f'{k:<4}{km.inertia_:<15.2f}')
        
    final_kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df['Cluster'] = final_kmeans.fit_predict(X_scaled)
    
    print('\nCLUSTER ASSIGNMENT FOR COUNTRIES (Clusters = 3):')
    for _, row in df[['country_nm', 'Cluster']].iterrows():
        print(f'{row["country_nm"]:15} -> Cluster {row["Cluster"]}')

if __name__ == '__main__':
    main()
