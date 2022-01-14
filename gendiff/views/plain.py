"""Plain formatter for diffs."""

from gendiff.views.stylish import rename_spec_values


def format_value(value):
    """Formats value for plain formatter output.
    If value is string, return 'value'.
    If value is nested (dict): return [complex value]
    Otherwise return value as it is.
    """
    if isinstance(value, str):
        return "'{0}'".format(value)
    elif isinstance(value, dict):
        return "[complex value]"
    return value


def format_diff(diff, ancestry=""):
    """Returns formatted diff string in plain format.
    Format:
        - Property 'parent1.parent2.key' was added with value: 'value'
        - Property 'parent1.parent2.key' was updated. \
          From 'old_value' to 'new_value'
        - Property 'parent1.parent2.key' was removed.
    """
    diff_strings = []
    for entry in sorted(diff.items()):
        key, (status, value) = entry
        key = ancestry + key
        if status == "removed":
            diff_strings.append("Property '{0}' was removed".format(key))
        elif status == "added":
            diff_strings.append(
                "Property '{0}' was {1} with value: {2}".format(
                    key, status, format_value(value)
                )
            )
        elif status == "changed":
            old_value, new_value = value[0], value[1]
            diff_strings.append(
                "Property '{0}' was updated. ".format(key)
                + "From {0} to {1}".format(
                    format_value(old_value), format_value(new_value)
                )
            )
        elif status == "nested":
            diff_strings.append(format_diff(value, key + "."))
    diff = "\n".join(diff_strings)
    return rename_spec_values(diff)
