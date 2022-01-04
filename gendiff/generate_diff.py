"""Generate diff string between 2 dictionaries."""


def generate_diff(dict1, dict2):
    """
    Return diff string between 2 dictionaries.

    Returns:
        str
    """
    diff_items = []
    keys = dict1.keys() | dict2.keys()
    for key in sorted(keys):
        if key not in dict1:
            diff_items.append('  + {0}: {1}'.format(key, dict2[key]))
        elif key not in dict2:
            diff_items.append('  - {0}: {1}'.format(key, dict1[key]))
        elif dict1[key] == dict2[key]:
            diff_items.append('    {0}: {1}'.format(key, dict1[key]))
        else:
            diff_items.append('  - {0}: {1}'.format(key, dict1[key]))
            diff_items.append('  + {0}: {1}'.format(key, dict2[key]))
    return '\n'.join(['{'] + diff_items + ['}']).lower()
