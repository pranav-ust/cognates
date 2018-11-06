from src.shingle import *
from src.graph import *
from src.sim_functions import *
from error import *

import numpy as np

portuguese = open('data/portuguese/port.txt', "r+")
wordlist = {}
for line in portuguese:
    word = line.rstrip()
    wordlist[word] = two_ends(word, 2)

train = open('data/portuguese/portuguese_train_mrr.txt', "r+")
pairs = []
for line in train:
    word = line.rstrip().split('____')
    pairs.append((word[0], word[1]))
data = [(p[0], two_ends(p[0],2), p[1]) for p in pairs]
avgdl = np.mean([len(s[1]) for s in data])
print("Average is", avgdl)

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

def pi(source, target, k = 1.5):
    query = two_ends(source, 2) #Your query
    document = two_ends(target, 2) #Your document
    qd = common_elements(query, document) # q cap d
    first = uncommon_elements(query, qd) # q - (q cap d)
    second = uncommon_elements(document, qd) # d - (q cap d)
    graph = graph_model(first,second)
    res = 0 # sum the frequencies in the dictionary
    for i in graph:
        if i in port_ro_cog:
            res += port_ro_cog[i] ** k
    return res / len(graph)

# Initialize counts
frequencies = {}
text = open("data/portuguese/two_ends.txt", "r+")
for line in text:
    word = line.strip().split(' ')
    frequencies[word[0]] = float(word[1])

def score(query, document, alpha = 0.5):
    return alpha * pi(query, document) + (1.0 - alpha) * dirichlet(two_ends(query, 2), two_ends(document, 2))

for source in data:
    score_list = []
    for key in wordlist:
        score_list.append((key, score(key, source[0])))
    score_list = sorted(score_list, key=lambda x: x[1], reverse=True)

    for i in range(5):
        print(score_list[i])
