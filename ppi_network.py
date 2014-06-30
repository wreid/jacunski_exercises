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

    G = nx.Graph()

    load_txt(inp, G)
    del_dupl(G)


    components = sorted(nx.connected_components(G), key=len, reverse=True)
    graphs = list(nx.connected_component_subgraphs(G, copy=True))
    M = nx.Graph(graphs[0])
    removed = 0

    for component in components[1:]:
        removed = removed + len(component)

    print '%d nodes removed\n' % removed
    print '%d components removed\n' % len(components[1:])

    print '%d nodes and %d edges in main component\n' % (len(M.nodes()), len(M.edges()))



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



if __name__ == '__main__':
    main(argv)