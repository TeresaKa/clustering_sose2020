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


class KMeans:
    def __init__(self, path, k, iterations, initialise):
        self.path = path
        self.k = k
        self.iterations = iterations
        self.initialise = initialise

    def prepare_data(self):
        """ Dimensionality reduction of data """
        songs = pd.read_csv(self.path)
        songs.fillna(0)
        data = songs['text']
        tf_idf_vectorizer = TfidfVectorizer()
        tf_idf = tf_idf_vectorizer.fit_transform(data)
        X_reduced = TruncatedSVD(n_components=10, random_state=0).fit_transform(tf_idf)
        X_embedded = TSNE(n_components=2, perplexity=50, n_iter=1000, learning_rate=10, verbose=2).fit_transform(X_reduced)
        return X_embedded


    def initialise_centroids(self, array):
        """ Initialise centroids randomly from range of given datapoints """
        mü = {}

        idx = np.random.randint(array.shape[0], size=self.k)
        centroids = array[idx, :]

        for c in range(len(centroids)):
            mü[c] = list(centroids[c])
        return mü

    def assign_clusters(self, mü, array, dist):
        clustering_step = {}
        for K in range(k):
            clustering_step[K] = []
        for x in array:
            distances_dic = {}
            for K in range(self.k):
                d = dist(x, mü[K])
                distances_dic[K] = d
            minimum = min(distances_dic.values())
            best_cluster = list(distances_dic.keys())[list(distances_dic.values()).index(minimum)]
            clustering_step[best_cluster].append(list(x))
        return clustering_step

    def improve_clusters(self, clustering_step):
        """ Improve cluster centroids by calculating mean of clusters """
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
        """ Compare new clusters with previous clusters. If same, break, else continue to improve clusters """
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

    def clusterings(self, array, dist):
        """ Put algorithm together """
        clusterings = {}
        new_cents = {}
        for new_centroids in range(initialise):
            mü_one = self.initialise_centroids(array)

            for i in range(iterations):
                if i==0:
                    compare = self.assign_clusters(mü_one, array, dist)
                    mü = self.improve_clusters(compare)
                else:
                    clusters = self.assign_clusters(mü, array, dist)
                    mü = self.improve_clusters(clusters)
                    if self.compare_results(clusters, compare) == set():
                        compare = clusters
                        break
                    else:
                        compare = clusters
                clusterings[i] = compare
            new_cents[new_centroids] = clusterings
        return new_cents, mü, clusterings

    def find_best_cluster(self, new_cents, mü):
        """ Find best clustering result in all initialisations and iterations """
        distances = []
        distances_per_cluster = {}
        iters = {}
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
                iters[key] = np.mean(list(distances_per_cluster.values()))
            all_iterations[c] = iters
        return all_iterations

    def labels_datapoints(self, all_iterations, clusterings):
        """ Prepare labels and datapoints for visualisation of clusters """
        labels = []
        datapoints = []
        for key, value in all_iterations.items():
            for ke, va in all_iterations[key].items():
                if va == min(all_iterations[key].values()):
                    for s,v in clusterings[key].items():
                        l = len(clusterings[key][s])
                        labels.extend([s for i in range(l)])
                        for datapair in v:
                            datapoints.append(tuple(datapair))
        return labels, datapoints

    def visualise_clusters(self, labels, datapoints):
        """ Visualise best cluster model """
        ws = []
        es = []
        for w, e in datapoints:
            ws.append(w)
            es.append(e)

        fig = plt.figure(figsize=(8, 8))
        sns.scatterplot(ws, es, hue=labels, marker="o", palette=sns.color_palette("hls", k), legend=False)
        plt.savefig("teresa_kmeans.png")
        plt.show()



path = "songs_25.csv"
k = 15 # input number of clusters 2 - 10
iterations = 3 # number of improvements of cluster
initialise = 2 # number of new initialisations of mü; 50 - 1000

kmeans = KMeans(path, k, iterations, initialise)
array = kmeans.prepare_data()
new_cents, mü, clusterings = kmeans.clusterings(array, distance.euclidean)
all_iterations = kmeans.find_best_cluster(new_cents, mü)
labels, datapoints = kmeans.labels_datapoints(all_iterations, clusterings)
kmeans.visualise_clusters(labels, datapoints)