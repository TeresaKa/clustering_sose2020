import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize

import random

from scipy.spatial import distance

path = "songs_25.csv"
k = 8 # input number of clusters 2 - 10
iterations = ... # number of new initialisations of mü; 50 - 1000
c = ... #index of k


def prepare_data(path):
    songs = pd.read_csv(path)
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


def assign_clusters():
    mü, array = initialise_centroids(k)
    clustering_step = {}
    for x in array:
        distances_dic={}
        for i in range(k):
            d = distance.euclidean(x, mü[i])
            distances_dic[i] = d
        minimum = min(distances_dic.values())
        best_cluster = list(distances_dic.keys())[list(distances_dic.values()).index(minimum)]

        if best_cluster in clustering_step.keys():
            clustering_step[best_cluster].append(x)
        else:
            clustering_step[best_cluster] = x

    return clustering_step

print(assign_clusters())
# def improve_clusters():
#     compare = {}
#     for key, values in clustering_step:
#         if clustering_step[key] == compare[key]:  #bzw. set(l1).union ...etc.
#             break
#         else:
#             compare = clustering_step
#             for i in k:
#                 mü[i] = mean(clustering_step[i])
#                 assign_clusters()(mü)
#
# #Schleife mit für Neuinitialisierungen
# for i in iterations:
#     # assign_clusters()
#     # impr = improve_clusters()
#     clusterings[i] = impr
#     #calculate best model
#
# # l1 = [1,2,3,4]
# # l2 = [2,3,4,1]
# #
# # if set(l1).union(set(l2))-set(l1).intersection(set(l2)) == set():
# #     print("None")