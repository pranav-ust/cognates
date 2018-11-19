##########################
# Demo file for portuguese cognates
# For details, please refer python notebooks
# Author: Pranav
###########################


from src.shingle import *
from src.graph import *
from src.sim_functions import *
from pprint import pprint
import numpy as np

# Initialize the portuguese dictionary

portuguese = open('data/portuguese/port.txt', "r+")
wordlist = {}
for line in portuguese:
    word = line.rstrip()
    wordlist[word] = two_ends(word, 2)

# Initialize the portuguese query words

train = open('data/portuguese/portuguese_train_mrr.txt', "r+")
pairs = []
for line in train:
    word = line.rstrip().split('____')
    pairs.append((word[0], word[1]))
data = [(p[0], two_ends(p[0],2), p[1]) for p in pairs]
avgdl = np.mean([len(s[1]) for s in data])

# Initialize the cognate dictionaries

port_ro_cog = dict()
port_ro_noncog = dict()

def init_dict():
    cogs = open("data/portuguese/graph_cognates_freq.txt", "r+")
    for line in cogs:
        splits = line.rstrip().split()
        port_ro_cog[(splits[1], splits[2])] = int(splits[0])
    cogs.close()
    noncogs = open("data/portuguese/graph_noncognates_freq.txt", "r+")
    for line in noncogs:
        splits = line.rstrip().split()
        port_ro_noncog[(splits[1], splits[2])] = int(splits[0])
    noncogs.close()

init_dict()

# Initialize counts

frequencies = {}
text = open("data/portuguese/two_ends.txt", "r+")
for line in text:
    word = line.strip().split(' ')
    frequencies[word[0]] = float(word[1])

# Error Function

def pi(source, target, k = 1):
    query = two_ends(source, 2) #Your query
    document = two_ends(target, 2) #Your document
    qd = common_elements(query, document) # q cap d
    first = uncommon_elements(query, qd) # q - (q cap d)
    second = uncommon_elements(document, qd) # d - (q cap d)
    graph = graph_model(first, second)
    sum = 0
    for i in graph:
        if i in port_ro_cog:
            sum += port_ro_cog[i] ** k
    return sum / len(graph)

# Similarity function, Dirichlet is being used

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

def score(query, document, alpha = 0.5):
    return alpha * pi(query, document, 1.5) + (1.0 - alpha) * dirichlet(two_ends(query, 2), two_ends(document, 2))

# Loop the data and show the results

for source in data:
    score_list = []
    for key in wordlist:
        score_list.append((key, score(source[0], key)))
    score_list = sorted(score_list, key=lambda x: x[1], reverse=True)

    print("For the cognate " + str(source[0]) + ", top 5 matches are:")

    for i in range(5):
        print(str(i + 1) + ": " + score_list[i][0] + ", score: " + str(score_list[i][1]))

    print("Correct match should be, " + source[2])
