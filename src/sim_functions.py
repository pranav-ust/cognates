from shingle import *
from math import ceil, floor
import numpy as np

# Initialize counts
frequencies = {}
text = open("data/portuguese/two_ends.txt", "r+")
for line in text:
    word = line.strip().split(' ')
    frequencies[word[0]] = float(word[1])

def tf(intersection, query):
    '''Counts term frequency'''
    tf = [query.count(word) for word in intersection]
    return np.array(tf)

def idf(intersection, document, N):
    '''Counts inverse document frequency'''
    idf = np.array([frequencies[word] for word in intersection])
    idf = np.log10(np.divide(N + 1, idf + 0.5))
    return idf

def tf_idf(query, document, N):
    '''Computes tf-idf'''
    intersection = [word for word in document if word in query] # intersection
    score = np.dot(tf(intersection, query), idf(intersection, document, N))
    return score

def bm25_tf(intersection, query, document, k1, b, avgdl, N):
    '''Computes term frequency for BM25'''
    tf_ = tf(intersection, document)
    numerator = tf_ * (k1 + 1.0)
    denominator = tf_ + k1 * (1.0 - b + b * (len(query) / avgdl))
    bm25_tf = np.divide(numerator, denominator)
    return bm25_tf

def bm25(query, document, k1 = 1.2, b = 0.75, avgdl = 8.3, N = 50000):
    intersection = [word for word in document if word in query] # intersection
    score = np.dot(bm25_tf(intersection, query, document, k1, b, avgdl, N), idf(intersection, document, N))
    return score

shingles = 470751
def smooth(intersection, document, mu):
    smooth = []
    for word in intersection:
        prob = 1.0 + np.divide(document.count(word), mu * frequencies[word] / shingles)
        smooth.append(np.log10(prob))
    smooth = np.array(smooth)
    return smooth

def dirichlet(query, document, mu = 100.0):
    intersection = [word for word in document if word in query] # intersection
    add = len(query) * np.log10(np.divide(mu, mu + len(document)))
    score = np.dot(tf(intersection, query), smooth(intersection , document, mu)) + add
    return score
