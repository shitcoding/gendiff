import json
import os
import yaml
from gendiff import generate_diff
from gendiff.views import stylish, plain


def get_fixture_path(fixture_filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', fixture_filename)


def read_file(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    return data


def get_json_data(json_file_name):
    return json.load(open(get_fixture_path(json_file_name)))


def get_yaml_data(yaml_file_name):
    return yaml.safe_load(open(get_fixture_path(yaml_file_name)))


def get_expected_output(output_fixture_file_name):
    return read_file(get_fixture_path(output_fixture_file_name)).rstrip()


# Formatter: stylish
def test_plain_json_stylish_formatter():
    data1, data2 = get_json_data('plain1.json'), get_json_data('plain2.json')
    expected = get_expected_output('plain_expected_stylish.txt')
    assert stylish.format_diff(generate_diff(data1, data2)) == expected


def test_plain_yaml_stylish_formatter():
    data1, data2 = get_yaml_data('plain1.yaml'), get_yaml_data('plain2.yaml')
    expected = get_expected_output('plain_expected_stylish.txt')
    assert stylish.format_diff(generate_diff(data1, data2)) == expected


def test_nested_json_stylish_formatter():
    data1, data2 = get_json_data('nested1.json'), get_json_data('nested2.json')
    expected = get_expected_output('nested_expected_stylish.txt')
    assert stylish.format_diff(generate_diff(data1, data2)) == expected


def test_nested_yaml_stylish_formatter():
    data1, data2 = get_yaml_data('nested1.yaml'), get_yaml_data('nested2.yaml')
    expected = get_expected_output('nested_expected_stylish.txt')
    assert stylish.format_diff(generate_diff(data1, data2)) == expected


# Formatter: plain
def test_nested_json_plain_formatter():
    data1, data2 = get_json_data('nested1.json'), get_json_data('nested2.json')
    expected = get_expected_output('nested_expected_plain.txt')
    assert plain.format_diff(generate_diff(data1, data2)) == expected


def test_nested_yaml_plain_formatter():
    data1, data2 = get_yaml_data('nested1.yaml'), get_yaml_data('nested2.yaml')
    expected = get_expected_output('nested_expected_plain.txt')
    assert plain.format_diff(generate_diff(data1, data2)) == expected
