
import numpy as np
from PIL import Image as im
import matplotlib.pyplot as plt
import sklearn.datasets as datasets

centers = [[0, 0], [2, 2], [-3, 2], [2, -4]]
X, _ = datasets.make_blobs(n_samples=300, centers=centers, cluster_std=1, random_state=0)

def show_data():
    x, y = np.hsplit(X,2)
    z = plt.scatter(x,y)
    return plt.savefig('Temp.png')