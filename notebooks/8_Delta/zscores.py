import glob
import regex as re
from collections import Counter

import pandas as pd

from scipy.stats import zscore
from scipy.spatial import distance

import nltk
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import CountVectorizer

class Zscores():
    def __init__(self, data):
        self.data = data

    def remove_stopwords(self):
        stopword = open("de_stopwords.txt")
        stopwords = stopword.read()
        self.data['text'] = [str(i).lower() for i in self.data['text']]
        self.data['removedstopword'] = self.data['text'].apply(lambda x: ' '.join([item for item in str(x).split() if item not in stopwords]))
        return self.data


    def count_frequencies(self, df):
        freq_list = []
        for i, row in df.iterrows():
            title = str(row.Genre1)+'_'+str(row.artist)+'-'+str(row.decades)
            vocab = Counter(row.removedstopword.split())
            frequencies = list(vocab.values())
            words = list(vocab.keys())
            freq_list.append(pd.Series(frequencies, words, name=title))
        return freq_list

    def calculate_zscores(self):
        df = self.remove_stopwords()
        freq_list = self.count_frequencies(df)
        counts = pd.DataFrame(freq_list)
        counts = counts.fillna(0)
        counts = counts.div(counts.sum(axis=1), axis=0)
        counts.loc['Total_per_word'] = counts.sum()
        counts = counts.sort_values(by='Total_per_word', axis=1, ascending=False)
        counts.drop('Total_per_word', inplace=True, axis=0)
        print(counts)

        zscores = (counts - counts.mean()) / counts.std()
        # zscores = counts.apply(zscore)
        print(zscores)

        zscores.drop(zscores.columns[1000:], inplace=True, axis=1)

        return zscores


poems = pd.read_csv('vier_genres.csv', index_col=[0])
z = Zscores(poems)
zscores = z.calculate_zscores()
zscores.to_csv('zscores_vier_genres.csv')