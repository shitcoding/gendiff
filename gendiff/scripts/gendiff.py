"""Gendiff script."""

import json
from gendiff import cli, generate_diff


def main():
    path1, path2 = cli.args.first_file, cli.args.second_file
    dict1 = json.load(open(path1))
    dict2 = json.load(open(path2))
    print(generate_diff(dict1, dict2))


if __name__ == '__main__':
    main()
