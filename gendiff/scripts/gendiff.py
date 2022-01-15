"""Gendiff script."""

from gendiff import cli, generate_diff


def main():
    path1, path2 = cli.args.first_file, cli.args.second_file
    formatter = cli.args.format
    return print(generate_diff(path1, path2, formatter))


if __name__ == '__main__':
    main()
