import json
from gendiff import generate_diff


EXPECTED_PLAIN_JSON_DIFF = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""


def test_plain_json():
    data1 = json.load(open('./tests/fixtures/plain_file1.json'))
    data2 = json.load(open('./tests/fixtures/plain_file2.json'))
    assert generate_diff(data1, data2) == EXPECTED_PLAIN_JSON_DIFF
