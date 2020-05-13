import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import TSNE

import random

from scipy.spatial import distance

import seaborn as sns
import matplotlib.pyplot as plt

path = "songs_25.csv"
k = 15 # input number of clusters 2 - 10
iterations = 3 # number of improvements of cluster
initialise = 1 # number of new initialisations of mü; 50 - 1000


class KMeans:
    def __init__(self, path, k, iterations, initialise):
        self.path = path
        self.k = k
        self.iterations = iterations
        self.initialise = initialise

    def prepare_data(self):
        songs = pd.read_csv(self.path)
        # songs = songs[:150]  #löschen!!
        songs.fillna(0)
        data = songs['text']
        tf_idf_vectorizer = TfidfVectorizer()
        tf_idf = tf_idf_vectorizer.fit_transform(data)
        # tf_idf_norm = normalize(tf_idf)
        # array = tf_idf_norm.toarray()
        X_reduced = TruncatedSVD(n_components=10, random_state=0).fit_transform(tf_idf)
        X_embedded = TSNE(n_components=2, perplexity=50, n_iter=1000, learning_rate=10, verbose=2).fit_transform(X_reduced)
        return X_embedded


    def initialise_centroids(self, array):
        mü = {}

        idx = np.random.randint(array.shape[0], size=self.k)
        centroids = array[idx, :]

        for c in range(len(centroids)):
            mü[c] = list(centroids[c])
        return mü

    def assign_clusters(self, mü, array):
        clustering_step = {}
        for K in range(k):
            clustering_step[K] = []
        for x in array:
            distances_dic = {}
            for K in range(self.k):
                d = distance.euclidean(x, mü[K])
                distances_dic[K] = d
            minimum = min(distances_dic.values())
            best_cluster = list(distances_dic.keys())[list(distances_dic.values()).index(minimum)]
            clustering_step[best_cluster].append(list(x))
        return clustering_step

    def improve_clusters(self, clustering_step):
        mü = {}
        for K in range(k):
            if K in clustering_step.keys():
                if clustering_step[K] == []:
                    idx = np.random.randint(array.shape[0], size=self.k)
                    centroids = array[idx, :]
                    for c in range(len(centroids)):
                        mü[K] = list(centroids[c])
                else:
                    mean = np.mean(clustering_step[K], axis=0)
                    mü[K] = mean
        return mü

    def compare_results(self, clustering_step, compare):
        d = []
        for key, values in clustering_step.items():
            if compare[key] == []:
                break
            else:
                union = set(clustering_step[key][0]).union(set(compare[key][0]))
                intersection = set(clustering_step[key][0]).intersection(set(compare[key][0]))
                difference = union - intersection
                d.append(difference)
        return d
#
# #Schleife mit für Neuinitialisierungen

kmeans = KMeans(path, k, iterations, initialise)

clusterings = {}
array = kmeans.prepare_data()
new_cents = {}
for new_centroids in range(initialise):
    mü_one = kmeans.initialise_centroids(array)

    for i in range(iterations):
        if i==0:
            compare = kmeans.assign_clusters(mü_one, array)
            mü = kmeans.improve_clusters(compare)
        else:
            clusters = kmeans.assign_clusters(mü, array)
            mü = kmeans.improve_clusters(clusters)
            if kmeans.compare_results(clusters, compare) == set():
                compare = clusters
                break
            else:
                compare = clusters
        clusterings[i] = compare
    new_cents[new_centroids] = clusterings


distances = []
distances_per_cluster = {}
all_iterations = {}

for c in new_cents.keys():
    # c = new initialisation of centroids
    for key in new_cents[c].keys():
        #key = iteration
        for ke in new_cents[c][key].keys():
            # ke = cluster
            for l in new_cents[c][key][ke]:
                d = distance.euclidean(l, mü[ke])
                distances.append(d)
            distances_per_cluster[ke] = np.mean(distances)
        all_iterations[key] = np.mean(list(distances_per_cluster.values()))
print(all_iterations, "\n", min(all_iterations.values()))

labels = []
punkte = []
for y, v in all_iterations.items():
    if v == min(all_iterations.values()):
        # print("clusterings",(clusterings[y]), mü[y])
        for o,r in clusterings[y].items():
            l = len(clusterings[y][o])
            labels.extend([o for i in range(l)])
            for punkt in r:
                punkte.append(tuple(punkt))
ws = []
es = []
for w, e in punkte:
    ws.append(w)
    es.append(e)


# for x,va in clusterings[y].items():

fig = plt.figure(figsize=(8, 8))
sns.scatterplot(ws, es, hue=labels, marker="o", palette=sns.color_palette("hls", k), legend=False)
plt.show()
