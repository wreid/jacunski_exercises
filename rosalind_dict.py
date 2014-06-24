"""
Script for the Rosalind dictionary problem.
"""
import csv
from sys import argv
from sys import exit

def load_terms(inp, d):
    """
    Iterates over a list of words, checking if each word is in the dictionary.
    If the word isn't, it creates an entry with value 1. If it is, it adds 1 to
    the existing entry.
    """
    for word in inp:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

def main(argv):
    with open(argv[2], 'wb') as o:
        with open(argv[1], 'rb') as f:
            words = {}
            reader = csv.reader(f, delimiter=' ')
            for line in reader:
                load_terms(line, words)
            for key, value in words.items():
                o.write('%s %d\n' % (key, value))

if __name__ == '__main__':
    main(argv)