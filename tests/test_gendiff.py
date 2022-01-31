import os
from gendiff import generate_diff
import pytest


def get_path(fixture_filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', fixture_filename)


def read_fixture(filename):
    path = get_path(filename)
    with open(path, 'r') as f:
        data = f.read()
        return data.rstrip()


TEST_CASES = [
    ("plain1.json", "plain2.json", "stylish", "plain_expected_stylish.txt"),
    ("plain1.yaml", "plain2.yaml", "stylish", "plain_expected_stylish.txt"),
    ("nested1.json", "nested2.json", "stylish", "nested_expected_stylish.txt"),
    ("nested1.yaml", "nested2.yaml", "stylish", "nested_expected_stylish.txt"),
    ("nested1.json", "nested2.json", "plain", "nested_expected_plain.txt"),
    ("nested1.yaml", "nested2.yaml", "plain", "nested_expected_plain.txt"),
    ("nested1.json", "nested2.json", "json", "nested_expected_json.txt"),
    ("nested1.yaml", "nested2.yaml", "json", "nested_expected_json.txt"),
]


@pytest.mark.parametrize("file1, file2, formatter, expected", TEST_CASES)
def test_gendiff(file1, file2, formatter, expected):
    path1 = get_path(file1)
    path2 = get_path(file2)
    assert generate_diff(path1, path2, formatter) == read_fixture(expected)
