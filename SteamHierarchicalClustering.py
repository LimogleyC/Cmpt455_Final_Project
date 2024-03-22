from scipy.cluster.hierarchy import dendrogram, linkage
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("clean_steam_data.csv")

# print(data.shape)

# linkage_data = linkage(data, method='ward', metric='euclidean')

# # Visualize the dendrogram
# plt.figure(figsize=(12, 6))
# dendrogram(linkage_data)
# plt.title('Hierarchical Clustering Dendrogram')
# plt.xlabel('Sample Index')
# plt.ylabel('Distance')
# plt.show()

sample_size = 10000  # Adjust this based on your requirements

# Randomly sample the data
data_sample = data.sample(n=sample_size, random_state=42)  # Adjust random_state for reproducibility

# Perform hierarchical clustering on the sample
linkage_data = linkage(data_sample, method='ward', metric='euclidean')

# Visualize the dendrogram
plt.figure(figsize=(12, 6))
dendrogram(linkage_data)
plt.title('Hierarchical Clustering Dendrogram (Sample)')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.show()