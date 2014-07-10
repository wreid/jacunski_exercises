#!/usr/bin
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from ppi_network import *
from scipy import stats
from sys import argv
from sys import exit

def main(args):
    file1 = args[1]
    file2 = args[2]

    inp1 = sanitize_name(file1)
    inp2 = sanitize_name(file2)

    H = nx.Graph()

    load_txt(inp1, H)
    del_dupl(H)

    d = {}

    with open(inp2) as f:
        load_terms(f, d)

    for node in H.nodes():
        if node not in d:
            H.remove_node(node)

    graphs = sorted(list(nx.connected_component_subgraphs(H, copy=True)), key=len, reverse=True)

    #k = []
    #for graph in graphs[1:]:
    #    for node in graph:
    #        k.append(node)

    #print k

    #C = nx.Graph()
    #for graph in graphs[1:]:
    #    C.add_nodes_from(graph.nodes())
    #    C.add_edges_from(graph.edges())

    #nx.draw(C)
    #plt.show()

    #print "%d nodes deleted\n" % len(k)
    #print k

    #nx.draw(graphs[0], node_size=60, line_width=.1)
    #plt.show()


def load_terms(inp, d):
    """
    Takes file as input, creates a list of words, iterates over the list, 
    checking if each word is in the dictionary. If the word isn't, it 
    creates an entry with value True. 
    """
    x = []
    for line in inp.readlines():
        x.append(line.strip('\r\n'))

    for word in x:
        if word in d:
            pass
        else:
            d[word] = True



if __name__ == '__main__':
    main(argv)