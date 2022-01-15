import os
from gendiff import generate_diff


def get_fixture_path(fixture_filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', fixture_filename)


def read_file(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    return data


def get_expected_output(output_fixture_file_name):
    return read_file(get_fixture_path(output_fixture_file_name)).rstrip()


# Formatter: stylish
def test_plain_json_stylish_formatter():
    path1 = get_fixture_path('plain1.json')
    path2 = get_fixture_path('plain2.json')
    expected = get_expected_output('plain_expected_stylish.txt')
    assert generate_diff(path1, path2) == expected


def test_plain_yaml_stylish_formatter():
    path1 = get_fixture_path('plain1.yaml')
    path2 = get_fixture_path('plain2.yaml')
    expected = get_expected_output('plain_expected_stylish.txt')
    assert generate_diff(path1, path2) == expected


def test_nested_json_stylish_formatter():
    path1 = get_fixture_path('nested1.json')
    path2 = get_fixture_path('nested2.json')
    expected = get_expected_output('nested_expected_stylish.txt')
    assert generate_diff(path1, path2) == expected


def test_nested_yaml_stylish_formatter():
    path1 = get_fixture_path('nested1.yaml')
    path2 = get_fixture_path('nested2.yaml')
    expected = get_expected_output('nested_expected_stylish.txt')
    assert generate_diff(path1, path2) == expected


# Formatter: plain
def test_nested_json_plain_formatter():
    path1 = get_fixture_path('nested1.json')
    path2 = get_fixture_path('nested2.json')
    expected = get_expected_output('nested_expected_plain.txt')
    assert generate_diff(path1, path2, formatter='plain') == expected


def test_nested_yaml_plain_formatter():
    path1 = get_fixture_path('nested1.yaml')
    path2 = get_fixture_path('nested2.yaml')
    expected = get_expected_output('nested_expected_plain.txt')
    assert generate_diff(path1, path2, formatter='plain') == expected


# Formatter: Json
def test_nested_json_json_formatter():
    path1 = get_fixture_path('nested1.json')
    path2 = get_fixture_path('nested2.json')
    expected = get_expected_output('nested_expected_json.txt')
    assert generate_diff(path1, path2, formatter='json') == expected


def test_nested_yaml_json_formatter():
    path1 = get_fixture_path('nested1.yaml')
    path2 = get_fixture_path('nested2.yaml')
    expected = get_expected_output('nested_expected_json.txt')
    assert generate_diff(path1, path2, formatter='json') == expected

