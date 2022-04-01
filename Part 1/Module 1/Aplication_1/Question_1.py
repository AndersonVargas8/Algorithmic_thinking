import urllib2

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print("Loaded graph with", len(graph_lines), "nodes")
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

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
    dist_in_degrees = {}
    
    for each in in_degrees:
        if in_degrees[each] in dist_in_degrees:
            dist_in_degrees[in_degrees[each]] += 1
        else:
            dist_in_degrees[in_degrees[each]] = 1
    
    return dist_in_degrees

def normalized_distribution(digraph):
    """
    Generate the normalized distribution of the in_degrees in the digraph
    """
    in_degree_dist = in_degree_distribution(digraph)
    
    total = 0
    
    for each in in_degree_dist:
        total += in_degree_dist[each]
    norm_dist = {}
    
    for each in in_degree_dist:
         norm_dist[each] = in_degree_dist[each]/float(total)
         
    return norm_dist

       
cit_graph = load_graph(CITATION_URL)

#create a normalized in_degree distribution

norm_in_degree = normalized_distribution(cit_graph)

# generate plot

import matplotlib.pyplot as plt
import math

for key, value in norm_in_degree.items():
   x = key
   y = value
   plt.scatter(x,y)

#plt.legend(norm_indegree.keys())
plt.xscale('log')
plt.yscale('log')
plt.xlim(0.1, 2000)
plt.title('Normalized in-degree distribution of the citation graph\n')
plt.ylabel('Normalized distribution')
plt.xlabel('Num of papers')
plt.show()