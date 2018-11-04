from math import ceil, floor

def common_elements(list1, list2):
    ''' Carries out set intersection '''
    return [element for element in list1 if element in list2]

def uncommon_elements(list1, list2):
    ''' Carries out set difference '''
    return [element for element in list1 if element not in list2]

def graph_model(first, second):
    ''' Constructs the graphical structure between two shingle sets. '''

    # Step 1: Initialization
    # If the given sets first and second are empty, we initialize
    # them by inserting an empty token, (nun), into those sets.

    if len(first) == 0:
        first.append("nun") #insert empty token if found empty
    if len(second) == 0:
        second.append("nun") #insert empty token if found empty

    # Step 2: Equalization of the set cardinalities
    # The cardinalities of the sets first and second made
    # equal by inserting empty tokens (nun) into the
    # middle of the sets.

    # While loops to equalize the sizes
    while(len(first) < len(second)):
        pos = ceil(len(first) / 2)
        first.insert(pos, "nun")

    # While loops to equalize the sizes
    while(len(first) > len(second)):
        pos = floor(len(second) / 2)
        second.insert(pos, "nun")

    # Step 3: Inserting the mappings of the set members into the graph
    # The empty graph is initialized as graph = {}.
    # The directed edges are generated, originating from every set member
    # of first to every set member of second. This results in a complete
    # directed bipartite graph between first and second sets.

    # Pairs in tuples
    graph = set() #Graph in sets to avoid duplicates

    for i in range(len(first)):
        pair = (first[i], second[i]) # One to one mapping with same index
        graph.add(pair)
    for i in range(len(first) - 1):
        pair = (first[i], second[i + 1]) # One to one mapping with an index ahead
        graph.add(pair)
    if len(first) > 1:
        for i in range(1, len(first)):
            pair = (first[i], second[i - 1]) # One to one mapping with an index before
            graph.add(pair)
    return graph
