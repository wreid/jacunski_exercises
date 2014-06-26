#!/usr/bin

import networkx as nx
import matplotlib as plt
from sys import argv
from sys import exit

def main(args):
    input_file = args[1]
    input_num = args[2]
    try:
        dthresh = int(input_num)
    except TypeError:
        print 'Threshold number must be an integer.'
        exit()

    try:
        inp = str(input_file)
    except TypeError:
        print 'Input file name must be a string.'
        exit()

    G=nx.Graph()

    add_edges(load_txt(inp), G)
    del_dupl(G)

    degree_threshold(dthresh, G)
    print nx.degree(G)

    #nx.draw(G)
    #plt.pyplot.show()


def load_txt(fname):
    """
    loads text from a file and removes whitespace
    """
    f = open(fname, 'rb')
    txt = f.readlines()

    for line in txt:
        line.strip()

    return txt


def add_edges(input, graph):
    """
    converts each line into a tuple of two proteins,
    adding the tuple as a pair of nodes connected by and edge
    """
    for line in input:
        l = tuple(line.split())
        graph.add_edge(*l)


def del_dupl(graph):
    """
    iterates through graph, deleting duplicate edges
    """
    for edge in graph.edges():
        if edge[0] == edge[1]:
            graph.remove_edge(edge[0], edge[1])


def degree_threshold(thresh, graph):
    for node in nx.degree(graph):
        if graph[node] < thresh:
            graph.remove_node(node)

if __name__ == '__main__':
    main(argv)