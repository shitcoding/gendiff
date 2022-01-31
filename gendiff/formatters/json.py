"""Json formatter for diffs."""

import json


def format_diff(diff):
    """Return diff in json format."""
    return json.dumps(diff, sort_keys=True, indent=4)
