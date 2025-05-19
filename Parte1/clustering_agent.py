import os
import pandas as pd

from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

filename = 'iris_data_challenge.csv'
file_path = os.path.join(os.path.dirname(os.getcwd()), filename)


def main():
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {filename} not found in the current directory.")

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        raise RuntimeError(f"Error reading the file: {e}")

    df = df.rename(columns={
        'sepal length (cm)': 'sepal_length',
        'sepal width (cm)' : 'sepal_width',
        'petal length (cm)': 'petal_length',
        'petal width (cm)' : 'petal_width',
    })
    df = df.drop_duplicates()
    df = df.loc[~(df.isna().sum(axis=1) > 1)]

    df['sepal_width'] = df['sepal_width'].fillna(df['sepal_width'].mean())

    scaler = StandardScaler()
    df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']] = scaler.fit_transform(
        df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    )
    imputer = KNNImputer(n_neighbors=5)
    df[['sepal_length', 'petal_length', 'petal_width']] = imputer.fit_transform(
        df[['sepal_length', 'petal_length', 'petal_width']]
    )

    df = df.reset_index(drop=True)

    kmeans = KMeans(n_clusters=5, random_state=0, n_init='auto', max_iter=30)
    kmeans.fit(df)

    df['cluster'] = kmeans.labels_
    df['cluster'] = df['cluster'].astype('category')

    df.to_csv('iris_data_challenge_with_clusters.csv', index=False)
    print("✅ Saved clustered data to iris_data_challenge_with_clusters.csv")

    return df

if __name__ == "__main__":
    df_with_clusters = main()
    print("Clustered DataFrame:")
    print(df_with_clusters.head())
