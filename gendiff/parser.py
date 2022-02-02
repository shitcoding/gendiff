"""Parse data from json and yaml files."""

import json
import yaml


def parse(data, file_type):
    """
    Parse data according to file_type, return dictionary.
    Return None if file_type is not `json`, `yaml` or `yml`.
    """
    if file_type == 'json':
        return json.load(data)
    elif file_type == 'yaml' or 'yml':
        return yaml.safe_load(data)
