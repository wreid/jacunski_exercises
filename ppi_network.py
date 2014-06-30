#!/usr/bin/env

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from sys import argv
from sys import exit

def main(args):
    input_file1 = args[1]
    input_file2 = args[2]

    try:
        inp1 = str(input_file1)
    except TypeError:
        print 'Input file name must be a string.'
        exit()

    try:
        inp2 = str(input_file2)
    except TypeError:
        print 'Input file name must be a string.'
        exit()

    Y = nx.Graph()
    H = nx.Graph()

    load_txt(inp2, Y)
    del_dupl(Y)

    load_txt(inp1, H)
    del_dupl(H)

    print '\nYEAST'
    MY = largest_component(Y)

    print 'HUMAN'
    MH = largest_component(H)

    plt.xlabel('degree', fontsize=14, color='blue')
    plt.ylabel('frequency', fontsize=14, color='blue')
    plt.autoscale(enable=True)
    n1, bins1, patches1 = plt.hist(nx.degree(MY).values(), \
        bins=np.max(nx.degree(MY).values())/25, log=True, histtype='bar', \
        color='blue', alpha=1.0)
    n2, bins2, patches2 = plt.hist(nx.degree(MH).values(), \
        bins=np.max(nx.degree(MH).values())/25, log=True, histtype='bar', \
        color='red', alpha=.3)
    d, p = stats.ks_2samp(n1, n2)
    print 'D value of %f' % d
    print 'P value of %f' % p
    plt.show()
    plt.close()


def load_txt(fname, graph):
    """
    loads text from a file, removes whitespace and loads
    each line as two nodes connected by an edge
    """
    f = open(fname, 'rb')
    txt = f.readlines()

    for line in txt:
        line.strip()
        l = tuple(line.split())
        if l[0] != l[1]:
            graph.add_edge(*l)


def del_dupl(graph):
    """
    iterates through graph, deleting duplicate edges
    """
    for edge in graph.edges():
        if edge[0] == edge[1]:
            graph.remove_edge(edge[0], edge[1])


def largest_component(graph):
    """
    makes a new graph of the largest component in the input graph
    """
    # find and output graph
    graphs = list(nx.connected_component_subgraphs(graph, copy=True))
    most = 0
    for subgraph in graphs:
        if len(list(subgraph)) >= most:
            most = len(list(subgraph))
            out_graph = nx.Graph(subgraph)

    # print info
    components = sorted(nx.connected_components(graph), key=len, reverse=True)
    removed = 0

    for component in components[1:]:
        removed = removed + len(component)
    print '%d nodes removed' % removed
    print '%d components removed' % len(components[1:])
    print '%d nodes and %d edges in main component\n' % (len(out_graph.nodes()), \
        len(out_graph.edges()))

    return out_graph
    
    


if __name__ == '__main__':
    main(argv)