"""Parsing and processing script arguments from CLI."""

import argparse


parser = argparse.ArgumentParser(prog='gendiff',
                                 description='Generate diff')
parser.add_argument('first_file')   # Path to first file
parser.add_argument('second_file')  # Path to second file
parser.add_argument('-f', '--format',
                    choices=['stylish', 'plain', 'json'],
                    default='stylish',
                    help='set format of output'
                    )

args = parser.parse_args()
