import os
import pandas as pd

from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

from constants import OUTPUT_PATH

def clusterize(path_csv: str) -> str:
    """Clusters the data in the given CSV file and returns a summary of the first few rows."""

    df = pd.read_csv(path_csv)

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

    df.to_csv(OUTPUT_PATH, index=False)

    return f"✅ Clusterized data into 5 groups and saved to {OUTPUT_PATH}."


def summarize(csv_with_clusters_path) -> str:
    """Summarizes the clustered data in the CSV file."""
    if not os.path.exists(csv_with_clusters_path):
        return "❌ No clustered data found. Please run the clustering tool first."

    df = pd.read_csv(csv_with_clusters_path)

    summary = ""
    for value in sorted(df['cluster'].unique()):
        cluster_df = df[df['cluster'] == value]
        summary += f"Cluster {value}:\n"
        summary += f"  - Count: {len(cluster_df)}\n"
        summary += f"  - Mean Sepal Length: {cluster_df['sepal_length'].mean()}\n"
        summary += f"  - Mean Sepal Width: {cluster_df['sepal_width'].mean()}\n"
        summary += f"  - Mean Petal Length: {cluster_df['petal_length'].mean()}\n"
        summary += f"  - Mean Petal Width: {cluster_df['petal_width'].mean()}\n\n"

    return summary