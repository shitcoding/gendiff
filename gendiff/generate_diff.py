"""Generate diff string."""

from gendiff.diff import make_diff
from gendiff.parser import parse
from gendiff.views import json, plain, stylish


FORMATTERS = {
    'json': json,
    'plain': plain,
    'stylish': stylish,
}


def generate_diff(path1, path2, formatter='stylish'):
    dict1, dict2 = parse(path1), parse(path2)
    formatter = FORMATTERS[formatter]
    return formatter.format_diff(make_diff(dict1, dict2))
