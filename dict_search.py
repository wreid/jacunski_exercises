#!/usr/bin/env
"""
Script for Jacunski exercise 5. 
"""
import csv
from sys import argv
from sys import exit
from os.path import exists

def main(arguments):

    input_name, output_name, terms_file, in_number = arguments[1:5]
    header_length, fields = parse_num(in_number)
    print header_length
    print fields

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