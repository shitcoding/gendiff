"""Parsing and processing script arguments from CLI."""

import argparse


parser = argparse.ArgumentParser(prog='gendiff',
                                 description='Generate diff')
parser.add_argument('first_file', nargs=1)
parser.add_argument('second_file', nargs=1)
parser.add_argument('-f', '--format', nargs=1, help='set format of output')

args = parser.parse_args()
