"""
The following are examples of representation of graphs with dictionaries
"""

EX_GRAPH0 = {
    0:set([1,2]),
    1:set(),
    2:set()
}

EX_GRAPH1 = {
    0:set([1,4,5]),
    1:set([2,6]),
    2:set([3]),
    3:set([0]),
    4:set([1]),
    5:set([2]),
    6:set()
}

EX_GRAPH2 = {
    0:set([1,4,5]),
    1:set([2,6]),
    2:set([3,7]),
    3:set([7]),
    4:set([1]),
    5:set([2]),
    6:set(),
    7:set([3]),
    8:set([1,2]),
    9:set([0,3,4,5,6,7])
}


def make_complete_graph(num_nodes):
    """
    Receive a positive number and returns a dictionary that represents a complete 
    directed graph
    """
    graph = {}
    for dummy_i in range(num_nodes):
        graph[dummy_i] = set()
        for dummy_j in range(num_nodes):
            if dummy_i != dummy_j:
                graph[dummy_i].add(dummy_j)
        
    return graph

#print(make_complete_graph(5))

def compute_in_degrees(digraph):
    """Receive a directed graph and return a list of in-dregress
    """
    in_degrees = {}
    for each in digraph:
        in_degrees[each] = 0
        
    for dummy_i in digraph:
        for each in digraph[dummy_i]:
            in_degrees[each] += 1

    return in_degrees

def in_degree_distribution(digraph):
    """Return a dictionary with de in-degree distributions of the graph
    """
    in_degrees = compute_in_degrees(digraph)
    total_in_degrees = {}
    for dummy_i in in_degrees.values():
        total_in_degrees[dummy_i] = sum(value == dummy_i for value in in_degrees.values())
    
    return total_in_degrees

print(in_degree_distribution(make_complete_graph(5)))

