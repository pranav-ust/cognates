from math import ceil, floor
from shingle import *
from graph import *

port_ro_cog = dict()
port_ro_noncog = dict()

def init_dict():

    # for cognates
    cogs = open("data/portuguese/graph_cognates_freq.txt", "r+")
    for line in cogs:
        splits = line.rstrip().split()
        port_ro_cog[(splits[1], splits[2])] = int(splits[0])
    cogs.close()

    # for non cognates
    noncogs = open("data/portuguese/graph_noncognates_freq.txt", "r+")
    for line in noncogs:
        splits = line.rstrip().split()
        port_ro_noncog[(splits[1], splits[2])] = int(splits[0])
    noncogs.close()

def pi(source, target, k = 1):
    query = two_ends(source, 2) #Your query
    document = two_ends(target, 2) #Your document
    qd = common_elements(query, document) # q cap d
    first = uncommon_elements(query, qd) # q - (q cap d)
    second = uncommon_elements(document, qd) # d - (q cap d)
    graph = graph_model(first,second)
    res = sum([port_ro_cog[i]**k for i in graph]) # sum the frequencies in the dictionary
    return res / len(graph)
