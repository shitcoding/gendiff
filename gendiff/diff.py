"""Make diff dictionary with differences between 2 imput dictionaries."""


def make_diff(dict1, dict2):
    diff = {}
    keys = dict1.keys() | dict2.keys()
    for key in keys:
        if key not in dict1:
            # key added to dict2
            value = dict2[key]
            diff[key] = ("added", value)
        elif key not in dict2:
            # key removed
            value = dict1[key]
            diff[key] = ("removed", value)
        elif dict1[key] == dict2[key]:
            # key and value are unchanged
            value = dict1[key]
            diff[key] = ("unchanged", value)
        else:
            # value has changed
            old_value, new_value = dict1[key], dict2[key]
            # both values are nested, generate diff for them
            if isinstance(old_value, dict) and isinstance(new_value, dict):
                value = make_diff(old_value, new_value)
                diff[key] = ("nested", value)
            # one or both values are plain, no need to generate diff
            else:
                diff[key] = ("changed", (old_value, new_value))
    return diff
