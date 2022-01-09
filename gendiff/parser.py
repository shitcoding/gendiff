"""Parse data from json and yaml files."""

import json
import pathlib
import yaml


def parse(file_path):
    """
    Return dictionary containing data from input file.
    Accepts json and yaml files.
    Returns None if extension is not `json`, `yaml` or `yml`.
    """
    with open(file_path, 'r') as f:
        data = f.read()
    path = pathlib.Path(file_path)
    extension = path.suffix.lower()
    if extension == 'json':
        return json.load(data)
    elif extension == 'yaml' or 'yml':
        return yaml.safe_load(data)
