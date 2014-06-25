#!/usr/bin/env
"""
Script for Jacunski exercise 5. 
"""
import csv, gzip
from sys import argv
from sys import exit
from os.path import exists


def main(arguments):

    input_name, output_name, terms_file, in_number = arguments[1:5]
    header_length, field_nums = parse_num(in_number)
    # print header_length
    print field_nums

    open_flag = check_files(input_name, output_name)
    read_flag = 'rb'

    t = {}
    terms = load_file(terms_file, read_flag)
    load_terms(terms, t)
    #print t


    i = load_file(input_name, read_flag)
    o = load_file(output_name, open_flag)

    #print i.read()

    csv_loop(i, o, '\t', t, field_nums)


def csv_loop(inp, out, delimiter, di, fields):
    """uses csv to read file and print appropriate lines"""
    rd = csv.reader(inp, delimiter=delimiter)
    wr = csv.writer(out, delimiter=delimiter)
    # loops through list of fields in the row, writes the [x] field
    for row in rd:
        #print row
        for w in row:
            if w in di:
                wr.writerow([row[y] for y in fields])


def load_terms(inp, d):
    """
    Takes file as input, creates a list of words, iterates over the list, 
    checking if each word is in the dictionary. If the word isn't, it 
    creates an entry with value 1. If it is, it adds 1 to the existing entry.
    """
    x = []
    for line in inp.readlines():
        x.append(line.strip('\n'))

    for word in x:
        if word in d:
            pass
        else:
            d[word] = 'exists'


def check_files(f1, f2):
    """checks if the input and output files exist"""
    write = 'wb'
    append = 'ab'
    if exists(f1):
        print 'Input file exists'

    else:
        print 'Invalid input file'
        exit()

    if exists(f2):
        print 'Output file exists. Overwrite (o), append (a), or quit (q)?'
        a = str(raw_input('> '))
        if a[0] == 'o' or a[0] == 'O':
            return write

        elif a[0] == 'a' or a[0] == 'A':
            return append

        elif a[0] == 'q' or a[0] == 'Q':
            print 'Quitting program.'
            exit()

        else:
            print 'Invalid input. Quitting program.'
            exit()  

    else:
        print 'Writing output file.'
        return write


def load_file(file_name, flag):
    """
    Checks the file type and calls an error message if invalid. 
    """
    if file_name[-2:] == 'gz':
        return gzip.open(file_name, flag)

    if file_name[-3:] == 'txt' or file_name[-3:] == 'csv':
        return open(file_name, flag)

    else:
        print 'File must be .txt or .gz. Aborting program.'
        exit()


def parse_num(num):
    a = []
    for i in range(0, len(num)):
        try:
            a.append(int(num[i]))
        except TypeError:
            print 'Final argument must include all integer characters.'
            exit()

    hl = a[0]
    fs = a[1:]
    return hl, fs



if __name__ == '__main__':
    main(argv)