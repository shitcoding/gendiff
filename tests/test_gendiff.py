import json
import os
from gendiff import generate_diff


def get_fixture_path(fixture_filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', fixture_filename)


def read_file(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    return data


def test_plain_json():
    data1 = json.load(open(get_fixture_path('plain1.json')))
    data2 = json.load(open(get_fixture_path('plain2.json')))
    expected = read_file(get_fixture_path('plain_json_expected.txt')).rstrip()
    assert generate_diff(data1, data2) == expected
