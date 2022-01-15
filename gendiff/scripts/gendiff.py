"""Gendiff script."""

from gendiff import cli, generate_diff, parser
from gendiff.views import json, plain, stylish


FORMATTERS = {
    'json': json,
    'plain': plain,
    'stylish': stylish,
}


def main():
    path1, path2 = cli.args.first_file, cli.args.second_file
    formatter = FORMATTERS[cli.args.format]
    print(formatter.format_diff(generate_diff(path1, path2)))


if __name__ == '__main__':
    main()
