from scipy.cluster.hierarchy import dendrogram, linkage
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("clean_steam_data.csv",dtype={'Name': 'str'}, low_memory=False)