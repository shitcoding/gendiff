"""Generate diff string."""

from gendiff.diff import make_diff
from gendiff.parser import parse
from gendiff.read import read_file
from gendiff.formatters.formatters import FORMATTERS


def generate_diff(path1, path2, formatter='stylish'):
    data1, file_type1 = read_file(path1)
    data2, file_type2 = read_file(path2)
    dict1, dict2 = parse(data1, file_type1), parse(data2, file_type2)
    formatter = FORMATTERS[formatter]
    return formatter.format_diff(make_diff(dict1, dict2))
