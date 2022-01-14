"""Stylish formatter for diffs."""


def rename_spec_values(diff_str):
    '''Changes name of special values from Python specific
    to json specific.
    '''
    REPLACEMENTS = {
        'None': 'null',
        'True': 'true',
        'False': 'false',
    }
    for string, replacement in REPLACEMENTS.items():
        diff_str = diff_str.replace(string, replacement)
    return diff_str


def format_value(value, tab_lvl):
    '''Format value.
    If value is nested (dict): Return formatted nested value string.
    If value is plain (not a dict): Return value.
    '''
    if not isinstance(value, dict):
        return value
    # format nested value
    tab_lvl += 1
    indent = ' ' * 4 * (tab_lvl - 1)
    nested_indent = ' ' * 4 * tab_lvl
    item_strings = []
    for key, val in value.items():
        item_strings.append('{0}{1}: {2}'.format(
            nested_indent,
            key,
            format_value(val, tab_lvl),
        ))
    return '{{\n{0}\n{1}}}'.format(
        '\n'.join(item_strings),
        indent,
    )


def format_entry(entry, tab_lvl):
    # Format diff entry, {key: (status, value)}
    key, (status, value) = entry
    indent = ' ' * 2 * (tab_lvl * 2 - 1)
    if status == "added":
        return "{0}+ {1}: {2}".format(
            indent,
            key,
            format_value(value, tab_lvl)
        )
    elif status == "removed":
        return "{0}- {1}: {2}".format(
            indent,
            key,
            format_value(value, tab_lvl)
        )
    elif status == "unchanged":
        return "{0}  {1}: {2}".format(
            indent,
            key,
            format_value(value, tab_lvl)
        )
    # value changed, one or both values are plain
    elif status == "changed":
        old_value, new_value = value[0], value[1]
        return "{0}- {1}: {2}\n{3}+ {4}: {5}".format(
            indent, key, format_value(old_value, tab_lvl),
            indent, key, format_value(new_value, tab_lvl),
        )
    # value changed, both values are nested: render diff between them
    elif status == "nested":
        return "{0}{1}: {2}".format(
            ' ' * 4 * tab_lvl,
            key,
            format_diff(value, tab_lvl)
        )


def format_diff(diff, tab_lvl=0):
    diff_strings = []
    for entry in sorted(diff.items()):
        diff_strings.append(format_entry(entry, tab_lvl + 1))
    closing_bracket_indent = ' ' * 4 * tab_lvl
    diff = "\n".join(["{"] + diff_strings + [closing_bracket_indent + "}"])
    return rename_spec_values(diff)
