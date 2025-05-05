
import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def customer_segmentation_graph(input_file):
    df = pd.read_csv(input_file.name)
    x = df['Age']
    y = df['Spending']

    kmeans = KMeans(n_clusters=3)
    df['Cluster'] = kmeans.fit_predict(df[['Age', 'Spending']])

    plt.figure(figsize=(6, 4))
    plt.scatter(df['Age'], df['Spending'], c=df['Cluster'], cmap='viridis')
    plt.title("Customer Segmentation Analysis")
    plt.xlabel("Age")
    plt.ylabel("Spending")
    plt.colorbar(label="Cluster")
    plt.savefig('/tmp/segmentation_graph.png')
    return '/tmp/segmentation_graph.png'
