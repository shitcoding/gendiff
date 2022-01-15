"""Parse data from json and yaml files."""

import json
import pathlib
import yaml


def parse(data):
    """
    If 'data' is a dictionary: Return 'data' as it is.
    If 'data' is a file path: Return dictionary containing data from input file.
    Accepts json and yaml files.
    Returns None if extension is not `json`, `yaml` or `yml`.
    """
    if isinstance(data, dict):
        return data
    with open(data, 'r') as f:
        data = f.read()
    path = pathlib.Path(data)
    extension = path.suffix.lower()
    if extension == 'json':
        return json.load(data)
    elif extension == 'yaml' or 'yml':
        return yaml.safe_load(data)
