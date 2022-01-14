"""Gendiff script."""

from gendiff import cli, generate_diff, parser
from gendiff.views import plain, stylish


FORMATTERS = {
    'stylish': stylish,
    'plain': plain,
}


def main():
    path1, path2 = cli.args.first_file, cli.args.second_file
    formatter = FORMATTERS[cli.args.format]
    dict1 = parser.parse(path1)
    dict2 = parser.parse(path2)
    print(formatter.format_diff(generate_diff(dict1, dict2)))


if __name__ == '__main__':
    main()
