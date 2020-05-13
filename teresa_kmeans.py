import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize

import random

from scipy.spatial import distance

path = "songs_25.csv"
k = 8 # input number of clusters 2 - 10
iterations = ... # number of improvements of cluster
ini = ...# number of new initialisations of mü; 50 - 1000


def prepare_data(path):
    songs = pd.read_csv(path)
    songs = songs[:100]  #löschen!!
    data = songs['text']
    tf_idf_vectorizer = TfidfVectorizer()
    tf_idf = tf_idf_vectorizer.fit_transform(data)
    tf_idf_norm = normalize(tf_idf)
    array = tf_idf_norm.toarray()
    return array


def initialise_centroids(k):
    mü = {}
    array = prepare_data(path)
    idx = np.random.randint(array.shape[0], size=k)
    centroids = array[idx, :]
    for i in range(len(centroids)):
        mü[i] = list(centroids[i])
    return mü, array

def assign_clusters(mü):
    clustering_step = {}
    for x in array:
        distances_dic={}
        for i in range(k):
            d = distance.euclidean(x, mü[i])
            distances_dic[i] = d
        minimum = min(distances_dic.values())
        best_cluster = list(distances_dic.keys())[list(distances_dic.values()).index(minimum)]

        if best_cluster in clustering_step.keys():
            clustering_step[best_cluster].append(list(x))
        else:
            clustering_step[best_cluster] = list(x)

    return clustering_step


def improve_clusters(clustering_step):
    for i in k:
        mü[i] = mean(clustering_step[i])
    return mü


def compare_results():
    for key, values in clustering_step.items():
        #if clustering_step[key] == compare[key]:
        union = set(clustering_step[key]).union(set(compare[key]))
        intersection = set(clustering_step[key]).intersection(set(compare[key]))
        if union - intersection == set():
            break
        else:
            compare = clustering_step
    return compare
#
# #Schleife mit für Neuinitialisierungen

# compare = {}
# for i in iterations:
#     if i==0:
#         mü, array = initialise_centroids(k)
#         compare = assign_clusters(mü)
#     else:
#         mü = improve_clusters()
#         clustering_step = assign_clusters(mü)
#         clusterings[i] = impr
    #calculate best model
#
