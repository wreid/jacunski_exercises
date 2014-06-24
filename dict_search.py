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



if __name__ == '__main__':
    main(argv)

def parse_num(num):
    for i in range(0, len(num)):
        try:
            a = int(num[i])
        except TypeError:
            print 'Final argument must include all integer characters.'
            exit()
